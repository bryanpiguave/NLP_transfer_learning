# NLP_transfer_learning

The purpose of this project 
is to show NLP methods for email spam classification.

# Datasets

The datasets used in this project are the following 

1. [Enron Dataset](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset)
2. [Fraudulent Email Corpus](https://www.kaggle.com/datasets/rtatman/fraudulent-email-corpus)

The process of training and testing is formed by the following steps:

1. Extract email body and headers 
2. Tokenize 
3. Remove stop words 
4. Classify emails


# Setting up service

We initialize the service using the following command
```
uvicorn main:app --reload
```
Use the client script adding your text as prompt 
or as file
```
python3 client.py --prompt <your prompt>
```

# Author 
Bryan Piguave 