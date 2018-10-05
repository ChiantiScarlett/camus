from urllib.request import urlopen, Request, quote
import json
import settings


class NaverAPI:
    def __init__(self):
        # Initialize CLIENT, SECRET from settings
        self._CLIENT = settings.CLIENT
        self._SECRET = settings.SECRET

    def _load(self, URL, queries):
        # urlopen with appropriate headers and parameters in GET format.

        keys = list(queries.keys())
        values = list(queries.values())

        queries = []
        for i in range(len(keys)):
            queries.append("{}={}".format(quote(keys[i]), quote(values[i])))

        req = Request(URL + "?" + "&".join(queries),
                      headers={'X-Naver-Client-Id': self._CLIENT,
                               'X-Naver-Client-Secret': self._SECRET}
                      )

        json_data = json.loads(urlopen(req).read().decode('utf-8'))
        return json_data

    def load_movie(self, queries):
        url = 'https://openapi.naver.com/v1/search/movie.json'
        data = self._load(url, queries)
        return data
