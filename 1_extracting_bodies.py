import numpy as np 
import pandas as pd 
import email 
from typing import List
import pickle
import tqdm 
"""
    The purpose of this code is extract bodies from 
    spam emails and authentic emails 

"""

# Extracting data from Enron emails dataset
file_path = "input/emails.csv"
emails = pd.read_csv(file_path)
print("Succesfully loaded {} rows and {} columns".format(emails.shape[0], emails.shape[1]))
print(emails.loc[0]["message"])

def extract_messages(df:pd.DataFrame) -> List[str]:
    messages= []
    for item in df["message"]:
        e = email.message_from_string(item)
        message_body= e.get_payload()
        messages.append(message_body)
    print("Retrieved message body from emails")


bodies = extract_messages(df=emails)

with open("input/enron_bodies","wb") as fp:
    pickle.dump(obj=bodies,file=fp)

# Extracting data from fraudulent emails
