from usda import UsdaClient
import random
client = UsdaClient('rfMvRseGhasTej6Ogcpj5gxidNqUtckuXjJIcOcM')


meats = ["beef", "meat", "pork", "chicken breast", "mutton thigh", "t-bone steak", "ground beef", "ham", "chicken", "bacon", "salami", "steak", "turkey", "duck", "lamb", "mutton", "duck", "veal", "sausage", "tilapia", "halibut", "cod", "salmon", "shrimp", "lobster", "crab", "catfish", "trout", "sardines", "tuna"]
non_meat_subs = ["tofu", "tempeh", "seitan", "textured vegetable protein", "jackfruit", "mushroom", "lentils", "beans"]
fish = ["tilapia", "halibut", "cod", "salmon", "shrimp", "lobster", "crab", "catfish", "trout", "sardines", "tuna"] 
joined_meats = meats + non_meat_subs
joined_meats_w_fish = meats + fish

#do pescatarian too
#could not find a way to distinguish between meat tagger but can use the text search feature of usda
#problem with usda text search: non-meat items can return meat items (see red bell peppers and onion)
#include everything that is a string in the search? helps with onion but not red bell pepper
def VegetarianTransformTo (recipe):
	print("\n*******************************")
	print("\nYour recipe with less meat is coming right up!\n")
	print("Here are the transformations that were made to your recipe:")

	new_steps = recipe['Recipe']['Steps']
	my_sub = random.choice(non_meat_subs)
	for key, value in recipe["Recipe"].items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						if any(x in value1 for x in meats): #replace value1 with my_stirng if you want to use usda lib
							#print(value1)
							ing[key1] = my_sub
							print("\n\tReplaced " + value1 + " with " + my_sub)
		num = 0
		if key == "Steps":
			for step in new_steps:
				#print(step)
				number = new_steps.index(step)
				temp = step
				for x in meats:
					#print(x)
					if x in step:
						#print(value2.replace(x,"tofu"))
						#new_steps = recipe['Recipe']['Steps']
						#print(x)
						#print(step)
						
						new_steps.remove(temp)
						new_steps.insert(number, step.replace(x, my_sub))
						temp = new_steps[number]
						num += 1
			print("\n\tChanged " + str(num) + " steps in the recipe")

	#recipe['Recipe'].pop("Steps", None)
	#print(new_steps)
	recipe['Recipe']['Steps'] = new_steps
	#print (recipe['Recipe']['Steps'])
	return recipe

def PescatarianTransformTo (recipe):

	print("\n*******************************")
	print("\nYour recipe with less meat and more fish is coming right up!\n")
	print("Here are the transformations that were made to your recipe:")

	new_steps = recipe['Recipe']['Steps']
	my_sub = random.choice(fish)
	for key, value in recipe["Recipe"].items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						if any(x in value1 for x in meats): #replace value1 with my_stirng if you want to use usda lib
							#print(value1)
							ing[key1] = my_sub
							print("\n\tReplaced " + value1 + " with " + my_sub)
		num = 0
		if key == "Steps":
			for step in new_steps:
				#print(step)
				number = new_steps.index(step)
				temp = step
				for x in meats:
					#print(x)
					if x in step:
						#print(value2.replace(x,"tofu"))
						#new_steps = recipe['Recipe']['Steps']
						#print(x)
						#print(step)
						
						new_steps.remove(temp)
						new_steps.insert(number, step.replace(x, my_sub))
						temp = new_steps[number]

			print("\n\tChanged " + str(num) + " steps in the recipe")

	#recipe['Recipe'].pop("Steps", None)
	#print(new_steps)
	recipe['Recipe']['Steps'] = new_steps
	#print (recipe['Recipe']['Steps'])
	return recipe


