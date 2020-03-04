from usda import UsdaClient
import random
client = UsdaClient('rfMvRseGhasTej6Ogcpj5gxidNqUtckuXjJIcOcM')

non_healthy_foods = ['buttermilk']
healthy_foods = ['skim milk']

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
	my_sub = random.choice(healthy_foods)
	for key, value in recipe.items():
		if key == "Ingredients":
			for ing in value: #value is array, ing are the ingrediants
				for key1, value1 in ing.items():
					if type(value1) == str:
						foods_search = client.search_foods(value1, 1)
						my_food = next(foods_search)
						report = client.get_food_report(my_food.id)
						my_string = report.food.name.lower()
						if any(x in value1 for x in meats): #replace value1 with my_stirng if you want to use usda lib
							ing[key1] = my_sub
		if key == "Steps":
			for key2, value2 in value.items():
				for x in non_healthy_foods:
					if x in value2:
						value[key2] = value2.replace(x, my_sub)


	return recipe

def main():
	print(HealthyTransformTo(ExampleRecipe))
