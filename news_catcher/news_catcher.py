import requests
import logging
import os

from exceptions.exceptions import NewsCatcherFailedException

log = logging.getLogger(__name__)


class NewsCatcher:
    """
    NewsCatcher class
    """

    def __init__(self):
        """
        Sets headers, get api key
        through environment variable.
        """
        self.headers = {'X-Api-Key': os.getenv('NEWS_CATCHER_API_KEY')}  # Get your API : https://newscatcherapi.com/

    def get_news(self, query: str = "Google", country: str = 'US', payload: dict = {}):
        """
        Takes query, country and payload to
        get news

        :param query: str object
        :param country: str object
        :param payload: dict object
        :return: str object or raise NewsCatcherFailedException
        """
        response = requests.get(f"https://api.newscatcherapi.com/v2/search?q=\"{query}\"&lang=en&countries={country}",
                                headers=self.headers, data=payload)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            log.error("News catcher failed due to [%s] with status code [%s]", response.text, response.status_code)
            raise NewsCatcherFailedException


if __name__ == '__main__':
    news_catcher = NewsCatcher()
    print(news_catcher.get_news())
