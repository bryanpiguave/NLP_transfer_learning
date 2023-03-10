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

with open("input/fraudulent_emails.txt") as fp:
    fp = fp.read()

fraud_emails=fp.split("From r")
print("Successfully loaded {} spam emails".format(len(fraud_emails)))

fraud_emails = pd.DataFrame(fraud_emails,columns=["message"],   dtype=str)
fraud_emails = extract_messages(df=fraud_emails)

with open("input/fraud_emails","wb") as fp:
    pickle.dump(obj=fraud_emails,file=fp)
