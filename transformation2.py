from usda import UsdaClient
import random
client = UsdaClient('rfMvRseGhasTej6Ogcpj5gxidNqUtckuXjJIcOcM')

non_healthy_foods = ['buttermilk']
healthy_foods = ['skim milk']

#incldue plurals or larger words that contain others before their counterparts 
substitutions = {
    'butter': 'margarine',
    'egg': 'egg white',
    'buttermilk': 'skim milk',
    'milk': 'almond milk',
    'bacon': 'turkey bacon',
    'white rice': 'brown rice',
    'chocolate': 'dark chocolate',
    'couscous': 'quinoa',
    'crouton': 'mixed nut',
    'cream': 'coconut milk',
    'flour tortilla': 'corn tortilla',
    'frosting': 'meringue',
    'sour cream': 'fat-free yogurt',
    'flour': 'whole wheat flour',
    'ground beef': 'ground turkey',
    'bread': 'whole wheat bread',
    'sugar': 'stevia',
    'potato': 'cauliflower',
    'mayonnaise': 'hummus',
    'mayo': 'hummus',
    'tomato': "red pepper",
    'bean': 'soy bean',
    'noodle': 'zuchinni noodle',
    'pasta': 'Quinoa pasta',
    'cheese': 'low-fat cheese',
    'thigh': 'breast', 
    'beef': 'lean beef',
    'pork': 'turkey',
    'sausage': 'chicken', 
    'oil': 'organic oil',
    'mustard': 'horseradish',
    'ranch dressing': 'sliced avocado', 
    'jam': 'fresh strawberry',
    'peanut butter': 'tahini',
    'pancake': 'whole wheat coconut pancake', 
    'black pepper': 'cayenne pepper',
    'butter': 'low-fat greek yogurt',
    'biscuit': "granola",
    'salt': "garlic",
    'namak': "garlic",





}

substitutions1 = {
	

	'lettuce': 'butter arugula',
	'tomato': 'potato',
	'apple': 'pineapple',
	'peach': 'mango',
	'orange': 'mango',
	'cantaloupe': "watermelon",
	'kiwi': 'watermelon',
	'bread': 'white bread',
	'toast': 'texas toast',
	'chicken': 'beef',
	'turkey': 'salami',
	'wheat bread': 'buttered bun',
	'milk': 'whole milk',
	'bacon': 'smoked bacon',
	'pancake': 'chocolate chip pancake',
	'egg': 'egg yolk',
	'butter': 'salted butter',
	'skim milk': 'whole milk',
	'chocolate': 'milk chocolate',
	'rice': 'white rice',
	'cream': 'heavy whipping cream',
	'flour': 'high gluten flour',
	'cauliflower': 'potato',
	'cabbage': 'corn',
	'oil' : 'canola oil',
	'strawberry': 'jam',
	'breast': 'thigh',
	'nut': 'crouton',
	'guacamole': 'dressing',
	'chips': 'fries',
	'beef': 'corned beef',
	'pheasant': 'duck',
	'lamb': 'ham',
	'veal': 'prosciutto',
	'yogurt': 'creamy yogurt',
	'sugar': 'white sugar',
	'honey': 'raw sugar',
	'syrup': 'white sugar',
	'onion': 'onion ring',
	'cheese': 'sweetened cottage cheese',
	'pepper': 'hot pepper',







}



def HealthyTransformTo (recipe):

    print("\n*******************************")
    print("\nYour healthy recipe is coming right up!\n")
    print("Here are the transformations that were made to your recipe:")

    unhealthy = substitutions.keys() #list of unhealthy items (keys)
    new_steps = recipe['Recipe']['Steps']
    for key, value in recipe['Recipe'].items():
        if key == 'Ingredients':
            for ing in value: # ing being the ingredient object
                for key1, value1 in ing.items():
                    #print(value1)
                    if key1 == 'name':
                        #print(value1)
                        for unhealthy_item in unhealthy:
                            if unhealthy_item in value1: #item-> unhealthy item, value1-> name of ing
                                replacement = substitutions[unhealthy_item] #unhealthy item as a key
                                number = recipe['Recipe']['Ingredients'].index(ing)
                                recipe['Recipe']['Ingredients'][number][key1] = value1.replace(unhealthy_item,replacement)
                                print("\n\tReplaced " + value1 + " with " + substitutions[unhealthy_item])


        if key == 'Steps':
            num = 0
            for step in new_steps:
                number = new_steps.index(step)
                temp = step
                for item in unhealthy:
                    if item in step:
                        new_steps.remove(temp)
                        new_steps.insert(number, temp.replace(item, substitutions[item])) 
                        temp = new_steps[number]
                        num+=1
            print("\n\tChanged " + str(num) + " steps in the recipe")
    return recipe

def UnhealthyTransform (recipe):

	print("\n*******************************")
	print("\nYour unhealthy recipe is coming right up!\n")
	print("Here are the transformations that were made to your recipe:")
	healthy = substitutions1.keys()
	new_steps = recipe['Recipe']['Steps']
	for key, value in recipe['Recipe'].items():
		if key == 'Ingredients':
			for ing in value: # ing being the ingredient object
				for key1, value1 in ing.items():
					if key1 == 'name':
						for healthy_item in healthy:
							if healthy_item in value1: #item-> unhealthy item, value1-> name of ing
								replacement = substitutions1[healthy_item] #unhealthy item as a key
								number = recipe['Recipe']['Ingredients'].index(ing)
								recipe['Recipe']['Ingredients'][number][key1] = value1.replace(healthy_item,replacement)
								print("\n\tReplaced " + value1 + " with " + substitutions1[healthy_item])
		if key == 'Steps':
			num = 0
			for step in new_steps:
				number = new_steps.index(step)
				temp = step
				for item in healthy:
					if item in step:
						new_steps.remove(temp)
						new_steps.insert(number, temp.replace(item, substitutions1[item])) 
						temp = new_steps[number]
						num+=1
			print("\n\tChanged " + str(num) + " steps in the recipe")

	return recipe


