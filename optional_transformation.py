from optional_transformation_list import original_to_chinese_recipe_ing, original_to_chinese_utensils


def transformation_to_chinese(directions):
    print("The Original Recipe------->")
    for dir in directions:
        print(" *", dir)
    print("\n\n")
    print("***************************************** ")
    print("Transformed Chinese Recipe")
    transformed_to_chinese = changed_instructions(directions, original_to_chinese_recipe_ing)
    transformed_to_chinese = changed_instructions(transformed_to_chinese, original_to_chinese_utensils)
    print("\n * ".join(transformed_to_chinese))
    print(" ** " + "Pour the particles of cassia powder and chinese cinammon into the dish")
    print(" ** " + "Then add the hoisin sauce for more taste")
    print(" ** " + "Toast it with the baijiu and your chinese dish is now ready")
    print("\n\n")


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
