import requests

from constants import URL, TOKEN
from utils import fetch, get_all_from_table

DB = 'D:/task/chinook.db'
COMPOSER = 'COMPOSER'
url = '{URL}/task_3'.format(URL=URL)


def task_4(*genre):

    genres_data = get_all_from_table(DB, 'genres')
    tracks_data = get_all_from_table(DB, 'tracks')
    albums_data = get_all_from_table(DB, 'albums')
    artists_data = get_all_from_table(DB, 'artists')
    media_types_data = get_all_from_table(DB, 'media_types')

    search_genres_ids = []

    for genre_data in genres_data:
        genre_id = genre_data[0]
        genre_name = genre_data[1]
        if genre_name in genre:
            search_genres_ids.append(genre_id)

    media_types_names = {}

    for media_type_data in media_types_data:
        media_type_id = media_type_data[0]
        media_type_name = media_type_data[1]
        media_types_names[media_type_id] = media_type_name

    artists_id_name = {}

    for artist in artists_data:
        artist_id = artist[0]
        artist_name = artist[1]
        artists_id_name[artist_id] = artist_name

    albums_id_title = {}

    for album_data in albums_data:
        album_id = album_data[0]
        artist_id = album_data[2]
        album_name = album_data[1]
        albums_id_title[album_id] = album_name, artist_id

    result = {}

    for track_data in tracks_data:
        genre_id = track_data[4]
        if genre_id not in search_genres_ids:
            continue
        track_duration = track_data[6]
        if track_duration // 1000 // 60 >= 5:
            continue
        track_duration_result = '{min}:{sec:02d}.{sss:03d}'.format(
            min=track_duration // 1000 // 60,
            sec=track_duration // 1000 % 60,
            sss=track_duration % 1000
        )
        album_id = track_data[2]
        album_title = albums_id_title[album_id][0]
        artist_id = albums_id_title[album_id][1]
        artist_name = artists_id_name[artist_id]
        media_type_id = track_data[3]
        media_type_name = media_types_names[media_type_id]
        track_id = track_data[0]
        track_name = track_data[1]
        composer = track_data[5]

        if not composer:
            composer = COMPOSER

        if artist_id not in result:
            result[artist_id] = {
                'artist_name': artist_name,
                'albums': {
                }
            }
        albums = result[artist_id]['albums']
        if album_id not in albums:
            albums[album_id] = {
                'title': album_title,
                'tracks': {
                }
            }
        tracks = albums[album_id]['tracks']
        if track_id not in tracks:
            tracks[track_id] = {
                'name': track_name,
                'media_type': media_type_name,
                'composer': composer,
                'duration': track_duration_result
            }

    response = requests.post(
        url=url,
        json={
            'token': TOKEN,
            'music': result,
        }
    )
    if response.status_code // 100 != 2:
        raise ConnectionError(f'Неудачный запрос. Полученный ответ: {response.text}')

    print(response.text)
