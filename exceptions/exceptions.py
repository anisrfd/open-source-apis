class ImageBackgroundRemoveFailedException(Exception):
    """
    Exception raised if image background remove api failed
    """
    pass


class MovieDBFailedException(Exception):
    """
    Exception raised if movie database api failed to get movie info
    """
    pass


class NewsCatcherFailedException(Exception):
    """
    Exception raised if news catcher api failed to get news
    """
    pass


class PokemonFetchFailedException(Exception):
    """
    Exception raised if pokemon api failed to get info
    """
    pass


class URLShortenFailedException(Exception):
    """
    Exception raised if url shorten api failed to get short url
    """
    pass
