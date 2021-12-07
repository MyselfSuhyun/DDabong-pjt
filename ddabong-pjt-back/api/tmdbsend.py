import requests
from .tmdb import TMDBHelper

def TMDBsend(title):
    tmdb = TMDBHelper('4775dca612e07fb742a5fcdc1532178e')
    tmdb_id = tmdb.get_movie_id(title)
    print(tmdb_id)
    if not tmdb_id:
        return tmdb_id
    result_list = []
    for i in range(len(tmdb_id)):
        inform_url = tmdb.get_movie_inform(tmdb_id[i])
        # print(inform_url)
        movie_data = requests.get(inform_url).json()
        # print(movie_data)
        a = str(movie_data.get('poster_path'))
        result_list.append({'title':movie_data.get('title'),'overview':movie_data.get('overview'),'poster_path':f'https://image.tmdb.org/t/p/w500/{a}','vote_average':movie_data.get('vote_average')})
    print(result_list)
    return result_list

