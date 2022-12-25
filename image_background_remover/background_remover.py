import logging
import os
import requests

from exceptions.exceptions import ImageBackgroundRemoveFailedException

log = logging.getLogger(__name__)


class BackgroundRemover:
    """
    BackgroundRemover class
    """

    def __init__(self):
        """
        Sets API URL and headers, get api key
        through environment variable.
        """
        self.url = 'https://api.remove.bg/v1.0/removebg'
        self.headers = {'X-Api-Key': os.getenv('BACKGROUND_REMOVE_API_KEY')}  # Get Your API Key: https://www.remove.bg/tools-api

    def remove_image_background_using_file_path(self, image_path: str):
        """
        Takes image_path and remove image
        background of providing image.
        Saves the image which background is removed.

        :param image_path: str object
        """
        res = requests.post(self.url, files={'image_file': open(image_path, 'rb')}, data={'size': 'auto'},
                            headers=self.headers)
        if res.status_code == requests.codes.ok:
            with open('no_background_using_file.jpg', 'wb') as out:
                out.write(res.content)
        else:
            log.error("Image background remover failed due to [%s] with status code [%s]", res.text, res.status_code)
            raise ImageBackgroundRemoveFailedException

    def remove_image_background_using_url_path(self, url_path: str):
        """
        Takes url_path and remove image
        background of providing image.
        Saves the image which background is removed.

        :param url_path: str object
        """
        res = requests.post(self.url,  data={'image_url': url_path, 'size': 'auto'},
                            headers=self.headers)
        if res.status_code == requests.codes.ok:
            with open('no_background_using_url.jpg', 'wb') as out:
                out.write(res.content)
        else:
            log.error("Image background remover failed due to [%s] with status code [%s]", res.text, res.status_code)
            raise ImageBackgroundRemoveFailedException


if __name__ == '__main__':
    bg_remover = BackgroundRemover()
    bg_remover.remove_image_background_using_file_path('PROVIDE_LOCAL_IMAGE_FILE_PATH')
    bg_remover.remove_image_background_using_url_path('PROVIDE_IMAGE_FILE_URL')
