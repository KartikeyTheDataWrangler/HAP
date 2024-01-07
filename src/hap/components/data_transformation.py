import pandas as pd
import numpy as np
import os, sys
from src.hap.config.configeration import Configuration_Creator
from src.hap.utils import read_object  # Assuming you have read_object implemented
import dill 
from sklearn.preprocessing import OrdinalEncoder
from src.hap.logger import logging
from src.hap.exception import CustomException
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


preprocessor_dir = Configuration_Creator().create_preprocessor()
transformer_path = os.path.join(preprocessor_dir, 'transformer')

class DataTransformationConfig:
    def __init__(self):
        self.data_transformation_path = transformer_path
        
    def DataTransformer(self):
        try:
            encoder = OrdinalEncoder()
            
            num_col = ['Cholesterol','Family History ','Alcohol Consumption','Previous Heart Problems','Medication Use','Stress Level',
                       'Physical Activity Days Per Week','Sleep Hours Per Day']
            cat_col = ['Age','Sex','Diet','BMI','Triglycerides','Continent','Pulse Pressure Category','diabetes']
            
            logging.info("Initiating Data Transformer Creation")
            logging.info(f'Cat Cols : {cat_col}')
            logging.info(f'Num Cols: {num_col}')
            
            cat_pipeline = Pipeline(steps=[('encoder',encoder)])
            
            
            transformer_obj = ColumnTransformer(
                [('cat_pipeline', cat_pipeline, cat_col)]
                ,remainder='passthrough'
            )
            transformer_obj.set_output(transform='pandas')
            
            return transformer_obj
            
        except Exception as e:
            raise CustomException(e,sys)
    
    



if __name__ == '__main__':
    
    raw_data_path = Configuration_Creator().create_ingestion().raw_data_path
    preprocessor_dir = Configuration_Creator().create_preprocessor()
    preprocessor_path = os.path.join(preprocessor_dir, 'preprocessor')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    train_cleaned_path = os.path.join(raw_data_path,'train_cleaned.csv')

    
   
    df = pd.read_csv(train_data_path)
    
    get_preprocessor = read_object(file_path=preprocessor_path)
    df_= get_preprocessor(df)
    transformer = DataTransformationConfig().DataTransformer()
    print(df_)
    
    transformer.fit(df_)
   
    df_transformed = transformer.transform(df_)
    
    
    print(df_transformed)