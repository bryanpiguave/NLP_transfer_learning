from ast import arg
import requests
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-p","--prompt", type=str)
parser.add_argument("-t","--text-file",type=str)
args= parser.parse_args()

def main():
    if isinstance(args.prompt, str): 
        url = "http://localhost:8000/classify?prompt=" + args.prompt
    response = requests.get(url)
    print(response.json())
    return 0

if __name__=="__main__":
    main()

