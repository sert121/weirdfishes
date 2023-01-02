import os
import pylast
import requests
# read os variables

# lastFM API key
LASTFM_API_KEY = os.environ.get("LASTFM_API_KEY")
# lastFM API secret
LASTFM_API_SECRET = os.environ.get("LASTFM_API_SECRET")
    headers = {
        'user-agent': 'WeirdFishes'
    }

# artist related functions
def get_similiar_artists():
    payload = {
        'api_key': LASTFM_API_KEY,
        'method': 'artist.getsimilar',
        'format': 'json',

    }


def get_corrected_artists(artist):

    payload = {
        'api_key': LASTFM_API_KEY,
        'method': 'artist.getcorrection',
        'format': 'json',
        'artist': artist
    }
    r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)


# track related functions

def get_similiar_tracks(track):
    payload = {
        'api_key': LASTFM_API_KEY,
        'method': 'track.getsimilar',

        'format': 'json',
    }


def search_tracks(track):
    payload = {
        'api_key': LASTFM_API_KEY,
        'method': 'track.search',
        'track': 'track',
        'format': 'json',

    }
    r = requests.get('https://ws.audioscrobbler.com/2.0/', headers = headers, params=payload).json()
    data = r['results']['trackmatches']['track'][:5]
    formatted_data = data.copy()
    for i in range(len(data)):
     formatted_data[i] =  {
        'track': data[i]['name'],
        'artist': data[i]['artist'],
        'image_url': data[i]['image'][0]['#text']
    }