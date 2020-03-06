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
		print("9. Transform recipe into vegan")
		print("10. Transform recipe into gluten-free")
		choice = input()
		if choice == '0':
			break
		if choice == '1':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1

			vegRecipe1 = VegetarianTransformTo(recipe)
			print('\n')
			print("Transformation to Vegetarian (full recipe): \n")
			print(vegRecipe1)
			print("\nYou can also see veg_recipe.json for the transformed recipe.")
			print("\nSee below for a human-readable version of your vegetarian recipe:\n")

			for key, value in vegRecipe1['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1


			with open('veg_recipe.json', 'w') as outfile:
			    json.dump(vegRecipe1, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("\nPlease press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '2':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)

			print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1



			unvegRecipe2 = VegetarianTransformFrom(recipe)
			print('\n')
			print("Transformation from Vegetarian: \n")
			print(unvegRecipe2)
			print("\nYou can also see unveg_recipe.json for the transformed recipe.")

			print("\nSee below for a human-readable version of your vegetarian recipe:\n")

			for key, value in unvegRecipe2['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1


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

			print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1



			IndianRecipe = IndianTransform(recipe)
			print('\n')
			print("Indian Transformation: \n")
			print(IndianRecipe)
			print("\nYou can also see indian_recipe.json for the transformed recipe.")



			print("\nSee below for a human-readable version of your Indian recipe:\n")

			for key, value in IndianRecipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1



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

			print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1



			ChineseRecipe = transformation_to_chinese(recipe)
			print('\n')
			print("Chinese Transformation: \n")
			print(ChineseRecipe)
			print("\nYou can also see chinese_recipe.json for the transformed recipe.")

			print("\nSee below for a human-readable version of your Chinese recipe:\n")
			for key, value in ChineseRecipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1

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

			print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1


			Scaled_Recipe = DoubleOrHalf(recipe, float(my_multiplier))
			print('\n')
			print("Size Transformation: \n")
			print(Scaled_Recipe)
			print("\n")
			print("\nYou can also see size_change.json for the transformed recipe.")

			print("\nSee below for a human-readable version of your differently sized recipe:\n")
			for key, value in Scaled_Recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1


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

			print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1


			HealthyRecipe = HealthyTransformTo(recipe)
			print('\n')
			print("Healthy Transformation: \n")
			print(HealthyRecipe)
			print("\nYou can also see healthy_recipe.json for the transformed recipe.")

			print("\nSee below for a human-readable version of your healthy recipe:\n")
			for key, value in HealthyRecipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1


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
			print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1





			PescatarianRecipe = PescatarianTransformTo(recipe)
			print('\n')
			print("Pescatarian Transformation: \n")
			print(PescatarianRecipe)
			print("\nYou can also see pescatarian_recipe.json for the transformed recipe (full version).")
			print("\nSee below for a human-readable version of your pescatarian recipe:\n")

			for key, value in PescatarianRecipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1

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
		elif choice == '9':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			VeganRecipe = VeganTransform(recipe)
			print('\n')
			print("Vegan Transformation: \n")
			print(VeganRecipe)
			print("\nYou can also see vegan_recipe.json for the transformed recipe.")
			with open('vegan_recipe.json', 'w') as outfile:
				json.dump(VeganRecipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("Please press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		elif choice == '10':
			print("\n")
			print("Original Recipe: \n")
			print(recipe)
			GlutenFreeRecipe = GlutenFreeTransform(recipe)
			print('\n')
			print("GlutenFree Transformation: \n")
			print(GlutenFreeRecipe)
			print("\nYou can also see gluten_free_recipe.json for the transformed recipe.")
			with open('gluten_free_recipe.json', 'w') as outfile:
				json.dump(GlutenFreeRecipe, outfile)
			print('\nPlease choose how you would like to proceed by entering the appropriate number:')
			print("1. Continue transforming the recipe.")
			print("2. Start from scratch with a new recipe.")
			my_choice = input()
			if my_choice == '2':
				print("\nPlease press 0 when prompted for a transformation and then run 'python3 main_file.py' again in your command line.")
		else:
			print("Not a valid Transformation")
    # meat_lasagna = rf.search_recipes('meat lasagna')[0]
    # res = rf.scrape_recipe(meat_lasagna)
    # # print("res ", res)
    # result_methods = methods_parse(res['directions'])
    # result_tools = tools_parse(res['directions'])
    # print("result_methods ", result_methods)
    # print("result_tools ", result_tools)
