import logging
import os
import requests

from exceptions.exceptions import MovieDBFailedException

log = logging.getLogger(__name__)


class MovieDatabase:
    """
    MovieDatabase class
    """

    def __init__(self):
        """
        Sets url and gets api key
        through environment variable.
        """
        self.url = 'https://api.themoviedb.org/3/list/{}?api_key={}&language=en-US'.format(
            10, os.getenv('MOVIE_DATABASE_API_KEY'))

    def get_movie(self):
        """
        Requests to movie database url and returns
        response

        :return: response or raise URLShortenFailedException
        """
        log.info("Fetching short url for url [%s]", self.url)
        res = requests.get(self.url)
        if res.status_code == requests.codes.ok:
            return res.json()
        else:
            log.error("Movie database fetching failed due to [%s] with status code [%s]", res.text,
                      res.status_code)
            raise MovieDBFailedException


if __name__ == '__main__':
    movie_db = MovieDatabase()
    print(movie_db.get_movie())
