from usda import UsdaClient
import random
client = UsdaClient('rfMvRseGhasTej6Ogcpj5gxidNqUtckuXjJIcOcM')



# ExampleRecipe1 = {
# 	'Ingredients': 
# 		[{
# 		'name': 'ground beef',
# 		'quantity': 1,
# 		'Measurement': "pound", 
# 		'Descriptor': "",
# 		'Preparation': "",
# 		'Tags': ""
# 				},
# 		{
# 		'Name': 'onion',
# 		'Quantity': 0.5,
# 		'Measurement': "",
# 		"Descriptor": "",
# 		'Preparation':"chopped"
# 				},
# 	   {
# 		'Name': 'red bell peppers',
# 		'Quantity': 2,
# 		'Measurement': "",
# 		'Descriptor': "",
# 		'Preparation': "cut",
# 				}, 
# 		],
					
# 	'Tools': ["knife", "tablespoon"], 

# 	'Methods': {"Primary_cooking_method": ["grill"],
# 				"alternative_cooking_method": ["grate", "heat", "slice", "cut"]},

# 	'Steps': ['Preheat the oven to 350 degrees F (175 degrees C).',
# 			  'Crumble the ground beef into a large cast-iron skillet over medium-high heat. Cook, stirring frequently, until beef is evenly brown.;',
# 			  'Mix the package of cornbread mix according to the directions using the egg and milk. Spoon over the ground beef mixture, and spread evenly.',
# 			  'Place the whole skillet in the oven, and bake for 20 minutes, or until a toothpick inserted into the cornbread layer comes out clean. Cool for a few minutes before serving.'
# 			  ]
# 	} 


# VegetarianRecipe1 = {
# 	'Ingredients': 
# 		[{
# 		'Name': 'butter',
# 		'Quantity': 1,
# 		'Measurement': "tablespoon", 
# 		'Descriptor': "",
# 		'Preparation': "",
# 		'Tags': ""
# 				},
# 		{
# 		'Name': 'onion',
# 		'Quantity': 0.5,
# 		'Measurement': "cup",
# 		"Descriptor": "",
# 		'Preparation':"sliced"
# 				},
# 	   {
# 		'Name': 'garlic',
# 		'Quantity': 2,
# 		'Measurement': "cloves",
# 		'Descriptor': "",
# 		'Preparation': "minced",
# 				}, 
# 		],
					
# 	'Tools': ["knife", "tablespoon", "saucepan", "skillet"], 

# 	'Methods': [""],

# 	'Steps': {'Step 1': 'Preheat the oven to 375 degrees F (190 degrees C).',
# 			  'Step 2': 'Melt butter in a saucepan over medium heat. Add garlic and onion; cook for a few minutes until fragrant, but not brown. Stir in spinach, and cook for about 5 more minutes. Remove from the heat, and mix in ricotta cheese, sour cream, and 1 cup of Monterey Jack cheese.',
# 			  'Step 3': 'In a skillet over medium heat, warm tortillas one at a time until flexible, about 15 seconds. Spoon about 1/4 cup of the spinach mixture onto the center of each tortilla. Roll up, and place seam side down in a 9x13 inch baking dish. Pour enchilada sauce over the top, and sprinkle with the remaining cup of Monterey Jack.',
# 			  'Step 4': 'Bake for 15 to 20 minutes in the preheated oven, until sauce is bubbling and cheese is lightly browned at the edges.'
# 			  }
# 	}

# ExampleRecipe2 = {
# 	'Ingredients': 
# 		[{
# 		'Name': 'Bread',
# 		'Quantity': 1,
# 		'Measurement': "pound", 
# 		'Descriptor': "",
# 		'Preparation': "",
# 		'Tags': ""
# 				},
# 		{
# 		'Name': 'mayo',
# 		'Quantity': 0.5,
# 		'Measurement': "",  
# 		"Descriptor": "",
# 		'Preparation':"chopped"
# 				},
# 	   {
# 		'Name': 'butter',
# 		'Quantity': 2,
# 		'Measurement': "",
# 		'Descriptor': "",
# 		'Preparation': "cut",
# 				}, 
# 		{
# 		'Name': 'oil',
# 		'Quantity': 2,
# 		'Measurement': "",
# 		'Descriptor': "",
# 		'Preparation': "cut",
# 				},
# 		{
# 		'Name': 'rice',
# 		'Quantity': 2,
# 		'Measurement': "",
# 		'Descriptor': "",
# 		'Preparation': "cut",
# 				}
# 		],
					
# 	'Tools': ["knife", "tablespoon"], 

