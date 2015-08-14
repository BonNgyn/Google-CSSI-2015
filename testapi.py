import urllib2
import json

url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=puppies"
result = urllib2.urlopen(url)

kitty = json.loads(result.read())

print kitty['data']['image_url']