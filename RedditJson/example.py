from redditJson import RedditJson

# creds for reddit api
# get from https://www.reddit.com/wiki/api
credentials = {
    "appName": "XXXX",
    "appID": "XXXX",
    "appSecret": "XXXX",
    "appDeveloper": "XXXX",
    "username": "XXXX",
    "password": "XXXX"
}

# in seconds
cooldown = 5

# init
scraper = RedditJson(credentials, cooldown)

# begin scrape
scraper.beginScrape(
    path="./example.json", # what the file will be called, must include .json
    subreddit='wallstreetbets', # no /r needed, just type in subreddit name
    depth=1, # starts scrape using new sort (newest to oldest posts), goes x pages deep
    logging=True # prints what page it's on
)
