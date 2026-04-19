import os
import pandas

# Read the storybooks CSV into a DataFrame, and write the DataFrame to a CSV file
storybooks_csv_url = 'https://raw.githubusercontent.com/elimu-ai/webapp-lfs/main/lang-HIN/storybooks.csv'
print(os.path.basename(__file__), 'storybooks_csv_url: {}'.format(storybooks_csv_url))
storybooks_dataframe = pandas.read_csv(storybooks_csv_url)
print(os.path.basename(__file__), 'storybooks_dataframe: \n{}'.format(storybooks_dataframe))
storybooks_dataframe.to_csv('step1_1_storybooks.csv', index=False)

# Read the students CSV into a DataFrame to extract student IDs
students_csv_url = 'https://raw.githubusercontent.com/elimu-ai/ml-datasets/main/lang-HIN/students.csv'
print(os.path.basename(__file__), f'students_csv_url: {students_csv_url}')
try:
    students_dataframe = pandas.read_csv(students_csv_url)
except Exception as e:
    print(os.path.basename(__file__), f'Error downloading students.csv: {e}')
    students_dataframe = pandas.DataFrame()

# Loop through each student directory to download storybook-learning-events.csv
student_dfs = []
if not students_dataframe.empty and 'id' in students_dataframe.columns:
    for index, row in students_dataframe.iterrows():
        student_id = row['id']
        student_events_csv_url = f'https://raw.githubusercontent.com/elimu-ai/ml-datasets/main/lang-HIN/student-id-{student_id}/storybook-learning-events.csv'
        
        try:
            # We skip corrupt or empty files by catching exceptions and warning
            student_df = pandas.read_csv(student_events_csv_url)
            if not student_df.empty:
                student_dfs.append(student_df)
                print(os.path.basename(__file__), f'Successfully downloaded data for student {student_id} (rows: {len(student_df)})')
            else:
                print(os.path.basename(__file__), f'Data for student {student_id} is empty. Skipping.')
        except Exception as e:
            # This handles missing files gracefully (e.g., 404 Not Found)
            print(os.path.basename(__file__), f'Could not download data for student {student_id}. Skipping. Error: {e}')

# Concatenate all student data into a single pandas DataFrame
if student_dfs:
    storybook_learning_events_dataframe = pandas.concat(student_dfs, ignore_index=True)
else:
    print(os.path.basename(__file__), 'No student data could be downloaded. Creating empty DataFrame.')
    storybook_learning_events_dataframe = pandas.DataFrame()

print(os.path.basename(__file__), f'storybook_learning_events_dataframe: \n{storybook_learning_events_dataframe}')
storybook_learning_events_dataframe.to_csv('step1_1_storybook_learning_events.csv', index=False)
