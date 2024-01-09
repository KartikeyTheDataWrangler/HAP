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
from src.hap.utils import save_object

preprocessor_dir = Configuration_Creator().create_preprocessor()
transformer_path = os.path.join(preprocessor_dir, 'transformer')

class DataTransformationConfig:
    def __init__(self):
        self.data_transformation_path = transformer_path
        
    def DataTransformer(self):
        try:
            encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=np.nan)
            
            num_col = ['Cholesterol','Family History ','Alcohol Consumption','Previous Heart Problems','Medication Use','Stress Level',
                       'Physical Activity Days Per Week','Sleep Hours Per Day']
            cat_col = ['Age','Sex','Diet','BMI','Triglycerides','Continent','Pulse Pressure Category','diabetes']
            
            logging.info("Initiating Data Transformer Creation")
            logging.info(f'Cat Cols : {cat_col}')
            logging.info(f'Num Cols: {num_col}')
            
            cat_pipeline = Pipeline(steps=[('encoder',encoder)])
            
            
            transformer_obj = ColumnTransformer(transformers=
                [('cat_pipeline', cat_pipeline, cat_col)]
                ,remainder='passthrough'
            )
            transformer_obj.set_output(transform='pandas')
            
            save_object(obj=transformer_obj, file_path=transformer_path)
            return transformer_obj
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_categories(self,clean_df_path):
        try:
            self.transformer = DataTransformationConfig().DataTransformer()
            self.df = clean_df_path
            
            self.transformer.fit(self.df)
            df_transformed = self.transformer.transform(self.df)
            
            extracted_encoder = self.transformer.named_transformers_['cat_pipeline'].named_steps['encoder']
            
            cat_list = extracted_encoder.categories_    
            encoding = {}
            for i in range(len(cat_list)):
                encoding[df_transformed.columns[i]] = cat_list[i]
            
            for k, v in encoding.items():
                logging.info(f"the encodings of our transformer are col : {k}, encodings = {v}")
            return encoding
        except Exception as e:
            raise CustomException(e,sys)
        
        
raw_data_path = Configuration_Creator().create_ingestion().raw_data_path
train_cleaned_path = os.path.join(raw_data_path,'train_cleaned.csv')

get_categories = DataTransformationConfig()

cat = get_categories.get_categories(clean_df_path=pd.read_csv(train_cleaned_path))
print(cat)
        
    
    


        
        
        
    