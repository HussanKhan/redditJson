# RedditJson

redditJson is a small package meant to gather large amounts of data from the Reddit API. The package does this by making a json file and appending to that json file without increasing memory footprint.

The package allows any developer or data scientist to gathers multiple GB worth of data on a machine with only 8gb of memory.

I created this package because I was running into memory limitations on my MacBook Air while gathering user generated post data from r/wallstreetbets.

I hope this simple package helps you in your future projects!

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install redditJson.

```bash
pip3 install redditJson
```

## Usage

```python
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

```

## Example of Output JSON file

Please note that the first entry is always the subreddit that is currently being scraped. If you change the subreddit, but keep the same output file name, then another entry will be appended to the json in {subreddit: subredditName} format.

```json
{
  "data": [
    {
      "subreddit": "wallstreetbets"
    },
    {
      "content": "Individual Post data from api"
    }
  ]
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)