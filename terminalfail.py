#/usr/bin/python3
import tweepy
import os
from dotenv import load_dotenv
import sys, getopt

load_dotenv()                

verbose_mode = False

class Tweet:
    CKEY = os.getenv('CKEY')
    CSECRET = os.getenv('CSECRET')
    AKEY = os.getenv('AKEY')
    ASECRET = os.getenv('ASECRET')
    def __init__(self, message):
        self.message = message
        self.auth = tweepy.OAuthHandler(self.CKEY, self.CSECRET)
        self.auth.set_access_token(self.AKEY, self.ASECRET)
        self.api = tweepy.API(self.auth)
    
    def send_message(self):
        if(len(self.message) == 0):
            return
        self.api.update_status(self.message)

def main(argv):
    opts, args = getopt.getopt(argv,"m:c",["message=", "code="])
    twitter = Tweet(' '.join(args))
    try:
        twitter.send_message()
    except Exception as e:
        if verbose_mode:
            print(f'no tweet sent, forbidden \nErrors: \n{e}')
        else:
            exit
        
if __name__ == "__main__":
   main(sys.argv[1:])
