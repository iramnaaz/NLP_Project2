from ingredient_scrape import RecipeFetcher
from ing_packer import make_ing_list

rf = RecipeFetcher()
meat_lasagna = rf.search_recipes('meat lasagna')[0]
res = rf.scrape_recipe(meat_lasagna)

ing_obj = make_ing_list(res['ingredients'])