# 	'Methods': [""],

# 	'Steps': {'Step 1': 'Preheat the oven to 350 degrees F (175 degrees C).',
# 			  'Step 2': 'Crumble the bread into a large cast-iron skillet over a bread of medium-high heat. Cook, stirring frequently, until mayo and butter are evenly brown.;',
# 			  'Step 3': 'Mix the package of oil mix according to the directions using the egg and milk. Spoon over the oil mixture, and spread evenly.',
# 			  'Step 4': 'Place the whole rice in the oven, and bake for 20 minutes, or until a toothpick inserted into the cornbread layer comes out clean. Cool for a few minutes before serving.'
# 			  }
# 	} 




meats = ["beef", "pork", "ground beef", "ham", "chicken", "bacon", "meat", "salami", "steak", "turkey", "duck", "lamb", "mutton", "duck", "veal", "sausage", "tilapia", "halibut", "cod", "salmon", "shrimp", "lobster", "crab", "catfish", "trout", "fish", "sardines", "tuna"]
non_meat_subs = ["tofu", "tempeh", "seitan", "textured vegetable protein", "jackfruit", "mushroom", "lentils", "beans"]
joined_meats = meats + non_meat_subs

#do pescatarian too
#could not find a way to distinguish between meat tagger but can use the text search feature of usda
#problem with usda text search: non-meat items can return meat items (see red bell peppers and onion)
#include everything that is a string in the search? helps with onion but not red bell pepper
def VegetarianTransformTo (recipe):

	new_steps = []
	my_sub = random.choice(non_meat_subs)
	for key, value in recipe["Recipe"].items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						# foods_search = client.search_foods(value1, 1)
						# my_food = next(foods_search)
						# report = client.get_food_report(my_food.id)
						# my_string = report.food.name.lower()
						if any(x in value1 for x in meats): #replace value1 with my_stirng if you want to use usda lib
							#print(value1)
							ing[key1] = my_sub
		if key == "Steps":
			for step in recipe['Recipe']['Steps']:
				for x in meats:
					if x in step:
						#print(value2.replace(x,"tofu"))
						step = step.replace(x, my_sub)
						new_steps.append(step)
						# value[key2] = value2.replace(x, my_sub) 

	recipe['Recipe'].pop("Steps", None)
	recipe['Recipe']['Steps'] = new_steps

	return recipe

#caseI: no meats or non-meats are in the whole recipe and we need to add some meat
#caseII: we need to replace meat subs with meat
def VegetarianTransformFrom (recipe):

	#Case I - no meat or meat subs are present
	my_meat = random.choice(meats)
	vegetarian = 1
	for key, value in recipe.items():
		if key == "Ingredients":
			for ing in value: 
				for key1, value1 in ing.items():
					if type(value1) == str:
						if any(x in value1 for x in joined_meats):
							vegetarian = 0
	#gotta add meat bc there are no meats and no non-meats
	if vegetarian == 1: 
		recipe['Ingredients'].append({'Name': my_meat, 'Quantity': 1, 'Measurement': "pound", 'Descriptor': "", 'Preparation': ""})
		recipe['Steps']['Added Step 1'] = 'Crumble the ' + my_meat +' into a large cast-iron skillet over medium-high heat. Stir frequently, until '+ my_meat +' is cooked well.;'
		recipe['Steps']['Added Step 2'] = 'Add the cooked ' + my_meat + ' to the rest of the dish.'

	#Case II - meat subs are present and we need to replace with meat

	for key, value in recipe.items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				#print(ing)
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						#foods_search = client.search_foods(value1, 1)
						#my_food = next(foods_search)
						#report = client.get_food_report(my_food.id)
						#my_string = report.food.name.lower()
						if any(x in value1 for x in meats): #replace value1 with my_stirng if you want to use usda lib
							#print(value1)
							ing[key1] = my_meat
		if key == "Steps":
			for key2, value2 in value.items():
				for x in meats:
					if x in value2:
						#print(value2.replace(x,"tofu"))
						value[key2] = value2.replace(x, my_meat) 


	return recipe					


my_breads = ["toast", "bread", "sourdough", "tortilla", "baguette", "bun", "pita", "bagel", "biscuit"]
my_sauces = ["mayo", "BBQ", "sauce", "sweet and sour", "chipotle sauce", "dressing", "ranch"]
my_masalas = ["Godha", "Tikka", "Tandoori", "Sambhar", "Chole"]
cooking_methods = ["fry", "cook", "bake", "grill", "sautè", "roast", "steam", "broil"]

