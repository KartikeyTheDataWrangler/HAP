from src.hap.logger import logging
from src.hap.exception import CustomException
import os, sys
from src.hap.config.constants import *
from src.hap.utils import read_yaml_file, create_directories
from src.hap.config.config_entity import DataIngestionConfig
from src.hap.config.configeration import Configuration_Creator
import pandas as pd

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
            
            #we're using 'artifacts/data_ingestion' for storing raw, train and test datasets 
            
        except Exception as e:
            raise CustomException(e,sys)
    
    

