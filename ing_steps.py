from ingredient_scrape import RecipeFetcher
from ing_packer import make_ing_list
from Extract_Method_Tools import *
import json

rf = RecipeFetcher()
meat_lasagna = rf.search_recipes('meat lasagna')[0]
res = rf.scrape_recipe(meat_lasagna)

directions = res['directions']

ing_obj = make_ing_list(res['ingredients'])

methods = methods_parse(directions)

tools = tools_parse(directions)

# print(methods)
# print(tools)
# print(ing_obj)

recipe_comp = {}

recipe_comp["Ingredients"] = ing_obj
recipe_comp["Tools"] = tools
recipe_comp["Methods"] = methods
recipe_comp["Steps"] = directions

recipe = {}
recipe["Recipe"] = recipe_comp
print(recipe_comp)

with open('recipe.json', 'w') as outfile:
    json.dump(recipe, outfile)
# recipe["Recipe"] = {
# 	"Ingredients": {ing_obj},
# 	"Steps": {res['directions']}
# }