def DoubleOrHalf (recipe, multiplier):
    # Input is a recipe and a multiplier, output is the recipe with each ingredient scalled by that multiplier
    # For example, if the multiplier is 2 each ingredient in the returned recipe will have double the quantity of the initial recipe
    
    print("\n*******************************")
    print("\nYour differently sized recipe is coming right up!\n")

    for key, value in recipe['Recipe'].items():
        if key == 'Ingredients':
            for ing in value: #ing is type dict, value is type array
                #print(int(ing['quantity']))
                for key1, value1 in ing.items():
                    if key1 == 'quantity':
                        x = 0 
                        try:
                            ing['quantity'] = str(int(value1) * multiplier) 
                        except:
                            ing['quantity'] = str(multiplier) + "*" + value1


    #look at seconds, minutes, hrs and multilpy
                #x = float(ing['quantity'])
                #y = x * multiplier 
                #ing['quantity'] = str(y)

    return recipe


gluten_free_subs = {
    

    'pasta': 'corn noodles',
    'semolina': 'polenta',
    'bulgur': 'rice',
    'couscous': 'quinoa',
    'wheat bran': 'gluten-free oat bran',
    'bread': 'gluten-free bread',
    'cereal': 'corn flakes',
    'granola': 'gluten-free granola mix',
    'ovaltine': 'cocoa',
    'beer': 'gluten-free beer',
    'wheat': 'almond flour',
    'rye': 'almond flour',
    'barley': 'almond flour',
    'pasta': 'chickpea pasta',
    'noodle': 'soba noodle',
    'cracker': 'gluten-free cracker',
    'cake': 'coconut flour cake',
    'pancake': 'coconut flour pancake',
    'soy sauce': 'coconut aminos sauce',
    'tortilla': 'raw spinach rap'

}


vegan_subs = {
    
    'milk': 'oak milk',
    'cheese': 'almond cheese',
    'mozzarella': 'daiya',
    'blue': 'herb cashew',
    'ricotta': 'almond',
    'egg': 'siken tofu',
    'chicken': 'tempeh',
    'beef': 'seitan',
    'turkey': 'tofu',
    'steak': 'seitan',
    'shrimp': 'legumes',
    'tilapia': 'jackfruit',
    'fish': 'tempeh',
    'meat': 'tofu',
    'salmon': 'tofu',
    'lamb': 'seitan',
    'pork': 'seitan',
    'veal': 'tempeh',
    'meat': 'tempeh',
    'anchovies': 'tofu',
    'squid': 'mushrooms',
    'scallops': 'zucchini',
    'calamari': 'mushrooms',
    'mussels': 'mushrooms',
    'crab': 'tempeh',
    'lobster': 'seitan',
    'yogurt': 'soy yogurt',
    'butter': 'margarine',
    'cream': 'cashew cream',
    'honey': 'maple syrup',
    'noodle': 'zucchini noodle',
    'pasta': 'spaghetti squash',
    'spaghetti': 'spaghetti squash',
    'sausage': 'vegan sausage'

}


def GlutenFreeTransform(recipe):

    GlutenFree = gluten_free_subs.keys() #list of unhealthy items (keys)
    new_steps = recipe['Recipe']['Steps']
    for key, value in recipe['Recipe'].items():
        if key == 'Ingredients':
            for ing in value: # ing being the ingredient object
                for key1, value1 in ing.items():
                    #print(value1)
                    if key1 == 'name':
                        #print(value1)
                        for glutenfree_item in GlutenFree:
                            if glutenfree_item in value1: #item-> unhealthy item, value1-> name of ing
                                replacement = gluten_free_subs[glutenfree_item] #unhealthy item as a key
                                number = recipe['Recipe']['Ingredients'].index(ing)
                                recipe['Recipe']['Ingredients'][number][key1] = value1.replace(glutenfree_item,replacement)


        if key == 'Steps':
            for step in new_steps:
                number = new_steps.index(step)
                temp = step
                for item in GlutenFree:
                    if item in step:
                        new_steps.remove(temp)
                        new_steps.insert(number, temp.replace(item, gluten_free_subs[item])) 
                        temp = new_steps[number]
    return recipe
                  


def VeganTransform(recipe):

    vegan = vegan_subs.keys() #list of unhealthy items (keys)
    new_steps = recipe['Recipe']['Steps']
    for key, value in recipe['Recipe'].items():
        if key == 'Ingredients':
            for ing in value: # ing being the ingredient object
                for key1, value1 in ing.items():
                    #print(value1)
                    if key1 == 'name':
                        #print(value1)
                        for vegan_item in vegan:
                            if vegan_item in value1: #item-> unhealthy item, value1-> name of ing
                                replacement = vegan_subs[vegan_item] #unhealthy item as a key
                                number = recipe['Recipe']['Ingredients'].index(ing)
                                recipe['Recipe']['Ingredients'][number][key1] = value1.replace(vegan_item,replacement)

        if key == 'Steps':
            for step in new_steps:
                number = new_steps.index(step)
                temp = step
                for item in vegan:
                    if item in step:
                        new_steps.remove(temp)
                        new_steps.insert(number, temp.replace(item, vegan_subs[item])) 
                        temp = new_steps[number]

    return recipe
                  






#print(HealthyTransformTo(ExampleRecipe))
#print(DoubleOrHalf(ExampleRecipe, 0.5))
