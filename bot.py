import tweepy

API_Key= "SqPPe2l0qfHSWgy7W9iC6u5Ec"

SECRECT_KEY = "avymfjKME8VZI78WjHrocFbEjjRhh99k0d4OfMG40mum0LOmHB"

ACCESS_TOKEN = "1604591312971481088-lcBcHsWpT5OCCSDB5dqsfb0lpSLn1A"

ACCESS_SECRET = "1604591312971481088-lcBcHsWpT5OCCSDB5dqsfb0lpSLn1A"


BEAR = "AAAAAAAAAAAAAAAAAAAAAJJukgEAAAAA5Flm0Fwb0lv0Lk%2BBLf2M8tZ5pmA%3DABta5X1CopBJkrifIkOwfIsDhGG4Wkc8fUANMPjjGi97lONi8W"
consumer_key = '4ygwucH6uuoiu5XANJxXbds1n'
consumer_secret = '9EFxkrMnzUgb7BQeVMk07wOUs7XzqpfwXGPWbp9GXqjUdOXKJj'
access_token = '1604591312971481088-MC1aJ4jSdD8uauPqkVV63p3hrZC4Ia'
access_token_secret = 'n3K87lTdaRnJCajkYvHQmWArP287i7ptiPH4fJsxi6dH8'
print('d')

auth = tweepy.Client(consumer_key =consumer_key,consumer_secret=consumer_secret, bearer_token='AAAAAAAAAAAAAAAAAAAAAJJukgEAAAAA5Flm0Fwb0lv0Lk%2BBLf2M8tZ5pmA%3DABta5X1CopBJkrifIkOwfIsDhGG4Wkc8fUANMPjjGi97lONi8W')

redirect_url = auth._get_oauth_2_authenticating_user_id(access_token)

print("Please visit the following URL to complete the OAuth 2.0 authorization process:")
print(redirect_url)

# Get the verifier code from the URL
verifier_code = input("Enter the verifier code: ")

# Get the access token
auth.get_access_token(verifier_code)

# Create the API client
api = tweepy.API(auth)

# Make an API request
try:
    user = api.verify_credentials()
    print("Authentication successful! User: @" + user.screen_name)
except tweepy.TweepError as e:
    print("Authentication failed: " + str(e))

query = "ai"
date_since = "2022=02-12"
# Scrape tweets
tweets = tweepy.Cursor(api.search_tweets,
                       q=query,
                       lang='en',
                       since_id=date_since,
                       tweet_mode='extended').items(5)

# # Print tweets



# f = open("Tweetquery.txt","w")


# for tweet in tweets:
#     print(tweet.full_text)
#     f.write(tweet)

# f.close()