from sklearn.preprocessing import FunctionTransformer
from src.hap.transformer_functions import get_pulsepressure
import pandas as pd
import pickle 

df = pd.read_csv(r'artifacts\data_ingestion\train.csv')

def get_pulsepressure(df):
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
    df = df.drop(['Pressure List', 'Systolic', 'Diastolic'], axis=1,inplace=True)
    
    return df



preprocessor1 = pickle.dumps(get_pulsepressure)

with open('artifacts/models/preprocessor1', 'wb') as file:
    file.write(preprocessor1)



if __name__ == '__main__':
    with open('artifacts/models/preprocessor1', 'rb') as file:
        loaded_function = pickle.load(file)
        
    result_df = loaded_function(df)
    print(df)
    df.to_csv('asdasd.csv')