import os
import hashlib
import hmac
import pandas


def generate_pseudonym(identifier: str, salt: str) -> str:
    """Generate a deterministic pseudonym using HMAC-SHA256."""
    return hmac.new(
        salt.encode('utf-8'),
        identifier.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()[:16]


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

# Get salt from environment variable (required for pseudonymization)
pseudo_salt = os.getenv('PSEUDO_SALT')
if not pseudo_salt:
    raise ValueError(
        "Environment variable PSEUDO_SALT is required for pseudonymization. "
        "Please set it before running this script."
    )

# Extract unique android_id values and generate pseudonyms
unique_android_ids = storybook_learning_events_dataframe['android_id'].dropna().unique()
pseudonyms = [generate_pseudonym(str(aid), pseudo_salt) for aid in unique_android_ids]
students_dataframe = pandas.DataFrame({'pseudonym': sorted(pseudonyms)})
students_dataframe.to_csv('step1_1_students.csv', index=False)
print(os.path.basename(__file__), f'students_dataframe: \n{students_dataframe}')
print(os.path.basename(__file__), f'Created students manifest: step1_1_students.csv ({len(students_dataframe)} unique students)')

# Generate per-student learning event files using pseudonyms in filenames
for android_id, pseudonym in zip(unique_android_ids, pseudonyms):
    student_events_dataframe = storybook_learning_events_dataframe[
        storybook_learning_events_dataframe['android_id'] == android_id
    ].copy()
    filename = f'step1_1_storybook_learning_events_{pseudonym}.csv'
    student_events_dataframe.to_csv(filename, index=False)
    print(os.path.basename(__file__), f'Created: {filename} ({len(student_events_dataframe)} events)')

print(os.path.basename(__file__), f'Per-student organization complete! Total students: {len(unique_android_ids)}')
