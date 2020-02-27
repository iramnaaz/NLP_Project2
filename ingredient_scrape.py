from bs4 import BeautifulSoup

import requests

from collections import Counter

class RecipeFetcher:

    search_base_url = 'https://www.allrecipes.com/search/results/?wt=%s&sort=re'

    def search_recipes(self, keywords): 
        search_url = self.search_base_url %(keywords.replace(' ','+'))

        page_html = requests.get(search_url)
        page_graph = BeautifulSoup(page_html.content)

        return [recipe.a['href'] for recipe in\
               page_graph.find_all('div', {'class':'grid-card-image-container'})]

    def scrape_recipe(self, recipe_url):
        results = {}

        page_html = requests.get(recipe_url)
        page_graph = BeautifulSoup(page_html.content)
        # recipe-directions__list--item
        found = page_graph.find_all(itemprop = "recipeIngredient")
        found2 = page_graph.find('class' == "recipe-directions__list--item")
        print(found2)
        ing = []
        for ingredient in found:
          ing.append(ingredient.text)
        print(ing)
        
        # results['ingredients'] = # Fill out this list comprehension and get each element's text

        # results['directions'] = # Fill out this list comprehension and get each element's text
        
        return results

    
rf = RecipeFetcher()
meat_lasagna = rf.search_recipes('meat lasagna')[0]
print(meat_lasagna)
rf.scrape_recipe(meat_lasagna)