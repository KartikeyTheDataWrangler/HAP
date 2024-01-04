from src.hap.logger import logging
from src.hap.exception import CustomException
import yaml, sys, os
from src.hap.config.constants import *


def read_yaml_file(file_path):
    """
    Read and parse a YAML file.

    Parameters:
    - file_path (str): The path to the YAML file.

    Returns:
    - dict: A dictionary containing the parsed YAML data.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            #print(data)
            return data
    except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise CustomException(e,sys) 

    

def create_directories(path_:str):
    """
    Creates directories from path
    """
    try:
        logging.info(f"creating directories for path: {path_}")    
        os.makedirs(path_, exist_ok=True)
    except Exception as e:
        raise CustomException(e,sys) 
    
