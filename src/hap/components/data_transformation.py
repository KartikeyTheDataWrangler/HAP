from sklearn.preprocessing import FunctionTransformer
from src.hap.transformer_functions import get_pulsepressure
import pandas as pd




df = pd.read_csv(r'artifacts\data_ingestion\train.csv')
df['Pulse Pressure'] = df['Blood Pressure'].apply(get_pulsepressure) 
print(df)


