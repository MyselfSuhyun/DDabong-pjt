import requests

class TMDBHelper:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_request_url(self, method='/movie/popular', **kwargs):

        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url
    

    def get_movie_id(self, title):
        request_url = self.get_request_url('/search/movie', query=title, region='KR', language='ko')
        # print(request_url)
        data = requests.get(request_url).json()
        results = data.get('results')
        len_re = len(results)
        result_list = [0]*len_re
        # print(len(results))
        if len_re:
            for i in range(len_re):
                result_list[i] = results[i]['id']
            return result_list
        else:
            return None

    def get_movie_inform(self,id):
        result_url = 'https://api.themoviedb.org/3/movie/'
        result_url +=f'{id}?api_key={self.api_key}&language=ko-KR'
        return result_url
