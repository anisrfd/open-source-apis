# open-source-apis
Open source APIs to automate task. Those Api's are totally free to use any daily file task depending on necessity.

## Environment Setup:

### Installation instructions

_Run the commands in a terminal or command-prompt.

- Install `Python 3.6 or >3.6` for your operating system, if it does not already exist.

 - For [Mac](https://www.python.org/ftp/python/3.6.8/python-3.6.8-macosx10.9.pkg)

 - For [Windows](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe)

 - For Ubuntu/Debian

 ```bash
 sudo apt-get install python3.6
 ```

 Check if the correct version of Python (3.6) is installed.

 ```bash
 python --version
 ```

**Make sure your terminal is at the root of the project i.e. where 'README.md' is located.**

* Get `virtualenv`.

 ```bash
 pip install virtualenv
 ```

* Create a virtual environment named `.env` using python `3.6` and activate the environment.

 ```bash
 # command for gnu/linux systems
 virtualenv -p $(which python3.6) .env

 source .env/bin/activate
 ```
* If any error occurs to install a virtual environment you can see this [link](https://github.com/anisrfd/Python-Virtualenv-Setup/blob/master/Python_virtualenv_setup.md)

 
* Install python dependencies from requirements.txt.
 ```bash
  pip install -r requirements.txt
  ```

## Image Background Remover
To use the image background remover you have to get the API key from 'https://www.remove.bg/tools-api'. To use the remover 
need to export the API key using 'BACKGROUND_REMOVE_API_KEY' name. You can use local image path or image URL. You 
need to provide the image path in the main method.

## News Catcher
To use the news catcher you have to get the API key from 'https://newscatcherapi.com/'. To use it need to export the API key 
using 'NEWS_CATCHER_API_KEY' name. You can provide query, country and payload to filter the news.

## Pokemon
To use the pokemon api you need to use 'https://pokeapi.co/api/v2/pokemon/'. Using this api you will get pokemon information.

## URL Shorten
To use the url shorten you have to get the API key from 'https://dev.bitly.com/'. To use it need to export the API key 
using 'URL_SHORTEN_API_KEY' name. Now call 'get_short_url' method by providing the url you want to short.

## Movie Database
To use the movie database you have to get the API key from 'https://www.themoviedb.org/documentation/api'. To use it need to export the API key 
using 'MOVIE_DATABASE_API_KEY' name. Now call 'get_movie' to get the movie information.

## Food Recipe
To use the food recipe api you have to get the API key from 'https://spoonacular.com/'. To use it need to export the API key 
using 'FOOD_RECIPE_API_KEY' name. Now call 'get_recipe_info' to get recipe information by providing recipe id and if you don't provide id then you 
will get a random recipe, 'get_recipe_ingredients' to get a food recipe ingredients by proving ingredients, 'get_recipe_joke' to get a recipe joke.
