import requests
import time
import json

class RedditJson:

    """
    This class uses the reddit api to gather user generated
    posts for a specific subreddit. After scraping, the content is 
    stored in a json file.

    This class should be memory efficent, so it should be suitable 
    for large data gathering operations.
    """

    def __init__(self, credObject, cooldown):
        self.headers = {
        'Authorization': 'bearer ' + self.get_access_key(credObject), 
        'User-Agent': '{} by {}'.format(
            credObject['appName'], 
            credObject['appDeveloper'])
        }
        
        self.payload = {'limit': 100, 'count': 0, 'after': ''}
        self.cooldown = cooldown

    def makeRequest(self, subreddit):

        # cooldown between requests
        time.sleep(self.cooldown)
        
        response = requests.get(
            'https://oauth.reddit.com' + '/r/{}/new'.format(subreddit), 
            headers=self.headers, 
            params=self.payload)

        # update marker for pagination
        self.payload['after'] = response.json()["data"]['after'] 
        
        return response


    def beginScrape(self, path, subreddit, depth=3, logging=True):

        # checks if json file exists
        # if not, just make one
        # it's dirty, but it works
        try:
            with open(path, 'r') as file:
                file.close()

        except IOError:
            
            with open(path, 'w') as file:
                json.dump({
                    "data": [
                        {"subreddit": subreddit}
                    ]
                }, file)

        # resets payload to start pagination from first page on reddit
        self.payload = {'limit': 100, 'count': 0, 'after': ''}

        # depth for each subreddit (how many pages)
        for i in range(0, depth):

            if logging:
                print("Scraping {} - Page {}".format(subreddit, i+1))  

            # send request for new posts
            response = self.makeRequest(subreddit=subreddit)

            # extracts posts
            posts = response.json()["data"]["children"] 

            # Checking posts on page to see if eligible entry into db
            for post in posts:
                # provided info for post
                postData = post['data']
                self.appendJsonFile(path, postData)

    # appends json file without loading into memory
    def appendJsonFile(self, path, data):

        with open (path, mode="r+") as file:
        
            file.seek(0,2)
            position = file.tell() -2
            file.seek(position)
            file.write( ",{}]".format(json.dumps(data)) + "}" )

            file.close()

    # Creds to gain access to API
    def get_access_key(self, credObject):

        base_url = 'https://www.reddit.com/'

        data = {'grant_type': 'password', 
        'username': credObject['username'], 
        'password': credObject['password']}

        auth = requests.auth.HTTPBasicAuth(
            credObject['appID'], 
            credObject['appSecret'])

        r = requests.post(base_url + 'api/v1/access_token',
                      data=data,
                      headers={'user-agent': '{} by {}'.format(credObject['appName'], credObject['appDeveloper'])},
                                            # app name, developer
    		  auth=auth)
        d = r.json()

        return d['access_token']