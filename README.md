# ml-storybooks-recommender

Machine learning model which predicts the rating of unread storybooks based on the student's previously read storybooks.

One model will be trained per language.


## 1. Prepare the Data

To prepare the data, follow these steps:
  * Open `prepare_data.py` and select environment and language.
  * Go to the website corresponding to the chosen environment and language, e.g. http://eng.test.elimu.ai.
  * Download `storybooks.csv` from http://eng.test.elimu.ai/content/storybook/list.
  * Download `storybook-learning-events.csv` from http://eng.test.elimu.ai/analytics/storybook-learning-event/list.
  * Add the two datasets to `RAW_DATA_DIR`.
  * Execute the script: `python prepare_data.py`


## 2. Train the Model

TODO


## 3. Make Predictions on New Samples

TODO
