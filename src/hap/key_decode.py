import os
import base64
import json
import subprocess
from dotenv import load_dotenv



load_dotenv(".env")
BASE_64 = os.getenv('base_64')
#print(BASE_64)
class key_decode:
    def decode_key(self,base64:str):
        self.base64 = BASE_64
        decode_json = base64.b64decode(BASE_64).decode('utf-8')
        #print(decode_json)
        with open('dvc remote/api_key.json', 'w') as f:
            
            



