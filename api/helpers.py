import requests

#Fixes weird issue with requests pending forever due to IPV4/6 issues without slow timeout hack
requests.packages.urllib3.util.connection.HAS_IPV6 = False

def getAPIRequest(tag):
    api_url = f"https://api.hatchways.io/assessment/blog/posts?tag={tag}"
    response = requests.get(api_url)
    return response.json()['posts']

def queryTags(tags):
    posts = []
    duplicate = []
    for tag in tags:
        for item in getAPIRequest(tag):
            if int(item['id']) not in duplicate:
                posts.append(item)
                duplicate.append(int(item['id']))
    return posts