def PescatarianTransformFrom (recipe):
	#convert fish to meat
	new_steps = recipe['Recipe']['Steps']
	my_sub = random.choice(meats)
	for key, value in recipe["Recipe"].items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						if any(x in value1 for x in fish): #replace value1 with my_stirng if you want to use usda lib
							#print(value1)
							ing[key1] = my_sub
		if key == "Steps":
			for step in new_steps:
				#print(step)
				number = new_steps.index(step)
				temp = step
				for x in fish:
					#print(x)
					if x in step:
						#print(value2.replace(x,"tofu"))
						#new_steps = recipe['Recipe']['Steps']
						#print(x)
						#print(step)
						
						new_steps.remove(temp)
						new_steps.insert(number, step.replace(x, my_sub))
						temp = new_steps[number]

	#if there is no fish present, then we need to add meat to recipe

		vegetarian = 1
		for key, value in recipe['Recipe'].items():
			if key == "Ingredients":
				#print(value)
				for ing in value: 
					for key1, value1 in ing.items():
						#print(value1)
						if type(value1) == str:
							#print(value1)
							for x in meats:
								#print(value1)
								if x in value1:
									vegetarian = 0
		#gotta add meat bc there is on if
		if vegetarian == 1: 
			recipe['Recipe']['Ingredients'].append({'quantity': 1, 'measurement': "pound", 'name': my_sub})
			#new_steps = recipe['Recipe']['Steps']
			new_steps.append ('Crumble the ' + my_sub +' into a large cast-iron skillet over medium-high heat. Stir frequently, until '+ my_sub +' is cooked well.;')
			new_steps.append('Add the cooked ' + my_sub + ' to the rest of the dish.')
			recipe['Recipe']['Tools'].append('large cast-iron skillet ')






	#recipe['Recipe'].pop("Steps", None)
	#print(new_steps)
	recipe['Recipe']['Steps'] = new_steps
	#print (recipe['Recipe']['Steps'])
	return recipe

#caseI: no meats or non-meats are in the whole recipe and we need to add some meat
#caseII: we need to replace meat subs with meat

VegFrom = {"Recipe": {"Ingredients": [{"quantity": "1", "name": "long thin baguette"}, 
	{"quantity": "0.25", "measurement": "cup", "name": "olive oil, divided"}, 
	{"quantity": "2", "preparation": "halved", "name": "chicken"}, 
	{"quantity": "1", "preparation": "halved", "name": "small tomato,  and seeded"}, 
	{"quantity": "1", "measurement": "quart", "name": "head romaine lettuce, outer leaves discarded and head cut into ers"}, 
	{"quantity": "", "measurement": "to taste", "name": "salt and coarsely ground black pepper"}, 
	{"quantity": "1", "measurement": "cup", "name": "Caesar salad dressing"}, 
	{"quantity": "0.5", "measurement": "cup", "name": "Parmesan cheese shavings"}], 
"Tools": ["grate"], 
"Methods": {"Primary_cooking_method": ["grill"], 
"alternative_cooking_method": ["grate", "heat", "slice", "cut"]}, 
"Steps": ["Preheat grill for low heat and lightly oil the grate.", "Cut chicken on a severely sharp diagonal to make 4 long slices about 1/2-inch thick. Lightly brush each cut side with about half of the olive oil.", "Grill baguette slices on the preheated grill until lightly crispy, 2 to 3 minutes per side. Rub each side of baguette slices with the cut-side of garlic and cut-side of tomatoes. Set aside to cool.", "Brush 2 cut sides of romaine quarters with remaining olive oil.", "Grill romaine quarters until lightly seared, 2 to 3 minutes per side. Sprinkle grilled romaine with salt and set aside to cool.", "Place a grilled romaine quarter, cut-side up, on top of a grilled baguette slice. Drizzle each with Caesar dressing and top with Parmesan cheese. Season with salt and black pepper."]}}


