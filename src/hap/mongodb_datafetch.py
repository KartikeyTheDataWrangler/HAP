import os
import sys
from src.hap.exception import CustomException
from src.hap.logger import logging
import pandas as pd
from pymongo.mongo_client import MongoClient
from src.hap.config.constants import *
from src.hap.utils import create_directories,read_yaml_file
from dotenv import load_dotenv

def fetch_mongo(filepath):
    try: 
        logging.info("Reading data from MongoDB")
        load_dotenv('.env')
        PASSWORD = os.getenv("password")
       
        uri = f"mongodb+srv://for9cloud9deployment:{PASSWORD}@cluster0.m8xajrt.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri)
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        logging.info("Pinged your deployment. You successfully connected to MongoDB!")

        db = client['HDP2']
        curs = db.hdp2
        #necessary to conver document to list
        all_doc = curs.find()
        #print(all_doc)
        
        df = pd.DataFrame(all_doc)
        df.to_csv(f'{filepath}/raw.csv')
        logging.info(f'pushed files from mongodb to directory:{filepath}')
        return df
    
    except Exception as e:
        raise CustomException(e,sys)
'''
mongopath = read_yaml_file(CONFIG_FILE_PATH)
mongopath_ = mongopath['data_ingestion']['raw_data_path']
create_directories(mongopath_)
mongopath2 = mongopath['dvc_remote']['remote_dir']
create_directories(mongopath2)
fetch_mongo(mongopath_)
fetch_mongo(mongopath2)
        '''