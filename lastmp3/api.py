import requests

def validate_api_key(api_key):
    """Validate the Last.fm API key by making a simple test request."""
    test_url = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={api_key}&format=json&limit=1"
    
    try:
        response = requests.get(test_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            #check if the response contains an error
            if 'error' in data:
                return False, f"API Error: {data.get('message', 'Invalid API key')}"
            return True, "API key is valid"
        else:
            return False, f"HTTP Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Network error: {str(e)}"

def fetch_recent_track(username, api_key):
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={api_key}&format=json&limit=1"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            #check for API errors
            if 'error' in data:
                print(f"Last.fm API Error: {data.get('message', 'Unknown error')}")
                return None
                
            #check if user has any tracks
            if 'recenttracks' not in data or 'track' not in data['recenttracks']:
                print(f"No recent tracks found for user '{username}'")
                return None
                
            recent_track = data["recenttracks"]["track"][0]
            track_name = recent_track["name"]
            artist_name = recent_track["artist"]["#text"]
            album_name = recent_track["album"]["#text"]
            album_art_images = recent_track.get("image", [])

            album_art_url = None
            for image in album_art_images:
                if image["size"] == "extralarge":
                    album_art_url = image["#text"]
                    break
            
            x=[]
            x.append(track_name)
            x.append(artist_name)
            x.append(album_name)
            x.append(album_art_url.replace("300x300", "700x700") if album_art_url else None)
            return x
        else:
            print(f"HTTP Error {response.status_code}: Unable to fetch recent tracks")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {str(e)}")
        return None
    except Exception as e:
        print(f"Error processing response: {str(e)}")
        return None

def tracklist(artist_name, album_name, api_key):
    url = f"https://ws.audioscrobbler.com/2.0/?method=album.getInfo&artist={artist_name}&album={album_name}&api_key={api_key}&format=json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print(f"Error: {data['message']}")
            return None
        else:
            album_info = data.get("album", {})
            tracks = album_info.get("tracks", {}).get("track", [])

            tracklist = [track.get("name", "") for track in tracks]
            return tracklist
    elif response.status_code == 404:
        print(f"Album '{album_name}' by '{artist_name}' not found in Last.fm database.")
        return None