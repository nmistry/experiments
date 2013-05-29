from flask import Flask, render_template
from flask.ext.pymongo import PyMongo
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'tweets'
mongo = PyMongo(app)


@app.route('/')
def home():
    return "hello"


@app.route('/tweets')
def show_tweets():
    tweets = mongo.db.tweets.find().sort('id', direction=-1).limit(100)
    return render_template('index.html', tweets=tweets)


@app.route('/tweets/user/<int:user_id>')
def show_user_tweets(user_id):
    tweets = mongo.db.tweets.find({'user.id': user_id}).sort('id', direction=-1).limit(100)
    return render_template('index.html', tweets=tweets)


@app.route('/tweets/hashtag/<hashtag>')
def show_hashtag_tweets(hashtag):
    tweets = mongo.db.tweets.find({'entities.hashtags.text': hashtag}).sort('id', direction=-1).limit(100)
    return render_template('index.html', tweets=tweets)


if __name__ == "__main__":
    app.debug = False
    app.config['SECRET_KEY'] = 'nm123'
    toolbar = DebugToolbarExtension(app)
    app.run()
