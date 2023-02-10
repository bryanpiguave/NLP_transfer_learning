import pickle
import re 


# Hyperparameters
NSAMP= 1000 #Number of samples to generate in each class spam and not spam 
MAXTOKENS=50 #The maximum number of tokens per document 
MAXTOKENLEN=20 #The maximum length of each token




def tokenize(row):
    # Tokenize and remove empty rows 
    if row in [None," "]:
        tokens=""
    else:
        tokens=str(row).split(" ")[:MAXTOKENS]
    return tokens



def main():

    with open("input/bodies","rb") as fp:
        bodies = pickle.load(fp)

    return 0 



if __name__=="__main__":
    main()