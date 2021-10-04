#/usr/bin/python3

from terminalfailbot.tweet import Tweet
from dotenv import load_dotenv
import sys, getopt
import json
import os

config = None

with open (os.path.abspath('repos/terminalfailbot/config.json'), 'r') as f:
    config = json.loads(f.read())

verbose_mode = bool(config['verbose_mode'])

def main(argv):
    opts, args = getopt.getopt(argv,"m:c",["message=", "code="])
    tweet = Tweet(' '.join(args), config)
    try:
        tweet.send_message()
    except Exception as e:
        if verbose_mode:
            print(f'no tweet sent, forbidden \nErrors: \n{e}')
        else:
            exit
        
if __name__ == "__main__":
   main(sys.argv[1:])
