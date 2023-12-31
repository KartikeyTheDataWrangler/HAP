from src.hap.config.constants import *
from src.hap.utils import read_yaml_file, create_directories
from src.hap.config.config_entity import DataIngestionConfig
from src.hap.logger import logging

class Configuration_Creator:
    logging.info("Creating Configeration Creator")    
    def __init__(self):
        config_filepath = CONFIG_FILE_PATH
        self.config = read_yaml_file(config_filepath)
        #print(self.config)
        #create_directories(self.config['data_ingestion']['root_dir'])
    def create_ingestion(self):
        root_dir_ = self.config['data_ingestion']['root_dir']
        raw_data_path_ = self.config['data_ingestion']['raw_data_path']
        create_directories(root_dir_)
        data_ingestion_config = DataIngestionConfig(
            root_dir=root_dir_,
            raw_data_path= raw_data_path_
        )
        #print(data_ingestion_config)
        return data_ingestion_config
    
    def create_remote(self):
        remote_dir_  = self.config['dvc_remote']['remote_dir']
        create_directories(remote_dir_)
    
        #print(remote_dir_)
        return remote_dir_
    
    def create_preprocessor(self):
        preprocessordir_ = self.config['preprocessor']['preprocessor_dir']
        create_directories(preprocessordir_)
        
        return preprocessordir_
    
if __name__=="__main__" :
       
    config_creator = Configuration_Creator()

    ingestion = config_creator.create_ingestion().root_dir
    remote = config_creator.create_remote()
    print(remote)
 
    

