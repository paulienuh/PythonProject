import tweepy


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



if __name__ == '__main__':
  app.run(debug=True)

