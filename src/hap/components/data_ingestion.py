from src.hap.logger import logging
from src.hap.exception import CustomException
import os, sys
from src.hap.config.constants import *
from src.hap.utils import read_yaml_file, create_directories
from src.hap.config.config_entity import DataIngestionConfig
from src.hap.config.configeration import Configuration_Creator
import pandas as pd
from sklearn.model_selection import train_test_split


root_dir = Configuration_Creator().create_ingestion().root_dir
raw_data_path = Configuration_Creator().create_ingestion().raw_data_path

dvc_remote = Configuration_Creator().create_remote()

#csv = pd.read_csv(f'{raw_data_path}/raw.csv')

#print(root_dir, raw_data_path)

class DataIngestion:
    logging.info("Entered Data Ingestion Config")
    
    def __init__(self):
        self.root_dir = root_dir
        self.raw_data_path = raw_data_path
        self.dvc_remote = dvc_remote
        
    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(f'{raw_data_path}/raw.csv')
            logging.info("mongo db dataset imported in data ingestion pipeline")
            print(df)
            logging.info("train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2)
            
            #we're using 'artifacts/data_ingestion' for storing raw, train and test datasets 
       
            
            train_data_path = os.path.join(raw_data_path,'train.csv')
            test_data_path = os.path.join(raw_data_path,'test.csv')
            dvc_remote_path = os.path.join(dvc_remote,'train.csv')
            
            #lets put the files in required directories
            train_set.to_csv(train_data_path)
            train_set.to_csv(dvc_remote_path)
            test_set.to_csv(test_data_path)
            return train_data_path, test_data_path

        except Exception as e:
            raise CustomException(e,sys)

        
if __name__ =='__main__':
    di = DataIngestion().initiate_data_ingestion()