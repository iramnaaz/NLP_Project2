import re

def make_ing_list(ingredients):
	ingredient_list = []
	for ing in ingredients:
		ing_obj = ing_parse(ing)
		ingredient_list.append(ing_obj)
	return ingredient_list

def ing_parse(ingredient):
	x = {}
	temp = re.findall(r'\d*\/\d*|\d*\.\d+|\d+', ingredient) 
	print(ingredient)
	print(temp)
	num = ''
	if len(temp) == 0:
		num = ''
	else:
		num = str(num_check(list(map(str, temp))[0]))
	print(num)
	return x;

def num_check(num):
	if '/' in num:
		s = num.split('/')
		x = int(s[0])/int(s[1])
		return x
	else:
		return int(num)