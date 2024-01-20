import os
import base64
import json
from dotenv import load_dotenv



#load_dotenv(".env")
#base_64 = os.getenv('base_64')
#BASE_64 = base_64

class key_decode:
    def decode_key(self,base64_str:str):
        decode_json = base64.b64decode(base64_str).decode('utf-8')
        dec_json = json.loads(decode_json)
        #print(dec_json)
        with open('dvc remote/api_key.json', 'w') as f:
            json.dump(dec_json,fp=f)
            
    def del_key(self):
        file_path = f'dvc remote/api_key.json'
        if os.path.exists(file_path):
            os.remove(file_path)
            print('directory deleted')
            
            
'''                 
#import time
base_64_decode = key_decode().decode_key(base64_str=BASE_64)
#time.sleep(20)
key_decode().del_key()

'''
            



