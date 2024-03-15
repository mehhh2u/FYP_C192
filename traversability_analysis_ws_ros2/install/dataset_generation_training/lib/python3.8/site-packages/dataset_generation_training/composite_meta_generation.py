import os
import pandas as pd

# File with meta data
meta_folder_path_base = '/home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/csv/'
output_path = '/home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/csv/'

dataset_type = 1 # 1 for training, 2 for evaluation

# Create an empty dataframe to store concatenated data
combined_df = pd.DataFrame()

# If for training dataset
if dataset_type == 1:
    meta_folder_path = meta_folder_path_base + 'training/individual_meta_data/'
    for filename in os.listdir(meta_folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(meta_folder_path, filename)
            # Read the CSV file
            df = pd.read_csv(file_path)
            # Append it to the combined DataFrame
            combined_df = combined_df.append(df, ignore_index = True)

# If for evaluation dataset
if dataset_type == 2:
    meta_folder_path = meta_folder_path_base + 'evaluation/individual_meta_data/'
    for filename in os.listdir(meta_folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(meta_folder_path, filename)
            # Read the CSV file
            df = pd.read_csv(file_path)
            # Append it to the combined DataFrame
            combined_df = combined_df.append(df, ignore_index = True)

# Reset the ID column
combined_df['ID'] = range(0, len(combined_df))

if dataset_type == 1:
    combined_df.to_csv(os.path.join(output_path, 'meta_training_data.csv'), index=False)

if dataset_type == 2:
    combined_df.to_csv(os.path.join(output_path, 'meta_evaluation_data.csv'), index=False)