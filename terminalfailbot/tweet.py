import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

class Tweet:
    def __init__(self, message, config):
        self.config = config
        self.message = Tweet.parse_message(message)
        self.set_credentials()
        self.api = tweepy.API(self.auth)
    
    def set_credentials(self):
        CKEY = self.config['consumer_token']
        CSECRET = self.config['consumer_token_secret']
        AKEY = self.config['access_token']
        ASECRET = self.config['access_token_secret']

        self.auth = tweepy.OAuthHandler(CKEY, CSECRET)
        self.auth.set_access_token(AKEY, ASECRET)

    def send_message(self):
        if not self.message:
            return
        self.api.update_status(self.message)

    @staticmethod
    def parse_message(message):
        msg = message.split(';')
        # only use messages with an exit code
        if(len(msg) != 2):
            return False
        message = f'Command: {msg[0]} --- Exit code: {msg[1]}'
        if len(message) > 280:
            return
        return message