def IndianTransformToV2 (recipe):
	masala = random.choice(my_masalas)
	#recipe['Ingredients'].append({'Name': "Garam Masala", 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
	if not "frying pan" in recipe['Tools']:
		recipe['Tools'].append("frying pan")
	#recipe['Ingredients'].append({'Name': "Coriander Chutney", 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})

	cooked_val = 0
	my_bread = ""
	for key, value in recipe.items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				#print(ing)
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						for x in my_breads:
							if x in value1.lower(): #replace bread with naan
								ing[key1] = "naan"
								my_bread = x
						if any(x in value1.lower() for x in my_sauces):
							ing[key1] = "coriander chutney"
						if "butter" in value1.lower():
							ing[key1] = "ghee"
						if "oil" in value1.lower():
							ing[key1] = "mustard oil"
						if "rice" in value1.lower():
							ing[key1] = "biryani"
							recipe['Ingredients'].append({'Name': "Biryani Masala", 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
							recipe['Steps']['Added Step 1'] = 'Before adding the biryani to your meal, fry the biryani masala for 10 minutes on medium heat. When finished, mix the fried masala with the biryani.'
		if key == "Steps":
			for key2, value2 in value.items():
				#for x in my_breads:
					#print(x)
				if my_bread in value2.lower():
					#print(my_bread)
					value[key2] = value2.replace(my_bread,"naan") 
					#print(value)
				#for x in my_sauces:
					#if x in value2.lower():
						#value[key2] = value2.replace(x, "coriander chutney")
				if "butter" in value2.lower():
					value[key2] = value2.replace("butter", "ghee")
				if "oil" in value2.lower():
					value[key2] = value2.replace("oil", "mustard oil")
				if "rice" in value2.lower():
					value[key2] = value2.replace("rice", "biryani")

	for methods in recipe['Methods']: 
		if any (x in methods for x in cooking_methods):
			cooked_val = 1

	if cooked_val == 1:
		recipe['Ingredients'].append({'Name': masala, 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		recipe['Steps']['Added Step 1'] = 'Take the .5 cups of ' + masala + ' masala and pour into the frying pan. Fry over medium heat in 3 tablespoons of mustard oil for 10 minutes until browning occurs.' 
		recipe['Steps']['Added Step 2'] = 'When the ' + masala + ' masala is finished frying, mix it into the rest of the dish.'
		if not "frying pan" in recipe['Tools']:
			recipe['Tools'].append('frying pan')
		if not "fry" in recipe['Methods']:
			recipe['Methods'].append('fry')

	if cooked_val == 0:
		recipe['Ingredients'].append({'Name': masala, 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		recipe['Ingredients'].append({'Name': "Kabuli chana", 'Quantity': 1, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		#recipe['Ingredients'].append({'Name': "tomato ", 'Quantity': 1, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		if not "boiling pot" in recipe['Tools']:
			recipe['Tools'].append("boiling pot")
		if not "bowl" in recipe['Tools']:
			recipe['Tools'].append("bowl")
		if not "frying pan" in recipe['Tools']:
			recipe['Tools'].append("frying pan")
		if not "wooden cooking spoon" in recipe['Tools']:
			recipe['Tools'].append("wooden cooking spoon")
		if not "fry" in recipe['Methods']:
			recipe['Tools'].append("fry")
		if not "mustard oil" in recipe['Tools']:
			recipe['Ingredients'].append({'Name': "Mustard Oil", 'Quantity': 3, 'Measurement': "tablespoon", 'Descriptor': "", 'Preparation': ""})
		recipe['Steps']['Added Step 1'] = 'Boil 1 cup of Kabuli chana over medium-high heat for 10 minutes. Once cooked, remove Kabuli chana from the pot and place into a bowl.'
		recipe['Steps']['Added Step 2'] = 'Take the .5 cups of garam masala and pour into the frying pan. Fry over medium heat in 3 tablespoons of mustard oil for 10 minutes until browning occurs.'
		recipe['Steps']['Added Step 3'] = 'Pour the fried Garam Masala mix into the bowl with the Kabuli channa and use the wooden spoon to mix together. Mix the Kabuli chana with the rest of your dish and enjoy!'


	return recipe








# def main():
# 	print(VegetarianTransformTo(ExampleRecipe1))

# #VegetarianTransform(ExampleRecipe1)
# #print(VegetarianTransformFrom(VegetarianRecipe1))
# #print(IndianTransformToV2(ExampleRecipe1))
# print(VegetarianTransformTo(ExampleRecipe1))
# print(VegetarianTransformFrom(VegetarianRecipe1))


#def HealthyTransform-> milk, yougurt, meat



	

