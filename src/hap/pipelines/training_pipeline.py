#importing modules 

from src.hap.logger import logging
#from src.hap.exception import CustomException
import os, sys
from src.hap.config.constants import *
from src.hap.config.configeration import Configuration_Creator
import pandas as pd
#from sklearn.model_selection import train_test_split
from src.hap.utils import save_object, read_object
import subprocess
from dotenv import load_dotenv

#importing paths

root_dir = Configuration_Creator().create_ingestion().root_dir
raw_data_path = Configuration_Creator().create_ingestion().raw_data_path
dvc_remote = Configuration_Creator().create_remote()
preprocessor_dir = Configuration_Creator().create_preprocessor()

train_data_csv = os.path.join(raw_data_path,'train.csv')
train_cleaned_data_csv = os.path.join(raw_data_path,'train_cleaned.csv')
preprocssor_path = os.path.join(preprocessor_dir,'preprocessor')
transformer_path = os.path.join(preprocessor_dir, 'transformer')


#importing scripts

from src.hap.mongodb_datafetch import fetch_mongo

logging.info(">>>STAGE 01 - FETCHING FILES FROM CLOUD<<<<<")
fetch_mongo(filepath=raw_data_path)
fetch_mongo(filepath=dvc_remote)

logging.info(">>>STAGE 02 - DATA INGESTION<<<<<")

from src.hap.components.data_ingestion import DataIngestion

Data_Ingestion = DataIngestion().initiate_data_ingestion()

logging.info(">>> STAGE 03 - DATA PREPROCESSING <<<<<")

from src.hap.components.data_preprocessing import get_preprocessor

preprocessor = get_preprocessor(df=pd.read_csv(train_data_csv,index_col=False))
preprocessor.to_csv(train_cleaned_data_csv,index=False)
save_object(file_path=preprocssor_path,obj=get_preprocessor)

logging.info(">>> STAGE 04 - DATA TRANSFORMATION <<<<<")

from src.hap.components.data_transformation import DataTransformationConfig

transformer = DataTransformationConfig()

transformer.DataTransformer(transformer_path=transformer_path, clean_df_path=pd.read_csv(train_cleaned_data_csv,index_col=False))

logging.info(">>> STAGE 05 MODEL TRAINING  <<<<<")

from src.hap.components.model_tranier import mlflow_model_trainer

transformer = read_object(transformer_path)
transformed_df = transformer.fit_transform(pd.read_csv(train_cleaned_data_csv))
model_trainer = mlflow_model_trainer(transformed_df_train=transformed_df)

logging.info(">>> STAGE 06 DVC-GDRIVE  <<<<<")

from src.hap.key_decode import key_decode

load_dotenv(".env")
base_64 = os.getenv('base_64')
BASE_64 = base_64

root = os.getcwd()
print(root)
key_creator = key_decode().decode_key(base64_str=BASE_64)
directory = 'dvc remote'

os.chdir(directory)

subprocess.run("dvc add train.csv raw.csv", shell=True)
subprocess.run("dvc push", shell=True)

logging.info("files pushed to gdrive remote")
os.chdir(root)
key_decode().del_key()


    