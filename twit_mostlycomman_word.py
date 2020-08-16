'''Using Twitter API, fetch all tweets posted by a particular Twitter handle and generate a list
 of most commonly used words used by that handle.'''


from requests_oauthlib import OAuth1Session
import json


consumer_key = 'fSYabsd6mktxf7x1cxYaT3zs2'
consumer_secret = 'VwOrM23fgWPCD7GCzZv9xnmZpOis7cXJOCQnnzajv66fq8EiHe'


# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')
print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
base_authorization_url = 'https://api.twitter.com/oauth/authorize'
authorization_url = oauth.authorization_url(base_authorization_url)
print('Please go here and authorize: %s' % authorization_url)
verifier = input('Paste the PIN here: ')

print('controller reached here>>>>>>>>>>>>>>')
# # Get the access token
access_token_url = 'https://api.twitter.com/oauth/access_token'
oauth = OAuth1Session(consumer_key,
                     client_secret=consumer_secret,
                     resource_owner_key=resource_owner_key,
                     resource_owner_secret=resource_owner_secret,
                     verifier=verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)

# print('controller reached here>>>>>>>>>>>>>>')


access_token = oauth_tokens['oauth_token']
access_token_secret = oauth_tokens['oauth_token_secret']

params = {"screen_name": "CERN", 'count':'200'}


# Make the request
oauth = OAuth1Session(consumer_key,
                       client_secret=consumer_secret,
                       resource_owner_key=access_token,
                       resource_owner_secret=access_token_secret)

response = oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params = params)

# response = oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MumbaiPolice&since_id=1249248288433246210")

print("Response status: %s" % response.status_code)
# print("Body: %s" % response.text)

j_response = json.loads(response.text)
print("response>>>>>>>",j_response,)
one_twit = ''
for text in j_response:
    ans = text.get('text')
    one_twit = one_twit+ans

most = one_twit.split()


def to_upper_case(s):
    return str(s).lower()


map_iterator = list(map(to_upper_case, most))

uniq = {}
for word in map_iterator:
    if word not in uniq:
        n = 0
        for each in map_iterator:
            if word == each:
                n = n + 1
        uniq[word] = n
twitter_handler=params.get('screen_name')
print("MOSTLY COMMONLY USED WORDS BY @"+twitter_handler+" is",uniq)

Keymax = max(uniq, key=uniq.get)
print("The most used words is >>>>>>>>",Keymax)
