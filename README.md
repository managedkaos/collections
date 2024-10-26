# Collections

Goal is to createa a static website that serves a web app for tracking TVs and movies.

The "collections" feature of Jekyll provides the underlying tech for the static website.

## Development Process

- Local CSV file with media name and IMDB ID; this will be the main data store
- Python (or Ruby!?) script to:
  - Read the CSV
  - Use the IMDB ID to look up the media in The Movie Database (TMDB)
  - Use the response from TMDB to create the collection files for Jekyll
  - Create the collection file in the proper location, `_movies` or `_shows`
  - Update the collection file according to the response
- Once collection files are created or upated, generate the static site

## CSV Data

### Sample

```csv
title,id,rule,status,date_added,date_completed,do_not_process
The Avengers,tt0848228,protected,watched,2012-04-25,2012-04-25,false
```

### Columns

| Name             | Definition  |
| ---------------- | ----------- |
| `title`          | The title of the movie or show |
| `id`             | the ID of the movie of show     |
| `rule`           | A rule for consuming the media; see below |
| `status`         | The status of consuming the media; see below |
| `date_added`     | the date the media was added to the database |
| `date_completed` | the date the media was consumed to completion |
| `do_not_process` | An signal for downstream processes to skip the media |
## TMDB Request

```python
import os
import requests

url = "https://api.themoviedb.org/3/find/tt0848228?external_source=imdb_id"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ["TMDB_API_KEY"]}"
}

response = requests.get(url, headers=headers)

print(response.text)
```

## TMDB Response

```json
{
 "movie_results": [
   {
     "backdrop_path": "/9BBTo63ANSmhC4e6r62OJFuK2GL.jpg",
     "id": 24428,
     "title": "The Avengers",
     "original_title": "The Avengers",
     "overview": "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!",
     "poster_path": "/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
     "media_type": "movie",
     "adult": false,
     "original_language": "en",
     "genre_ids": [
       878,
       28,
       12
     ],
     "popularity": 253.015,
     "release_date": "2012-04-25",
     "video": false,
     "vote_average": 7.7,
     "vote_count": 30618
   }
 ],
 "person_results": [],
 "tv_results": [],
 "tv_episode_results": [],
 "tv_season_results": []
}
```

## Images

- [How to build an image URL.](https://developer.themoviedb.org/docs/image-basics)

### Supported Image Sizes

```
                                  Min Res      Max Res  
poster   = Poster ............  500 x 750   2000 x 3000  
backdrop = Fanart ............ 1280 x 720   3840 x 2160  
still    = TV Show Episode ... 1280 x 720   3840 x 2160  
profile  = Actors Actresses ..  300 x 450   2000 x 3000  
logo     = TMDb Logo  
```

### API Supported Image Sizes  

```
|  poster  | backdrop |  still   | profile  |   logo   |
| :------: | :------: | :------: | :------: | :------: |
| -------- | -------- | -------- |    w45   |    w45   |
|    w92   | -------- |    w92   | -------- |    w92   |
|   w154   | -------- | -------- | -------- |   w154   |
|   w185   | -------- |   w185   |   w185   |   w185   |
| -------- |   w300   |   w300   | -------- |   w300   |
|   w342   | -------- | -------- | -------- | -------- |
|   w500   | -------- | -------- | -------- |   w500   |
| -------- | -------- | -------- |   h632   | -------- |
|   w780   |   w780   | -------- | -------- | -------- |
| -------- |  w1280   | -------- | -------- | -------- |
| original | original | original | original | original |  
```


### Examples

#### Original

_Original Size_ is the size of the uploaded image.  It can be between _Minimum Resolution_ and _Maximum Resolution_.  

- ![Original](https://image.tmdb.org/t/p/original/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg)

#### Background 

- ![w300](https://image.tmdb.org/t/p/w300/bOGkgRGdhrBYJSLpXaxhXVstddV.jpg)
- ![w780](https://image.tmdb.org/t/p/w780/bOGkgRGdhrBYJSLpXaxhXVstddV.jpg)

#### Poster

- ![w92](https://image.tmdb.org/t/p/w92/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg)  
- ![w154](https://image.tmdb.org/t/p/w154/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg)  
- ![w185](https://image.tmdb.org/t/p/w185/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg)  
- ![w342](https://image.tmdb.org/t/p/w342/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg)  
- ![w500](https://image.tmdb.org/t/p/w500/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg)  
- ![w780](https://image.tmdb.org/t/p/w780/bvYjhsbxOBwpm8xLE5BhdA3a8CZ.jpg)
