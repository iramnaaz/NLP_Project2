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
		print("\nPlease enter which transformation you would like to do on your recipe by entering the appropriate number:\n")
		print("0. Quit")
		print("1. Transform recipe into vegetarian")
		print("2. Transform recipe from vegetarian")
		print("3. Transform recipe to Indian Cuisine")
		print("4. Transform recipe to Chinese Cuisine")
		print("5. Transform recipe to a different size")
		print("6. Transform recipe to a healthy version")
		print("7. Transform recipe into pescatarian")
		print("8. Transform recipe from pescatarian")
		choice = input()
		if choice == '0':
			break
		if choice == '1':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			vegRecipe1 = VegetarianTransformTo(recipe)
			print('\n')
			print("Transformation to Vegetarian: \n")
			print(vegRecipe1)
			print("\nYou can also see veg_recipe.json for the transformed recipe.")
			with open('veg_recipe.json', 'w') as outfile:
			    json.dump(vegRecipe1, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '2':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			unvegRecipe2 = VegetarianTransformFrom(recipe)
			print('\n')
			print("Transformation from Vegetarian: \n")
			print(unvegRecipe2)
			print("\nYou can also see unveg_recipe.json for the transformed recipe.")
			with open('unveg_recipe.json', 'w') as outfile:
			    json.dump(unvegRecipe2, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '3':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			IndianRecipe = IndianTransform(recipe)
			print('\n')
			print("Indian Transformation: \n")
			print(IndianRecipe)
			print("\nYou can also see indian_recipe.json for the transformed recipe.")
			with open('indian_recipe.json', 'w') as outfile:
				json.dump(IndianRecipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '4':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			ChineseRecipe = transformation_to_chinese(recipe)
			print('\n')
			print("Chinese Transformation: \n")
			print(ChineseRecipe)
			print("\nYou can also see chinese_recipe.json for the transformed recipe.")
			with open('chinese_recipe.json', 'w') as outfile:
				json.dump(ChineseRecipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '5':
			print("Please enter a multiplier by which you would like to change the size of your recipe.")
			my_multiplier = input()
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			Scaled_Recipe = DoubleOrHalf(recipe, float(my_multiplier))
			print('\n')
			print("Size Transformation: \n")
			print(Scaled_Recipe)
			print("\n")
			print("\nYou can also see size_change.json for the transformed recipe.")
			with open('size_change.json', 'w') as outfile:
				json.dump(Scaled_Recipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '6':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			HealthyRecipe = HealthyTransformTo(recipe)
			print('\n')
			print("Healthy Transformation: \n")
			print(HealthyRecipe)
			print("\nYou can also see healthy_recipe.json for the transformed recipe.")
			with open('healthy_recipe.json', 'w') as outfile:
				json.dump(HealthyRecipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '7':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			PescatarianRecipe = PescatarianTransformTo(recipe)
			print('\n')
			print("Pescatarian Transformation: \n")
			print(PescatarianRecipe)
			print("\nYou can also see pescatarian_recipe.json for the transformed recipe.")
			with open('pescatarian_recipe.json', 'w') as outfile:
				json.dump(PescatarianRecipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '8':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			PescatarianRecipe = PescatarianTransformFrom(recipe)
			print('\n')
			print("Pescatarian Transformation: \n")
			print(PescatarianRecipe)
			print("\nYou can also see pescatarian_recipe.json for the transformed recipe.")
			with open('pescatarian_recipe.json', 'w') as outfile:
				json.dump(PescatarianRecipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		else:
			print("Not a valid Transformation")
    # meat_lasagna = rf.search_recipes('meat lasagna')[0]
    # res = rf.scrape_recipe(meat_lasagna)
    # # print("res ", res)
    # result_methods = methods_parse(res['directions'])
    # result_tools = tools_parse(res['directions'])
    # print("result_methods ", result_methods)
    # print("result_tools ", result_tools)
