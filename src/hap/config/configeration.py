from src.hap.config.constants import *
from src.hap.utils import read_yaml_file, create_directories
from src.hap.config.config_entity import DataIngestionConfig

class Configuration_Creator:
    def __init__(self):
        config_filepath = CONFIG_FILE_PATH
        self.config = read_yaml_file(config_filepath)
        #print(self.config)
        #create_directories(self.config['data_ingestion']['root_dir'])
    def create_ingestion(self):
        config = self.config['data_ingestion']['root_dir']
        create_directories(config)
        data_ingestion_config = DataIngestionConfig(
            root_dir=config
        )
        #print(data_ingestion_config)
        return data_ingestion_config
    
if __name__=="__main__" :
       
    config_creator = Configuration_Creator()

    ingestion = config_creator.create_ingestion().root_dir
    print(ingestion)
    