#fix steps part?
def VegetarianTransformFrom (recipe):
	print("\n*******************************")
	print("\nYour recipe with more meat is coming right up!\n")
	print("Here are the transformations that were made to your recipe:")

	new_steps = recipe['Recipe']['Steps']
	#Case I - no meat or meat subs are present
	my_meat = random.choice(meats)
	vegetarian = 1
	for key, value in recipe['Recipe'].items():
		if key == "Ingredients":
			#print(value)
			for ing in value: 
				for key1, value1 in ing.items():
					#print(value1)
					if type(value1) == str:
						#print(value1)
						for x in joined_meats:
							#print(value1)
							if x in value1:
								vegetarian = 0
	#gotta add meat bc there are no meats and no non-meats
	if vegetarian == 1: 
		recipe['Recipe']['Ingredients'].append({'quantity': '1', 'measurement': "pound", 'name': my_meat})
		print("\n\tAdded " + my_meat + " to the list of ingredients")
		recipe['Recipe']['Tools'].append('large cast-iron skillet')
		print("\n\tAdded large-cast-iron skillet to the list of tools")
		#new_steps = recipe['Recipe']['Steps']
		new_steps.append ('Crumble the ' + my_meat +' into a large cast-iron skillet over medium-high heat. Stir frequently, until '+ my_meat +' is cooked well.')
		new_steps.append('Add the cooked ' + my_meat + ' to the rest of the dish.')
		print('\n\tAdded 2 new steps to the recipe')
	#Case II - meat subs are present and we need to replace with meat

	for key, value in recipe['Recipe'].items():
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
						if any(x in value1 for x in non_meat_subs): #replace value1 with my_stirng if you want to use usda lib
							#print(value1)
							ing[key1] = my_meat
							print("\n\tReplaced " + value1 + " with " + my_meat)
		num = 0
		if key == "Steps":
			for step in new_steps: #recipe['Recipe']['Steps']:
				number = new_steps.index(step)
				temp = step
				for x in non_meat_subs:
					if x in step:
						#print(value2.replace(x,"tofu"))
						#new_steps = recipe['Recipe']['Steps']
						#number = recipe['Recipe']['Steps'].index(step)
						#recipe['Recipe']['Steps'].remove(step)
						new_steps.remove(temp)
						#step = step.replace(x, my_meat) 
						new_steps.insert(number, step.replace(x, my_meat))
						temp = new_steps[number]
						num+=1
			print("\n\tChanged " + str(num) + " steps in the recipe")


	#recipe['Recipe'].pop("Steps", None)
	recipe['Recipe']['Steps'] = new_steps

	return recipe					


my_breads = ["toast", "bread", "sourdough", "tortilla", "baguette", "bun", "pita", "bagel", "biscuit"]
my_sauces = ["mayo", "BBQ", "sauce", "sweet and sour", "chipotle sauce", "dressing", "ranch"]
my_masalas = ["Godha", "Tikka", "Tandoori", "Sambhar", "Chole"]
cooking_methods = ["fry", "cook", "bake", "sautè", "roast", "steam", "broil"]



ExampleRecipe2 = {"Recipe": {"Ingredients": 
	[{"quantity": "4", "measurement": "ounce", "name": "mayo"}, 
	{"quantity": "2", "preparation": "sliced", "name": "boneless, skinless chicken breast halves,  into thin strips"}, 
	{"quantity": "2", "measurement": "teaspoon", "name": "butter"}, 
	{"quantity": "2", "measurement": "tablespoon", "name": "oil"}, 
	{"quantity": "1", "preparation": "chopped", "name": "bread,"}, 
	{"quantity": "", "preparation": "chopped", "name": "\u00bd  red bell pepper,"}, 
	{"quantity": "4", "preparation": "sliced", "name": "fresh mushrooms,"}, 
	{"quantity": "1", "preparation": "minced", "name": "rice,"}, 
	{"quantity": "1", "measurement": "cup", "name": "\u00bd  heavy cream"}, 
	{"quantity": "", "measurement": "teaspoon", "name": "\u00bc  dried basil"}, 
	{"quantity": "", "measurement": "teaspoon", "name": "\u00bc  lemon pepper"}, 
	{"quantity": "", "measurement": "teaspoon", "name": "\u00bc  salt"}, 
	{"quantity": "", "measurement": "teaspoon", "name": "\u215b  garlic powder"}, 
	{"quantity": "", "measurement": "teaspoon", "name": "\u215b  ground black pepper"}, 
	{"quantity": "2", "measurement": "tablespoon", "preparation": "grated", "name": "Parmesan cheese"}, 
	{"Name": "Sambhar", "Quantity": 0.5, "Measurement": "cup", "Descriptor": "", "Preparation": ""}], 
	"Tools": ["skillet", "bowl", "pot", "frying pan"], 
	"Methods": {"Primary_cooking_method": ["saute", "boil", "cook"], "alternative_cooking_method": ["toss", "drain", "heat", "coat", "stir", "fry"]}, 
	"Steps": ["Bring a large pot of lightly salted mayo to a boil. Add linguini butter, and cook for 8 to 10 minutes, or until al dente; drain.", 
	"Meanwhile, place bread and Cajun seasoning in a bowl, and toss to coat.", 
	"In a large skillet over medium heat, saute oil in butter until no longer pink and juices run clear, about 5 to 7 minutes. Add green and red bell peppers, sliced mushrooms and green onions; cook for 2 to 3 minutes. Reduce heat, and stir in heavy cream. Season the sauce with basil, lemon pepper, salt, garlic powder and ground black pepper, and heat through.", 
	"In a large bowl, toss linguini with sauce. Sprinkle with grated Parmesan cheese.", "Take the .5 cups of rice and pour into the frying pan. Fry over medium heat in 3 tablespoons of mustard oil for 10 minutes until browning occurs.", 
	"When the Sambhar masala is finished frying, mix it into the rest of the dish."]}}


