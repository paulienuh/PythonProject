import tweepy
import os

auth = tweepy.OAuthHandler('J3reOjPoernyyX0BbebUhIUxE', 'LkpRlOobwykFthDhgif1kSAoPA39FVDqpyyBYCTg2mk7YJ0T9e')
auth.set_access_token('230185453-gaHgYdEK1DCeHkx2Ble0QrdCiWxCOxgrQfXvyLWN', 'YG7RCMeuuA9smUzvYfjKFJHcLqpZqpPSMZwC8BKKFs6zP')

api = tweepy.API(auth)

public_tweets = api.search(
    q = "#shefcodefirst"

)


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', tweets=public_tweets)


if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
