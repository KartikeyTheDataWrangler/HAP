
import pandas as pd
import pickle 
import numpy as np
import os
from src.hap.config.configeration import Configuration_Creator
from src.hap.utils import save_object
from src.hap.logger import logging
import dill

raw_data_path = Configuration_Creator().create_ingestion().raw_data_path
preprocessor_dir = Configuration_Creator().create_preprocessor()
print(preprocessor_dir)

#find a better way to deals with path in next project

train_data_path = os.path.join(raw_data_path,'train.csv')
train_cleaned_data_path = os.path.join(raw_data_path,'train_cleaned.csv')
preprocssor_path = os.path.join(preprocessor_dir,'preprocessor')

df = pd.read_csv(train_data_path)
#print(df)

logging.info('Creating preprocessor 1 object')

def get_preprocessor(df):
    target = df['Heart Attack Risk'] 
    # Assuming 'Blood Pressure' is the column name in the DataFrame
    df['Blood Pressure'] = df['Blood Pressure'].apply(lambda x: str(x))  # Ensure values are converted to strings
    df['Pressure List'] = df['Blood Pressure'].str.split('/')
    
    # Extract systolic and diastolic pressures and calculate pulse pressure
    df['Systolic'] = df['Pressure List'].apply(lambda x: int(x[0]))
    df['Diastolic'] = df['Pressure List'].apply(lambda x: int(x[1]))
    df['Pulse Pressure'] = df['Systolic'] - df['Diastolic']
    
    # Categorize pulse pressure
    df['Pulse Pressure Category'] = pd.cut(df['Pulse Pressure'], bins=[-float('inf'), 40, 80, 120, float('inf')],
                                        labels=['extremely low', 'low', 'normal', 'high'], include_lowest=True)
    
    # Drop intermediate columns if needed
    df = df.drop(['Pressure List', 'Systolic', 'Diastolic','Pulse Pressure','Heart Attack Risk','Blood Pressure','Patient ID','Country','Hemisphere','Income'], axis=1)
    
    df['diabetes'] = df['Diabetes'] + df['Smoking'] + df['Obesity']
    
    df = df.drop(['Diabetes','Smoking','Obesity'],axis=1)
    
    df['Exercise Hours Per Week'] = pd.cut(df['Exercise Hours Per Week'], 
                                        bins=[0, 2, 4, 6, 8, 10, np.inf]
                                        , labels=['very low', 'low', 'medium', 'high','very high','extreme' ])
    
    df['diabetes'] = pd.cut(df['diabetes'],3,labels=['normal','prediabetes','diabetes'])
    
    df['Triglycerides'] = pd.cut(df['Triglycerides'], bins=[0,150,200,np.inf], labels=['low', 'normal', 'high'])
    
    df = df.drop(columns=['Exercise Hours Per Week','Sedentary Hours Per Day','Heart Rate','Unnamed: 0','_id'])
    
    df['Age'] = pd.cut(df['Age'], bins=[0,30,50,np.inf], labels=['young adult', 'adult', 'elderly'])
    
    df['BMI'] = pd.cut(df['BMI'], bins= [0,18,25,30,np.inf], labels=['under weight', 'healthy', 'overweight','obesity'])
    
    df = pd.concat([df,target],axis=1,join='inner')
    return df

save_object(file_path=preprocssor_path,obj=get_preprocessor)


if __name__ == '__main__':
    df_print = get_preprocessor(df=df)
    df_print.to_csv(train_cleaned_data_path)
    print(df_print.isnull().sum())