indian_subs = {
	
	'cheese': 'paneer',
	'bread': 'naan',
	'toast': 'paratha',
	'tortilla': 'naan',
	'flatbread': 'chapati',
	'bun': 'naan',
	'pita': 'roti,',
	'bagel': 'naan',
	'pancake': 'chapati',
	'rice': 'biryani',
	'oil': 'mustard oil',
	'butter': 'ghee',
	'lamb': 'gosht',
	'mayo': 'coriander chutney',
	'mayonnaise': 'coriander chutney',
	'okra': 'bhindi',
	'chick peas': 'chana',
	'cauliflower': 'gobi',
	'broccoli': 'gobi',
	'pasta': 'white rice',
	'beef': 'lamb kebab',
	'chicken': 'chicken tikka',
	'bacon': 'chicken tikka',
	'ham': 'chicken tandoori',
	'sausage': 'seekh kebab',
	'potato': 'aloo potato',
	'lettuce': 'gobi',
	'apple': 'mango',
	'strawberry': 'mango',
	'spaghetti': 'biryani',
	'noodles': 'biryani',
	'yogurt': 'dahi',
	'lentil': 'dal',
	'steak': 'shami kebab',
	'dressing': 'chutney',
	'ground beef': 'beef keema',
	'soup': 'daal makhni',
	'wasabi': 'jalapeno',
	'olives': 'mushrooms',
	'squash': 'bhindi',
	'flour': 'chakki atta flour',
	'tea': 'chai',
	'coffee': 'chai',
	'salmon': 'shami kebab',
	'sugar': 'cheenee sugar',
	'salt': 'namak salt',
	'ranch': 'coriander chutney',
	'chuck roast': 'lamb kebab',
	'taco': 'roti',
	'burrito': 'naan',
	'sauce': 'chutney',

}



