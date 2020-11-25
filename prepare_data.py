# This Python script prepares the following two datasets:
#   1. Storybooks
#   2. Storybook learning events

import pandas as pd

# Select environment (TEST/PROD)
ENVIRONMENT = "TEST"

# Select language
# See https://github.com/elimu-ai/model/blob/master/src/main/java/ai/elimu/model/enums/Language.java
LANGUAGE = "ENG"

RAW_DATA_DIR = "./env-" + ENVIRONMENT + "/lang-" + LANGUAGE + "/data"
print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")

# Load the storybooks
storybooks_pd = pd.read_csv(RAW_DATA_DIR + "/storybooks.csv")
print(f"storybooks_pd: \n{storybooks_pd}")

# Load the storybook learning events
learning_events_pd = pd.read_csv(RAW_DATA_DIR + "/storybook-learning-events.csv")
print(f"learning_events_pd: \n{learning_events_pd}")

# Clean the data
# TODO
