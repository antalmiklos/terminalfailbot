#/usr/bin/python3

from terminalfailbot.tweet import Tweet
from dotenv import load_dotenv
import sys, getopt
import json
import os
from pathlib import Path

configpath = Path(f"{os.path.split(os.path.realpath(__file__))[0]}/config.json")
configpath = configpath.absolute()

with open (configpath, 'r') as f:
    config = json.loads(f.read())

def main(argv):
    opts, args = getopt.getopt(argv,"m:c",["message=", "code="])
    tweet = Tweet(' '.join(args), config)
    tweet.send_message()
        
if __name__ == "__main__":
   main(sys.argv[1:])