def IndianTransformToV2 (recipe):
	masala = random.choice(my_masalas)
	#recipe['Ingredients'].append({'Name': "Garam Masala", 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
	if not "frying pan" in recipe['Recipe']['Tools']:
		recipe['Recipe']['Tools'].append("frying pan")
	#recipe['Ingredients'].append({'Name': "Coriander Chutney", 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})

	cooked_val = 0
	#my_bread = ""
	#my_sauce = ""
	new_steps = recipe['Recipe']['Steps']
	#print(my_stuff)
	for key, value in recipe['Recipe'].items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				#print(ing)
				for key1, value1 in ing.items():
					#print(ings)
					if type(value1) == str:
						#print(value1)
						for x in my_breads:
							if x in value1.lower(): #replace bread with naan
								#print(x)
								ing[key1] = "naan"
								#recipe['Recipe']['Ingredients'].
								my_bread = x
						for x in my_sauces:
							if x in value1.lower():
								ing[key1] = "coriander chutney"
								my_sauce = x
						if "butter" in value1.lower():
							ing[key1] = "ghee"
						if "oil" == value1.lower():
							ing[key1] = "mustard oil"
						if "rice" in value1.lower():
							ing[key1] = "biryani"
							recipe['Recipe']['Ingredients'].append({'Name': "Biryani Masala", 'Quantity': 0.5, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
							new_steps.append('Before adding the biryani to your meal, fry the biryani masala for 10 minutes on medium heat. When finished, mix the fried masala with the biryani.')
		if key == "Steps":
			#print(new_steps)
			for step in new_steps:
				#for x in my_breads:
					#print(x)
				print(step)
				if my_bread in step.lower():
					#print(my_bread) 
					#step = step.replace(my_bread,"naan") 
					number = new_steps.index(step)
					#new_steps.remove(step) 
					#new_steps.insert(number, step.replace(my_bread,"naan"))
					#print(value)
				#for x in my_sauces:
					#if x in value2.lower():
						#value[key2] = value2.replace(x, "coriander chutney")
			for step in new_steps:
				if my_sauce in step.lower():
					#print(recipe['Recipe']['Steps'][1])
					#print(type(step))
					number = new_steps.index(step)
					#new_steps.remove(step)
					#new_steps.insert(number, step.replace(my_sauce,"coriander chutney"))
			for step in new_steps:
				if "butter" in step.lower():
					#print(recipe['Recipe']['Steps'][0])
					number = new_steps.index(step)
					new_steps.remove(step) 
					new_steps.insert(number, step.replace("butter","ghee"))
			for step in new_steps:
				if not "boil" in step.lower():
					if not "mustard oil" in step.lower():
						if "oil" in step.lower():
							number = new_steps.index(step)
							new_steps.remove(step) 
							new_steps.insert(number, step.replace("oil","mustard oil"))
			for step in new_steps:
				if "rice" in step.lower():
					number = new_steps.index(step)
					new_steps.remove(step) 
					new_steps.insert(number, step.replace("rice","biryani"))

	for methods in recipe['Recipe']['Methods']['Primary_cooking_method']: 
		if any (x in methods for x in cooking_methods):
			cooked_val = 1
	if cooked_val == 1:
		recipe['Recipe']['Ingredients'].append({'quantity': 0.5,'measurement': "cup", 'name': masala})
		new_steps.append('Take the .5 cups of ' + masala + ' masala and pour into the frying pan. Fry over medium heat in 3 tablespoons of mustard oil for 10 minutes until browning occurs.') 
		new_steps.append('When the ' + masala + ' masala is finished frying, mix it into the rest of the dish.')
		if not "frying pan" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append('frying pan')
		if not "fry" in recipe['Recipe']['Methods']["alternative_cooking_method"]:
			recipe['Recipe']['Methods']['alternative_cooking_method'].append('fry')
	if cooked_val == 0:
		recipe['Recipe']['Ingredients'].append({'Name': masala, 'quantity': 0.5, 'measurement': "cup"})
		recipe['Recipe']['Ingredients'].append({'Name': "Kabuli chana", 'Quantity': 1, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		#recipe['Ingredients'].append({'Name': "tomato ", 'Quantity': 1, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		if not "boiling pot" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("boiling pot")
		if not "bowl" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("bowl")
		if not "frying pan" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("frying pan")
		if not "wooden cooking spoon" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("wooden cooking spoon")
		if not "fry" in recipe['Recipe']['Methods']["alternative_cooking_method"]:
			recipe['Recipe']['Tools'].append("fry")
		if not "mustard oil" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Ingredients'].append({'Name': "Mustard Oil", 'Quantity': 3, 'Measurement': "tablespoon", 'Descriptor': "", 'Preparation': ""})
		#prev_steps = recipe['Recipe']['Steps']
		new_steps.append('Boil 1 cup of Kabuli chana over medium-high heat for 10 minutes. Once cooked, remove Kabuli chana from the pot and place into a bowl.')
		new_steps.append('Take the .5 cups of garam masala and pour into the frying pan. Fry over medium heat in 3 tablespoons of mustard oil for 10 minutes until browning occurs.')
		new_steps.append('Pour the fried Garam Masala mix into the bowl with the Kabuli channa and use the wooden spoon to mix together. Mix the Kabuli chana with the rest of your dish and enjoy!')

	#print(recipe['Recipe']['Steps'])
	recipe['Recipe'].pop("Steps", None)
	#new_steps.insert(recipe['Recipe']['Steps'])
	#print(new_steps)
	#print(prev_steps)
	recipe['Recipe']['Steps'] = new_steps

	return recipe


def IndianTransform (recipe):
	#PART 1

	print("\n*******************************")
	print("\nYour Indian recipe is coming right up!\n")
	print("Here are the transformations that were made to your recipe:")

	masala = random.choice(my_masalas)
	if not "frying pan" in recipe['Recipe']['Tools']:
		recipe['Recipe']['Tools'].append("frying pan")
		print("\n\tAdded frying pan to the list of tools")

	cooked_val = 0
	new_steps = recipe['Recipe']['Steps']

	indian = indian_subs.keys()
	for key, value in recipe['Recipe'].items():
		if key == 'Ingredients':
			for ing in value: # ing being the ingredient object
				for key1, value1 in ing.items():
					if key1 == 'name':
						for indian_item in indian:
							if indian_item in value1: #item-> unhealthy item, value1-> name of ing
								replacement = indian_subs[indian_item] #unhealthy item as a key
								number = recipe['Recipe']['Ingredients'].index(ing)
								recipe['Recipe']['Ingredients'][number][key1] = value1.replace(indian_item,replacement)
								#print("\n\tAdded " + my_meat + " to the list of ingredients")
								print("\n\tReplaced " + value1 + " in the list of ingredients with " + indian_subs[indian_item])
		num = 0
		if key == 'Steps':
			for step in new_steps:
				number = new_steps.index(step)
				temp = step
				for item in indian:
					if item in step:
						new_steps.remove(temp)
						new_steps.insert(number, temp.replace(item, indian_subs[item])) 
						temp = new_steps[number]
						num+=1
			print("\n\tChanged " + str(num) + " steps in the recipe")




	#PART 2: adding masala 
	for methods in recipe['Recipe']['Methods']['Primary_cooking_method']: 
		if any (x in methods for x in cooking_methods):
			cooked_val = 1
	if cooked_val == 1:
		recipe['Recipe']['Ingredients'].append({'quantity': '0.5','measurement': "cup", 'name': masala})
		new_steps.append('Take the .5 cups of ' + masala + ' masala and pour into the frying pan. Fry over medium heat in 3 tablespoons of mustard oil for 10 minutes until browning occurs.') 
		new_steps.append('When the ' + masala + ' masala is finished frying, mix it into the rest of the dish.')
		print("\n\tAdded 2 new steps to the recipe")
		if not "frying pan" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append('frying pan')
			print("\n\tAdded frying pan to the list of tools.")
		if not "fry" in recipe['Recipe']['Methods']["alternative_cooking_method"]:
			recipe['Recipe']['Methods']['alternative_cooking_method'].append('fry')
			print("\n\tAdded 'fry' to the list of methods")
	if cooked_val == 0:
		recipe['Recipe']['Ingredients'].append({'name': masala, 'quantity': '0.5', 'measurement': "cup"})
		print("\n\tAdded " + masala + " to the list of ingredients")
		recipe['Recipe']['Ingredients'].append({'name': "Kabuli chana", 'Quantity': '1', 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		print("\n\tAdded Kabuli chana to the list of ingredients")
		#recipe['Ingredients'].append({'Name': "tomato ", 'Quantity': 1, 'Measurement': "cup", 'Descriptor': "", 'Preparation': ""})
		if not "boiling pot" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("boiling pot")
			print("\n\tAdded boiling pot to the list of tools")
		if not "bowl" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("bowl")
			print("\n\tAdded bowl to the list of tools")
		if not "frying pan" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("frying pan")
			print("\n\tAdded frying pan to the list of tools")
		if not "wooden cooking spoon" in recipe['Recipe']['Tools']:
			recipe['Recipe']['Tools'].append("wooden cooking spoon")
			print("\n\tAdded wooden cooking spoon to the list of tools")
		if not "fry" in recipe['Recipe']['Methods']["alternative_cooking_method"]:
			recipe['Recipe']['Methods']['alternative_cooking_method'].append("fry")
			print("\n\tAdded 'fry' to the list of alternative cooking methods")
		#if not "mustard oil" in recipe['Recipe']['Ingredients']:
		num = 0
		for ing in recipe['Recipe']['Ingredients']:
			for key1, value1 in ing.items():
				if key1 == "name":
					if "mustard oil" == value1:
						num = 1
		if num == 0:
			recipe['Recipe']['Ingredients'].append({'quantity': '3', 'measurement': "tablespoon", 'name': "mustard oil"})
			print("\n\tAdded mustard oil to the list of ingredients")
		#prev_steps = recipe['Recipe']['Steps']
		new_steps.append('Boil 1 cup of Kabuli chana over medium-high heat for 10 minutes. Once cooked, remove Kabuli chana from the pot and place into a bowl.')
		new_steps.append('Take the .5 cups of ' +  masala + ' and pour into the frying pan. Fry over medium heat in 3 tablespoons of mustard oil for 10 minutes until browning occurs.')
		new_steps.append('Pour the fried Garam Masala mix into the bowl with the Kabuli channa and use the wooden spoon to mix together. Mix the Kabuli chana with the rest of your dish and enjoy!')
		print("\n\tAdded 3 new steps to the recipe")

	#print(recipe['Recipe']['Steps'])
	#recipe['Recipe'].pop("Steps", None)
	#new_steps.insert(recipe['Recipe']['Steps'])
	#print(new_steps)
	#print(prev_steps)
	recipe['Recipe']['Steps'] = new_steps

	return recipe


#print(VegetarianTransformTo(VegFrom))






# def main():

#print(IndianTransformToV2(ExampleRecipe2))







	

