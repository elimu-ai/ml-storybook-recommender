import os
import pandas

ML_DATASETS_BASE_URL = 'https://raw.githubusercontent.com/elimu-ai/ml-datasets/refs/heads/main/lang-HIN'

# Read the storybooks CSV into a DataFrame, and write the DataFrame to a CSV file
storybooks_csv_url = 'https://raw.githubusercontent.com/elimu-ai/webapp-lfs/main/lang-HIN/storybooks.csv'
print(os.path.basename(__file__), 'storybooks_csv_url: {}'.format(storybooks_csv_url))
storybooks_dataframe = pandas.read_csv(storybooks_csv_url)
print(os.path.basename(__file__), 'storybooks_dataframe: \n{}'.format(storybooks_dataframe))
storybooks_dataframe.to_csv('step1_1_storybooks.csv', index=False)

# Download students.csv manifest to get list of student IDs
students_csv_url = f'{ML_DATASETS_BASE_URL}/students.csv'
print(os.path.basename(__file__), f'students_csv_url: {students_csv_url}')
students_dataframe = pandas.read_csv(students_csv_url)
print(os.path.basename(__file__), f'students_dataframe: \n{students_dataframe}')
students_dataframe.to_csv('step1_1_students.csv', index=False)

# Download each student's learning events and collect in list
storybook_learning_events_dataframes = []
for _, row in students_dataframe.iterrows():
    student_id = int(row['id'])
    student_csv_url = f'{ML_DATASETS_BASE_URL}/student-id-{student_id}/storybook-learning-events.csv'
    print(os.path.basename(__file__), f'Downloading student {student_id}: {student_csv_url}')
    try:
        student_dataframe = pandas.read_csv(student_csv_url)
        print(os.path.basename(__file__), f'  Downloaded {len(student_dataframe)} events for student-id-{student_id}')
        storybook_learning_events_dataframes.append(student_dataframe)
    except Exception as e:
        print(os.path.basename(__file__), f'  Warning: Could not download events for student-id-{student_id}: {e}')

# Concatenate all per-student DataFrames into ONE combined DataFrame
if storybook_learning_events_dataframes:
    storybook_learning_events_dataframe = pandas.concat(storybook_learning_events_dataframes, ignore_index=True)
    print(os.path.basename(__file__), f'storybook_learning_events_dataframe: \n{storybook_learning_events_dataframe}')
    storybook_learning_events_dataframe.to_csv('step1_1_storybook_learning_events.csv', index=False)
    print(os.path.basename(__file__), f'Saved combined file: step1_1_storybook_learning_events.csv ({len(storybook_learning_events_dataframe)} total events)')
else:
    print(os.path.basename(__file__), 'No student events downloaded — output file not created')
