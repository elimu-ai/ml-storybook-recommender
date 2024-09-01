import os
import pandas

# Read the storybooks CSV into a DataFrame, and write the DataFrame to a CSV file
storybooks_csv_url = ('https://raw.githubusercontent.com/elimu-ai/webapp/main/src/main/resources/db/content_PROD/hin/storybooks.csv')
print(os.path.basename(__file__), 'storybooks_csv_url: {}'.format(storybooks_csv_url))
storybooks_dataframe = pandas.read_csv(storybooks_csv_url)
print(os.path.basename(__file__), 'storybooks_dataframe: \n{}'.format(storybooks_dataframe))
storybooks_dataframe.to_csv('step1_1_storybooks.csv', index=False)

# Read the storybook learning events CSV into a DataFrame, and write the DataFrame to a CSV file
storybook_learning_events_csv_url = ('https://raw.githubusercontent.com/elimu-ai/webapp/main/src/main/resources/db/analytics_PROD/hin/storybook-learning-events.csv')
print(os.path.basename(__file__), f'storybook_learning_events_csv_url: {storybook_learning_events_csv_url}')
storybook_learning_events_dataframe = pandas.read_csv(storybook_learning_events_csv_url)
print(os.path.basename(__file__), f'storybook_learning_events_dataframe: \n{storybook_learning_events_dataframe}')
storybook_learning_events_dataframe.to_csv('step1_1_storybook_learning_events.csv', index=False)
