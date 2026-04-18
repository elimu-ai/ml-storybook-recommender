import os
import pandas

# Read the storybooks CSV into a DataFrame, and write the DataFrame to a CSV file
storybooks_csv_url = 'https://raw.githubusercontent.com/elimu-ai/webapp-lfs/main/lang-HIN/storybooks.csv'
print(os.path.basename(__file__), 'storybooks_csv_url: {}'.format(storybooks_csv_url))
storybooks_dataframe = pandas.read_csv(storybooks_csv_url)
print(os.path.basename(__file__), 'storybooks_dataframe: \n{}'.format(storybooks_dataframe))
storybooks_dataframe.to_csv('step1_1_storybooks.csv', index=False)

# Read the storybook learning events CSV into a DataFrame, and write the DataFrame to a CSV file
storybook_learning_events_csv_url = 'https://raw.githubusercontent.com/elimu-ai/ml-datasets/refs/heads/main/lang-HIN/storybook-learning-events.csv'
print(os.path.basename(__file__), f'storybook_learning_events_csv_url: {storybook_learning_events_csv_url}')
storybook_learning_events_dataframe = pandas.read_csv(storybook_learning_events_csv_url)
print(os.path.basename(__file__), f'storybook_learning_events_dataframe: \n{storybook_learning_events_dataframe}')
storybook_learning_events_dataframe.to_csv('step1_1_storybook_learning_events.csv', index=False)

# Extract unique android_id values and create students manifest file
unique_android_ids = storybook_learning_events_dataframe['android_id'].dropna().unique()
students_dataframe = pandas.DataFrame({'android_id': sorted(unique_android_ids)})
students_dataframe.to_csv('step1_1_students.csv', index=False)
print(os.path.basename(__file__), f'students_dataframe: \n{students_dataframe}')
print(os.path.basename(__file__), f'Created students manifest: step1_1_students.csv ({len(students_dataframe)} unique students)')
for android_id in unique_android_ids:
    student_events_dataframe = storybook_learning_events_dataframe[
        storybook_learning_events_dataframe['android_id'] == android_id
    ].copy()
    safe_android_id = str(android_id).replace('/', '_').replace('\\', '_')
    filename = f'step1_1_storybook_learning_events_{safe_android_id}.csv'
    student_events_dataframe.to_csv(filename, index=False)
    print(os.path.basename(__file__), f'Created: {filename} ({len(student_events_dataframe)} events)')
print(os.path.basename(__file__), f'Per-student organization complete! Total students: {len(unique_android_ids)}')
