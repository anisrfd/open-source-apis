import requests
import logging

from pokemon.exceptions import PokemonFetchFailedException

log = logging.getLogger(__name__)


class Pokemon:
    """
    Pokemon class
    """

    def __init__(self):
        """
        Sets url, params and headers
        """
        self.url = "https://pokeapi.co/api/v2/pokemon/"
        self.params = {"limit": "150"}
        self.headers = {}

    def get(self):
        """
        Fetches pokemon information

        :return: json object or raise PokemonFetchFailedException
        """
        log.info("Fetching pokemon information using url [%s]", self.url)
        response = requests.request("GET", self.url, headers=self.headers, params=self.params)

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            log.error("Pokemon fetch failed due to [%s] with status code [%s]", response.text, response.status_code)
            raise PokemonFetchFailedException


if __name__ == '__main__':
    pokemon = Pokemon()
    pokemon_info = pokemon.get()
    for pokemon in pokemon_info["results"]:
        print(pokemon["name"])
