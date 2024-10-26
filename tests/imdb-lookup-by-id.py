import os
import requests

#url = "https://api.themoviedb.org/3/search/movie?query=the+avengers+marvel"
#url = "https://api.themoviedb.org/3/find/tt0848228?external_source=imdb_id"
url = "http://localhost:35445/avengers.json"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ["TMDB_API_KEY"]}"
}

response = requests.get(url, headers=headers)

print(response.text)
