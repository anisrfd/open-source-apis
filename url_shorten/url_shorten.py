import logging
import os
import bitly_api

from url_shorten.exceptions import URLShortenFailedException

log = logging.getLogger(__name__)


class URLShorten:
    """
    URLShorten class
    """

    def __init__(self):
        """
        Sets connection and gets api key
        through environment variable.
        """
        self.req = bitly_api.Connection(os.getenv('URL_SHORTEN_API_KEY'))   # Get your API : https://dev.bitly.com/

    def get_short_url(self, url: str):
        """
        Takes url and returns the short url
        of provided url

        :param url: str object
        :return: short url or raise URLShortenFailedException
        """
        log.info("Fetching short url for url [%s]", url)
        try:
            return self.req.shorten(url)
        except Exception as e:
            log.error("Shorten api request failed due to [%s] for url [%s]", e, url)
            raise URLShortenFailedException


if __name__ == '__main__':
    url_shorten = URLShorten()
    print(url_shorten.get_short_url('https://medium.com/'))
