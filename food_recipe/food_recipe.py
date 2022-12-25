import logging
import os
import spoonacular as sp

from exceptions.exceptions import (FoodRecipeFailedException, FoodRecipeJokeFailedException,
                                   FoodRecipeIngredientsFailedException, )

log = logging.getLogger(__name__)


class FoodRecipe:
    """
    FoodRecipe class
    """

    def __init__(self):
        """
        Sets recipe api and gets api key
        through environment variable.
        """
        self.recipe = sp.API(os.getenv('FOOD_RECIPE_API_KEY'))  # Get Your API : https://spoonacular.com/

    def get_recipe_info(self, recipe_id: str = None):
        """
        Takes recipe_id and returns
        food recipe info

        :param recipe_id: str object
        :return: food recipe or raise FoodRecipeFailedException
        """
        log.info("Fetching food recipe for recipe id [%s]", recipe_id)
        try:
            if recipe_id:
                return self.recipe.get_recipe_information(id=recipe_id)
            else:
                return self.recipe.get_a_random_recipe().json()['recipes'][0]
        except Exception as e:
            log.error("Food recipe request failed due to [%s] for id [%s]", e, recipe_id)
            raise FoodRecipeFailedException

    def get_recipe_ingredients(self, ingredients: str):
        """
        Takes ingredients and returns
        food recipe ingredients

        :param ingredients: str object
        :return: food recipe ingredients or raise FoodRecipeIngredientsFailedException
        """
        log.info("Fetching food recipe ingredients [%s]", ingredients)
        try:
            return self.recipe.parse_ingredients(ingredients)
        except Exception as e:
            log.error("Food recipe ingredients [%s] request failed due to [%s]", ingredients, e)
            raise FoodRecipeIngredientsFailedException

    def get_recipe_joke(self):
        """
        Returns a random food recipe joke

        :return: food recipe joke or raise FoodRecipeJokeFailedException
        """
        log.info("Fetching food recipe joke")
        try:
            response = self.recipe.get_a_random_food_joke()
            return response.json()['text']
        except Exception as e:
            log.error("Food recipe joke failed due to [%s]", e)
            raise FoodRecipeJokeFailedException


if __name__ == '__main__':
    food_recipe = FoodRecipe()
    print(food_recipe.get_recipe_info('recipe_id'))
    print(food_recipe.get_recipe_ingredients("5.25 cups flour"))
    print(food_recipe.get_recipe_joke())
