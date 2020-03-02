from usda import UsdaClient
import random
client = UsdaClient('rfMvRseGhasTej6Ogcpj5gxidNqUtckuXjJIcOcM')



ExampleRecipe1 = {
	'Ingredients': 
		[{
		'Name': 'ground beef',
		'Quantity': 1,
		'Measurement': "pound", 
		'Descriptor': "",
		'Preparation': "",
		'Tags': ""
				},
		{
		'Name': 'onion',
		'Quantity': 0.5,
		'Measurement': "",
		"Descriptor": "",
		'Preparation':"chopped"
				},
	   {
		'Name': 'red bell peppers',
		'Quantity': 2,
		'Measurement': "",
		'Descriptor': "",
		'Preparation': "cut",
				}, 
		],
					
	'Tools': ["knife", "tablespoon"], 

	'Methods': [""],

	'Steps': {'Step 1': 'Preheat the oven to 350 degrees F (175 degrees C).',
			  'Step 2': 'Crumble the ground beef into a large cast-iron skillet over medium-high heat. Cook, stirring frequently, until beef is evenly brown.;',
			  'Step 3': 'Mix the package of cornbread mix according to the directions using the egg and milk. Spoon over the ground beef mixture, and spread evenly.',
			  'Step 4': 'Place the whole skillet in the oven, and bake for 20 minutes, or until a toothpick inserted into the cornbread layer comes out clean. Cool for a few minutes before serving.'
			  }
	} 


VegetarianRecipe1 = {
	'Ingredients': 
		[{
		'Name': 'butter',
		'Quantity': 1,
		'Measurement': "tablespoon", 
		'Descriptor': "",
		'Preparation': "",
		'Tags': ""
				},
		{
		'Name': 'onion',
		'Quantity': 0.5,
		'Measurement': "cup",
		"Descriptor": "",
		'Preparation':"sliced"
				},
	   {
		'Name': 'garlic',
		'Quantity': 2,
		'Measurement': "cloves",
		'Descriptor': "",
		'Preparation': "minced",
				}, 
		],
					
	'Tools': ["knife", "tablespoon", "saucepan", "skillet"], 

	'Methods': [""],

	'Steps': {'Step 1': 'Preheat the oven to 375 degrees F (190 degrees C).',
			  'Step 2': 'Melt butter in a saucepan over medium heat. Add garlic and onion; cook for a few minutes until fragrant, but not brown. Stir in spinach, and cook for about 5 more minutes. Remove from the heat, and mix in ricotta cheese, sour cream, and 1 cup of Monterey Jack cheese.',
			  'Step 3': 'In a skillet over medium heat, warm tortillas one at a time until flexible, about 15 seconds. Spoon about 1/4 cup of the spinach mixture onto the center of each tortilla. Roll up, and place seam side down in a 9x13 inch baking dish. Pour enchilada sauce over the top, and sprinkle with the remaining cup of Monterey Jack.',
			  'Step 4': 'Bake for 15 to 20 minutes in the preheated oven, until sauce is bubbling and cheese is lightly browned at the edges.'
			  }
	} 





meats = ["beef", "pork", "ground beef", "ham", "chicken", "bacon", "meat", "salami", "steak", "turkey", "duck", "lamb", "mutton", "duck", "veal", "sausage", "tilapia", "halibut", "cod", "salmon", "shrimp", "lobster", "crab", "catfish", "trout", "fish", "sardines", "tuna"]
non_meat_subs = ["tofu", "tempeh", "seitan", "textured vegetable protein", "jackfruit", "mushroom", "lentils", "beans"]
joined_meats = meats + non_meat_subs

#do pescatarian too
#could not find a way to distinguish between meat tagger but can use the text search feature of usda
#problem with usda text search: non-meat items can return meat items (see red bell peppers and onion)
#include everything that is a string in the search? helps with onion but not red bell pepper
def VegetarianTransformTo (recipe):
	my_sub = random.choice(non_meat_subs)
	for key, value in recipe.items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				#print(ing)
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						foods_search = client.search_foods(value1, 1)
						my_food = next(foods_search)
						report = client.get_food_report(my_food.id)
						my_string = report.food.name.lower()
						if any(x in value1 for x in meats): #replace value1 with my_stirng if you want to use usda lib
							#print(value1)
							ing[key1] = my_sub
		if key == "Steps":
			for key2, value2 in value.items():
				for x in meats:
					if x in value2:
						#print(value2.replace(x,"tofu"))
						value[key2] = value2.replace(x, my_sub) 


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



def IndianCuisineTransformTo (recipe):

	






def main():
	print(VegetarianTransformTo(ExampleRecipe1))

#VegetarianTransform(ExampleRecipe1)
print(VegetarianTransformFrom(VegetarianRecipe1))


#def HealthyTransform-> milk, yougurt, meat



	

