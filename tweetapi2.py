import twitter



ACCESS_TOKEN = '350086556-yXyV5iuwp4WZL9GJaPYVgrG8UQjKUfgHIy8gcq9t'
ACCESS_SECRET = 'rNAPA59HQjr2J6YIi4xOGXhNWJMomBzcOgfycNBWvfGgp'
CONSUMER_KEY = 'fSYabsd6mktxf7x1cxYaT3zs2'
CONSUMER_SECRET = 'VwOrM23fgWPCD7GCzZv9xnmZpOis7cXJOCQnnzajv66fq8EiHe'

t = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=ACCESS_TOKEN,
                access_token_secret=ACCESS_SECRET)


print(">>>>>>>>>>>",t)
results = t.GetSearch(raw_query="q=from%3AGalarnykMichael&src=typd")
print(">>>>>>>>>>>",results)
