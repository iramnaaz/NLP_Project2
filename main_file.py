from Extract_Method_Tools import methods_parse, tools_parse
from ingredient_scrape import RecipeFetcher
from ing_steps import fetch_and_pack
import json

print("Please input a recipe URL:")
rf = RecipeFetcher()
url = input()
results = rf.search_recipes(url)
print("Search is Over..Thank you for waiting!")
if not results:
    print("Ooops I think it is not some kind of food")
else:
	fetch_and_pack(results[0])
	recipe = {}
	with open('recipe.json', 'r') as f:
	    recipe = json.load(f)
	print(recipe)
    # meat_lasagna = rf.search_recipes('meat lasagna')[0]
    # res = rf.scrape_recipe(meat_lasagna)
    # # print("res ", res)
    # result_methods = methods_parse(res['directions'])
    # result_tools = tools_parse(res['directions'])
    # print("result_methods ", result_methods)
    # print("result_tools ", result_tools)
