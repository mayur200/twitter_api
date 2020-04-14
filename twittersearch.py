'''
Using Twitter API, fetch all tweets based on a search keyword
Here I am getting all tweets related to Shree Ram

Helped API Doc:
https://developer.twitter.com/en/docs/labs/tweets-and-users/quick-start/get-tweets
https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
'''



#access token = "Jt350086556-OHeT0fMKHeVSknIyMZNpXlDEFQGLj149Yiazia"
#access token secret = "eWFjDcwDsfV7I4iYvhnG8ozgi7VHDM8vcXsovYJprRchj"

import os
from requests_oauthlib import OAuth1Session
import json

#changed key
consumer_key = '73RnbvXa91OYTikJFDPokYJgn'
consumer_secret = 'kH1MnK4bcN8aExdXHwX1uSmG45tNUQaaJLrVmjSMq26q2crF5n'


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



# Make the request
oauth = OAuth1Session(consumer_key,
                       client_secret=consumer_secret,
                       resource_owner_key=access_token,
                       resource_owner_secret=access_token_secret)

search_by = "Shree Ram"
search_by.replace(" ","%20")
result_type = "recent"

response = oauth.get(" https://api.twitter.com/1.1/search/tweets.json?q="+search_by+"&result_type="+result_type)

print("Response status: %s" % response.status_code)
# print("Body: %s" % response.text)

j_response = json.loads(response.text)
# print("response>>>>>>>",j_response,)
statuses = j_response.get('statuses')
for text in statuses:
    ans = text.get('text')
    print(ans)

