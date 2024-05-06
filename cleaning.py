import os
import re

def clean_data(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            new_filename = re.sub(r'\d*\.+(\.csv)$', r'\1', filename)
            
            if new_filename[-1].isdigit():
                new_filename = new_filename[:-1]
            
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(old_file_path, new_file_path)

folder_path = 'Data'
clean_data(folder_path)
