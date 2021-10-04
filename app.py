#/usr/bin/python3

from terminalfailbot.tweet import Tweet
from dotenv import load_dotenv
import sys, getopt
import json
import os
from pathlib import Path
from flask import Flask, request, jsonify

configpath = Path(f"{os.path.split(os.path.realpath(__file__))[0]}/config.json")
configpath = configpath.absolute()
config = None

app = Flask(__name__)
verbose_mode = True
@app.route('/submit', methods=['POST'])
def submit_message():
    content = request.json
    tweet = Tweet(content['message'], content['author'], config)
    try:
        tweet.send_message()
        return jsonify('OK', 200)
    except Exception as e:
        if verbose_mode:
            print(f'no tweet sent, forbidden \nErrors: \n{e}')
            return jsonify('OK', 200)
        else:
            return jsonify('OK', 200)
    return jsonify('OK', 200)

with open (configpath, 'r') as f:
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
   app.run('0.0.0.0')