import os
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm

def split_multiple_files(input_directory, train_ratio=0.8, chunk_size=50000):
    # Check directory existence and readability
    if not os.path.exists(input_directory) or not os.access(input_directory, os.R_OK):
        raise ValueError(f"Invalid or unreadable directory: {input_directory}")

    # Get list of CSV files
    csv_files = [f for f in os.listdir(input_directory) if f.lower().endswith('.csv')]
    if not csv_files:
        raise ValueError(f"No CSV files found in {input_directory}.")
    
    output_dir = os.path.join(input_directory, 'split')
    os.makedirs(output_dir, exist_ok=True)
    
    # Process files with progress bar
    with tqdm(total=len(csv_files), desc="Processing files") as pbar:
        for file in csv_files:
            file_path = os.path.join(input_directory, file)

            if os.stat(file_path).st_size == 0:
                print(f"Skipping empty file: {file}")
                pbar.update(1)
                continue
            
            try:
                # Initialize data lists
                train_data, test_data = [], []
                for chunk in pd.read_csv(file_path, chunksize=chunk_size):
                    chunk = optimize_memory(chunk)
                    train, test = train_test_split(chunk, test_size=1-train_ratio, random_state=42)
                    train_data.append(train)
                    test_data.append(test)

                # Save splits
                pd.concat(train_data).to_csv(os.path.join(output_dir, f"train_{file}"), index=False)
                pd.concat(test_data).to_csv(os.path.join(output_dir, f"test_{file}"), index=False)
                print(f"Processed {file} successfully.")
            
            except Exception as e:
                print(f"Error processing {file}: {e}")
            
            pbar.update(1)

def optimize_memory(data):
    """Convert columns to more memory-efficient types."""
    for col in data.select_dtypes(include=['float64']).columns:
        data[col] = data[col].astype('float32')
    for col in data.select_dtypes(include=['int64']).columns:
        data[col] = data[col].astype('int32')
    return data

if __name__ == "__main__":
    try:
        split_multiple_files(input_directory='/Users/nitikabahl/story recemonder/ml-storybook-recommender/step1_prepare')
    except Exception as e:
        print(f"Error: {e}")