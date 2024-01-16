import pandas as pd
import numpy as np
import os, sys
from src.hap.config.configeration import Configuration_Creator
from src.hap.utils import read_object, save_object
import dill 
from src.hap.logger import logging
import dagshub


preprocessor_dir = Configuration_Creator().create_preprocessor()
transformer_path = os.path.join(preprocessor_dir, 'transformer')

        
raw_data_path = Configuration_Creator().create_ingestion().raw_data_path
train_cleaned_path = os.path.join(raw_data_path,'train_cleaned.csv')
transformer = read_object(transformer_path)
transformed_df = transformer.fit_transform(pd.read_csv(train_cleaned_path))


#print(transformed_df.isnull().sum())


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import mlflow
import bentoml
import dagshub

def mlflow_model_trainer(transformed_df_train):
    param_rf = {
    'n_estimators': [25,50],
        'max_depth': [2, 4, 6,8,10 ],
    'min_samples_leaf': [ 6,8,10,12,15],
        'criterion' :['gini', 'entropy'],
        }
    
    X_train = transformed_df_train.drop('remainder__Heart Attack Risk',axis=1)
    y_train = transformed_df_train['remainder__Heart Attack Risk']
    

    DAGSHUB_TOKEN = dagshub.auth.get_token()
    DAGSHUB_USER = "c1bc62ffb769a24116050c71ba9a357691dd2366"
    
    
    os.environ["MLFLOW_TRACKING_USERNAME"] = DAGSHUB_USER
    os.environ["MLFLOW_TRACKING_PASSWORD"] = DAGSHUB_TOKEN
    
    
    
    mlflow.set_tracking_uri("https://dagshub.com/KartikeyTheDataWrangler/HAP.mlflow")
    rfc = mlflow.set_experiment(experiment_name='my_rf_classifier')
    with mlflow.start_run():
        
        grid_search = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_rf, cv=2, n_jobs=-1)
        grid_search.fit(X_train,y_train)

        best_rf_params = grid_search.best_params_
        logging.info(best_rf_params)
        best_model = grid_search.best_estimator_

        mlflow.log_params(best_rf_params)
        mlflow.sklearn.log_model(best_model, "random-forest-best-model")
        new_model = bentoml.sklearn.save_model("best_model", best_model)
        print(new_model)

    df = mlflow.search_runs(experiment_names=["my_rf_classifier"])
    return df



if __name__ == "__main__":   
    df = mlflow_model_trainer(transformed_df_train=transformed_df) 
    print(df)
    run_id = df.iloc[-1]["run_id"]
    print(run_id)
    model = mlflow.sklearn.load_model("runs:/{}/random-forest-best-model".format(run_id))

