import os
import pandas as pd
from sklearn.model_selection import train_test_split

def split_multiple_files(input_directory, train_ratio=0.8):
    # Get list of all CSV files in the directory
    csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]
    
    # Check if any CSV files were found
    if not csv_files:
        print("No CSV files found in the directory.")
        return
    
    # Iterate through all files and split them
    for file in csv_files:
        input_file = os.path.join(input_directory, file)
        
        # Load dataset
        print(f"Loading data from {input_file}...")
        data = pd.read_csv(input_file)
        
        # Check if the dataset is empty
        if data.empty:
            print(f"Warning: {file} is empty. Skipping...")
            continue
        
        # Split data
        print(f"Splitting data into {int(train_ratio*100)}% train and {int((1-train_ratio)*100)}% test sets.")
        train_data, test_data = train_test_split(data, test_size=(1 - train_ratio), random_state=42)
        
        # Save splits
        output_dir = os.path.join(input_directory, 'split')
        os.makedirs(output_dir, exist_ok=True)
        
        train_output = os.path.join(output_dir, f"train_{file}")
        test_output = os.path.join(output_dir, f"test_{file}")
        
        # Save the split datasets to CSV
        train_data.to_csv(train_output, index=False)
        test_data.to_csv(test_output, index=False)
        
        print(f"Data from {file} split and saved successfully.")

if __name__ == "__main__":
    # Example usage for splitting multiple files in a directory
    split_multiple_files(input_directory='/Users/nitikabahl/story recemonder/ml-storybook-recommender/step1_prepare/')