# NLP_Project2
Repository for projects undertaken in the course ' Natural Language Processing ' at Northwestern University

Team Members:
1)Iram Naaz Khan
2)Swapnanil Deb
3)Hadi Shiraz
4)Zachary Kornbluth

Steps to Run:
To run the code, clone the repo and you can see main.py file.
If required then create a virtual environment and activate it
$ pip install -r requirements.txt
To get a menu interface Run main.py

Menu
-> To view the scraped data, Ingredients, Tools, Methods, Steps and nutrients
-> Transform to Vegetarian
-> Transform to Non-Vegetarian
-> Transform to Healthy
-> Transform to Chinese
-> Transform to Indian
-> Scale by a multiplier

Steps:

We have first done the data analysis of most common ingredients which is used in the top recipes from AllRecipes.com website. 
We then created the parsers for ingredients, tools, methods, nutrients and steps(directions).

Transformations:
We have given the following options to a user to choose from:

Transform to Vegetarian, Transform to Non-Vegetarian, Transform to Healthy, Transform to Chinese,Transform to Indian, Scale by a multiplier.

Main program:
The main have a user interface to determines what the user wants the program to do. It call methods in transform and parse to get the recipes/data and print out the recipe(s) in a human-friendly format (to the console).

Thank You!
