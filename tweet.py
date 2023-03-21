import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
# Creating list to append tweet data to
tweets_list2 = []
i = 1
print("Enter the Search Query: ")
search = input()
query = search + ' lang:en'
print("Enter the number of Search Query: ")
n = input()
limit = int(n)
# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(query).get_items()):
    if i < limit:
        tweets_list2.append(
                [tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.url, tweet.user.renderedDescription,
                 tweet.user.followersCount, tweet.user.friendsCount, tweet.likeCount, tweet.retweetCount])
    else:
        break

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'url', 'description', 'followersCount', 'friendsCount', 'likeCount', 'Retweets'])
tweets_df2['Datetime'] = tweets_df2['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
dict1 = tweets_df2.to_dict(orient='index')
with open('tweet_esp.json', 'w') as fp:
    json.dump(dict1, fp, indent=4)
i = 0

with open('tweet_esp.json') as user_file:
    file_contents = user_file.read()

print(file_contents)
