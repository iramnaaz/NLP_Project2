from Extract_Method_Tools import methods_parse, tools_parse
from ingredient_scrape import RecipeFetcher
from ing_steps import fetch_and_pack
from transformation1 import *
from optional_transformation import *
from transformation2 import *
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
		print("Please enter which transformation you would like to do on your recipe by entering the appropriate number:")
		print("0. Quit")
		print("1. Transform recipe to vegetarian")
		print("2. Transform recipe from vegetarian")
		print("3. Transform recipe to Indian Cuisine")
		print("4. Transform recipe to Chinese Cuisine")
		print("5. Transform recipe to a different size")
		print("6. Transform recipe to a healthy version")
		choice = input()
		if choice == '0':
			break
		if choice == '1':
			print("Original Recipe: \n")
			print(recipe)
			vegRecipe1 = VegetarianTransformTo(recipe)
			print("Vegetarian Transformation: \n")
			print(vegRecipe1)
			print("You can also see veg_recipe.json for the transformed recipe")
			with open('veg_recipe.json', 'w') as outfile:
			    json.dump(vegRecipe1, outfile)
		elif choice == '2':
			print("Original Recipe: \n")
			print(recipe)
			unvegRecipe2 = VegetarianTransformFrom(recipe)
			print("Vegetarian Transformation: \n")
			print(unvegRecipe2)
			print("You can also see unveg_recipe.json for the transformed recipe")
			with open('unveg_recipe.json', 'w') as outfile:
			    json.dump(unvegRecipe2, outfile)
		elif choice == '3':
			print("Original Recipe: \n")
			print(recipe)
			IndianRecipe = IndianTransformToV2(recipe)
			print("Indian Transformation: \n")
			print(IndianRecipe)
			print("You can also see indian_recipe.json for the transformed recipe")
			with open('indian_recipe.json', 'w') as outfile:
				json.dump(IndianRecipe, outfile)
		elif choice == '4':
			print("Original Recipe: \n")
			print(recipe)
			ChineseRecipe = transformation_to_chinese(recipe)
			print("Chinese Transformation: \n")
			print(ChineseRecipe)
			print("You can also see chinese_recipe.json for the transformed recipe")
			with open('chinese_recipe.json', 'w') as outfile:
				json.dump(ChineseRecipe, outfile)
		elif choice == '5':
			print("Please enter a multiplier by which you would like to change the size of your recipe.")
			my_multiplier = input()
			print("Original Recipe: \n")
			print(recipe)
			Scaled_Recipe = DoubleOrHalf(recipe, float(my_multiplier))
			print("Size Transformation: \n")
			print(Scaled_Recipe)
			print("\n")
			print("You can also see size_change.json for the transformed recipe")
			with open('size_change.json', 'w') as outfile:
				json.dump(Scaled_Recipe, outfile)
		elif choice == '6':
			print("Original Recipe: \n")
			print(recipe)
			HealthyRecipe = HealthyTransformTo(recipe)
			print("HealthyTransformation: \n")
			print(HealthyRecipe)
			print("Please see healthy_recipe.json for the transformed recipe")
			with open('healthy_recipe.json', 'w') as outfile:
				json.dump(HealthyRecipe, outfile)

		else:
			print("Not a valid Transformation")
    # meat_lasagna = rf.search_recipes('meat lasagna')[0]
    # res = rf.scrape_recipe(meat_lasagna)
    # # print("res ", res)
    # result_methods = methods_parse(res['directions'])
    # result_tools = tools_parse(res['directions'])
    # print("result_methods ", result_methods)
    # print("result_tools ", result_tools)
