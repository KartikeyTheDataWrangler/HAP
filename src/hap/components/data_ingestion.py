from src.hap.logger import logging
from src.hap.exception import CustomException
import os, sys
from src.hap.config.constants import *
from src.hap.utils import read_yaml_file, create_directories
from src.hap.config.config_entity import DataIngestionConfig
from src.hap.config.configeration import Configuration_Creator

root_dir = Configuration_Creator().create_ingestion().root_dir
raw_data_path = Configuration_Creator().create_ingestion().root_dir


print(root_dir, raw_data_path)