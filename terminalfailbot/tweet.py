import tweepy
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class Tweet:
    def __init__(self, message, config):
        self.config = config
        self.message = self.parse_message(message)    

    def send_message(self):
        r = requests.post(
            'http://164.90.209.245:5000/submit', 
            json=self.message,
            headers={'Content-type': 'application/json'})

    def parse_message(self, message):
        msg = message.split(';')
        # only use messages with an exit code
        if(len(msg) != 2):
            return False

        msg = f'Command: {msg[0]} --- Exit code: {msg[1]}'
        if len(message) > 280:
            return
        message = {
            "author": self.config['author'],
            "message": msg
        }
        self.message = json.dumps(message)
        return message