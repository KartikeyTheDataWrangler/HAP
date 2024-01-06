import pandas as pd
import pickle
import os
from src.hap.config.configeration import Configuration_Creator
from src.hap.utils import read_object  # Assuming you have read_object implemented

if __name__ == '__main__':
    # Define paths
    raw_data_path = Configuration_Creator().create_ingestion().raw_data_path
    preprocessor_dir = Configuration_Creator().create_preprocessor()
    preprocessor_path = os.path.join(preprocessor_dir, 'preprocessor.pkl')
    train_data_path = os.path.join(raw_data_path, 'train.csv')

    # Read the DataFrame
    df = pd.read_csv(train_data_path)
    print(df)

    try:
        # Load the preprocessor instance
        loaded_preprocessor = read_object(preprocessor_path)

        # Apply the preprocessor method on the DataFrame
        result_df = loaded_preprocessor.get_preprocessor(df)
        print(result_df)

    except Exception as e:
        print(f"Error loading or applying preprocessor: {e}")

