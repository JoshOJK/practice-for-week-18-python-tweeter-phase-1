# !!START
from flask import Flask, render_template
from .config import Config
from .tweets import tweets

import random

app = Flask(__name__)

app.config.from_object(Config)
# !!END

@app.route('/')
def home():
    tweet = random.choice(tweets)
    return render_template('index.html', tweet=tweet)

# app.route('/feed')
# def feed():
