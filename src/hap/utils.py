from src.hap.logger import logging
from src.hap.exception import CustomException
import yaml, sys



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
            print(data)
            return data
    except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise CustomException(e,sys) 

read_yaml_file('config\config.yml')       