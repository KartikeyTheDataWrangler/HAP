import pandas as pd
import numpy as np
import os, sys
from src.hap.config.configeration import Configuration_Creator
from src.hap.utils import read_object, save_object
import mlflow
from src.hap.logger import logging
from src.hap.exception import CustomException
import dagshub
from src.hap.components.model_tranier import mlflow_model_trainer
import warnings
warnings.filterwarnings("ignore")
#importing paths

root_dir = Configuration_Creator().create_ingestion().root_dir
raw_data_path = Configuration_Creator().create_ingestion().raw_data_path
dvc_remote = Configuration_Creator().create_remote()
preprocessor_dir = Configuration_Creator().create_preprocessor()

train_data_csv = os.path.join(raw_data_path,'train.csv')
train_cleaned_data_csv = os.path.join(raw_data_path,'train_cleaned.csv')
preprocssor_path = os.path.join(preprocessor_dir,'preprocessor')
transformer_path = os.path.join(preprocessor_dir, 'transformer')


#prediction pipeline
transformer = read_object(transformer_path)
transformed_df = transformer.fit_transform(pd.read_csv(train_cleaned_data_csv, index_col=False))

try:
    
    #run_id = df.iloc[-1]["run_id"]
    #print(run_id)
    #model = mlflow.sklearn.load_model("runs:/{}/random-forest-best-model".format(run_id))
    
    #loading models from dagshub is resource intensive and takes time hence saving and loading model locally
    
    rf_model = read_object(preprocessor_dir + "/bestmodel")
    print(rf_model)
    input_data = np.array([1,0,1,0,100,1,2,100,1,1,1,100,2,2,500,1]).reshape(1,-1)
    print(input_data.shape)
   
    prediction = rf_model.predict(input_data)
    
    
    print(prediction)
    
    
    logging.info(prediction)
except Exception as e:
    raise CustomException(e,sys)


