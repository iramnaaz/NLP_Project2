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
    'sugar': 'artificial sweetner',
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
    'namak': "garlic"





}

ExampleRecipe = {
    'Ingredients':
        [{
        'Name': 'chicken',
        'Quantity': 4,
        'Measurement': 'pound',
        'Descriptor': '',
        'Preparation':'cut into pieces',
        'Tags': ''
        },
        {
        'Name': 'buttermilk',
        'Quantity': 1,
        'Measurement': 'cups',
        'Descriptor': '',
        'Preparation':'',
        'Tags': ''
        },
        {
        'Name': 'all-purpose flour',
        'Quantity': 2,
        'Measurement': 'cups',
        'Descriptor': '',
        'Preparation':'',
        'Tags': ''
        },
        {
        'Name': 'paprika',
        'Quantity': 1,
        'Measurement': 'teaspoon',
        'Descriptor': '',
        'Preparation':'',
        'Tags': ''
        },
        {
        'Name': 'vegetable oil',
        'Quantity': 2,
        'Measurement': 'quarts',
        'Descriptor': '',
        'Preparation':'',
        'Tags': ''
        }
        ],
        'Tools': ['plastic bag', 'knife', 'teaspoon'],
        'Methods': [''],

        'Steps':
            {'Step 1': 'Take your cut up chicken pieces and skin them if you prefer. Put the flour in a large plastic bag (let the amount of chicken you are cooking dictate the amount of flour you use). Season the flour with paprika, salt and pepper to taste (paprika helps to brown the chicken).',
            'Step 2': 'Dip chicken pieces in buttermilk then, a few at a time, put them in the bag with the flour, seal the bag and shake to coat well. Place the coated chicken on a cookie sheet or tray, and cover with a clean dish towel or waxed paper. LET SIT UNTIL THE FLOUR IS OF A PASTE-LIKE CONSISTENCY. THIS IS CRUCIAL!',
            'Step 3': 'Fill a large skillet (cast iron is best) about 1/3 to 1/2 full with vegetable oil. Heat until VERY hot. Put in as many chicken pieces as the skillet can hold. Brown the chicken in HOT oil on both sides. When browned, reduce heat and cover skillet; let cook for 30 minutes (the chicken will be cooked through but not crispy). Remove cover, raise heat again and continue to fry until crispy.',
            'Step 4': 'Drain the fried chicken on paper towels. Depending on how much chicken you have, you may have to fry in a few shifts. Keep the finished chicken in a slightly warm oven while preparing the rest.'
            }
}

def HealthyTransformTo (recipe):
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


        if key == 'Steps':
            for step in new_steps:
                number = new_steps.index(step)
                temp = step
                for item in unhealthy:
                    if item in step:
                        new_steps.remove(temp)
                        new_steps.insert(number, temp.replace(item, substitutions[item])) 
                        temp = new_steps[number]
    return recipe

def DoubleOrHalf (recipe, multiplier):
    # Input is a recipe and a multiplier, output is the recipe with each ingredient scalled by that multiplier
    # For example, if the multiplier is 2 each ingredient in the returned recipe will have double the quantity of the initial recipe
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
