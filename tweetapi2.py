import twitter



ACCESS_TOKEN = '350086556-OHeT0fMKHeVSknIyMZNpXlDEFQGLj149YiaziaJt'
ACCESS_SECRET = 'FjDcwDsfV7I4iYvhnG8ozgi7VHDM8vcXsovYJprRchjeW'
CONSUMER_KEY = 'RnbvXa91OYTikJFDPokYJgn73'
CONSUMER_SECRET = '1MnK4bcN8aExdXHwX1uSmG45tNUQaaJLrVmjSMq26q2crF5nkH'

t = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=ACCESS_TOKEN,
                access_token_secret=ACCESS_SECRET)


print(">>>>>>>>>>>",t)
results = t.GetSearch(raw_query="q=from%3AGalarnykMichael&src=typd")
print(">>>>>>>>>>>",results)
