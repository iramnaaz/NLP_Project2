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
	
	while(1):
		print("Please enter which transformation you would like to do on your recipe:")
		print("0. Quit")
		print("1. Transform recipe to vegetarian")
		print("2. Transform recipe from vegetarian")
		print("3. Transform recipe to Indian Cuisine")
		choice = input()
		if choice == '0':
			break
		if choice == '1':
			print("Vegetarian Transformation: ")
		elif choice == '2':
			print("Non-Vegetarian Transformation: ")
		elif choice == '3':
			print("Indian Transformation: ")
		else:
			print("Not a valid Transformation")
    # meat_lasagna = rf.search_recipes('meat lasagna')[0]
    # res = rf.scrape_recipe(meat_lasagna)
    # # print("res ", res)
    # result_methods = methods_parse(res['directions'])
    # result_tools = tools_parse(res['directions'])
    # print("result_methods ", result_methods)
    # print("result_tools ", result_tools)
