from optional_transformation_list import original_to_chinese_recipe_ing, original_to_chinese_utensils



original_to_chinese_recipe_ing = {
    "tofu": "mapo tofu",
    "white rice": "jasmine scented rice",
    'rice': 'Yangchow fried rice',
    "corn": "bok choy",
    "ice cream": "baobing",
    "tea": "chinese tea",
    "sausage": "lap ceung",
    "salsa" : "mala sauce",
    'potato': 'taro root',
    "maple sauce" : "mala sauce",
    "maple syrup" : "chinese mala syrup",
    "spaghetti pasta": "lo mein",
    "spaghetti": "lo mein",
    "vinegar": "black vinegar",
    "red pepper flakes": "dried chili flakes",
    'pepper': 'tien tsin pepper',
    "italian parsley": "cilantro",
    "parmigiano-reggiano cheese": "fermented bean curd",
    "pasta": "lo mein",
    "noodles": "lo mein",
    "mushrooms": "shiitake mushrooms",
    "salad": "malatang",
    "quesadilla": "xian bing",
    "Burger": "chinese hamburger",
    "french pancake": "jian bing",
    "meat sauce": "da lu mian",
    "churro": "you tiao",
    "pizza": "scallion pancake",
    "wine": "shaoxing wine",
    "olive oil": "peanut oil",
    "burger": " chinese burger",
    "vegetable oil": "peanut oil",
    "canola oil": "peanut oil",
    "peanut oil": "peanut oil",
    "coconut oil": "peanut oil",
    "corn oil": "peanut oil",
    "sunflower oil": "peanut oil",
    "safflower oil": "peanut oil",
    "chicken nuggets": "chicken balls",
    "chicken": 'orange chicken',
    "jerky": "bak kwa",
    "tofu": "mapo doufu",
    "meat": "bakkwa",
    "lamb": "lamb broth",
    "pasta": "lo mein",
    "sauce": "hoisin sauce",
    "shrimp": "cha jang mein",
    "dressing": 'ginger dressing',
    'beef': 'mongolian beef',
    'pork': 'moo shu pork',
    'duck': 'peking roasted duck',
    'shrimp': 'fried shrimp with cashew nuts',
    'lettuce': 'stir-fried garlic lettuce',
    'eggplant': 'japanese eggplant',
    'cabbage': 'chinese cabbage',
    'bean': 'yardlong bean',
    'radish': 'daikon radish',
    'arugla': 'mizuna',
    'romaine': 'lemongrass',
    'spinach': 'water spinach',
    'celery': 'leaf celery',
    'bread': 'mantou',
    'cheese': 'ginger root',
    'onion': 'green onion',
    




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




def transformation_to_chinese(recipe):

    chinese = original_to_chinese_recipe_ing.keys() #list of unhealthy items (keys)
    new_steps = recipe['Recipe']['Steps']
    for key, value in recipe['Recipe'].items():
        if key == 'Ingredients':
            for ing in value: # ing being the ingredient object
                for key1, value1 in ing.items():
                    #print(value1)
                    if key1 == 'name':
                        #print(value1)
                        for chinese_item in chinese:
                            if chinese_item in value1: #item-> unhealthy item, value1-> name of ing
                                replacement = original_to_chinese_recipe_ing[chinese_item] #unhealthy item as a key
                                number = recipe['Recipe']['Ingredients'].index(ing)
                                recipe['Recipe']['Ingredients'][number][key1] = value1.replace(chinese_item,replacement)


        if key == 'Steps':
            for step in new_steps:
                number = new_steps.index(step)
                temp = step
                for item in chinese:
                    if item in step:
                        new_steps.remove(temp)
                        new_steps.insert(number, temp.replace(item, original_to_chinese_recipe_ing[item])) 
                        temp = new_steps[number]
    return recipe


    #print("The Original Recipe------->")
    # for dir in directions:
    #     print(" *", dir)
    # print("\n\n")
    # print("***************************************** ")
    # print("Transformed Chinese Recipe")
    # transformed_to_chinese = changed_instructions(directions, original_to_chinese_recipe_ing)
    # transformed_to_chinese = changed_instructions(transformed_to_chinese, original_to_chinese_utensils)
    # print("\n * ".join(transformed_to_chinese))
    # print(" ** " + "Pour the particles of cassia powder and chinese cinammon into the dish")
    # print(" ** " + "Then add the hoisin sauce for more taste")
    # print(" ** " + "Toast it with the baijiu and your chinese dish is now ready")
    # print("\n\n")


def changed_instructions(directions, replace_with):
    new_updated_directory = []
    for dir in directions:
        list_directions = dir.split(" ")
        for ingredient in replace_with:
            for i in range(1, len(list_directions)):
                if (list_directions[i - 1].lower() + " " + list_directions[i].lower()) == ingredient:
                    list_directions[i - 1] = replace_with[ingredient]
                    list_directions[i] = ''

                elif (list_directions[i - 1].lower() + " " + list_directions[i].lower()) == (ingredient + ','):
                    list_directions[i - 1] = replace_with[ingredient] + ','
                    list_directions[i] = ''

                elif (list_directions[i - 1].lower() + " " + list_directions[i].lower()) == (ingredient + ';'):
                    list_directions[i - 1] = replace_with[ingredient] + ';'
                    list_directions[i] = ''

                elif list_directions[i - 1].lower() == ingredient:
                    list_directions[i - 1] = replace_with[ingredient]

                elif list_directions[i - 1].lower() == (ingredient + ','):
                    list_directions[i - 1] = replace_with[ingredient] + ','

                elif list_directions[i - 1].lower() == (ingredient + ';'):
                    list_directions[i - 1] = replace_with[ingredient] + ';'

                if i == len(list_directions) - 1:
                    if list_directions[i].lower() == ingredient:
                        list_directions[i] = replace_with[ingredient]

        new_directions = " ".join(list_directions)
        new_updated_directory.append(new_directions)
        #print(new_updated_directory)
    return new_updated_directory

#print(transformation_to_chinese(ExampleRecipe))
