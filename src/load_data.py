import kagglehub
import os
import shutil

def load_data():

    existe_df = os.path.exists("data/raw/DataScience_salaries_2025.csv")

    if(not existe_df):

        # Download latest version
        path = kagglehub.dataset_download("saurabhbadole/latest-data-science-job-salaries-2024")

        # Copy to data
        existe_df = os.path.exists("data/raw/DataScience_salaries_2025.csv")
        shutil.copy(f"{path}/DataScience_salaries_2025.csv", "data/raw/DataScience_salaries_2025.csv")
