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
-> Transform to Unhealthy
-> Transform to Chinese
-> Transform to Indian
-> Scale by a multiplier

Steps:

We have first done the data analysis of most common ingredients which is used in the top recipes from AllRecipes.com website. 
We then created the parsers for ingredients, tools, methods, nutrients and steps(directions).

Transformations:
We have given the following options to a user to choose from:

Transform to Vegetarian, Transform to Non-Vegetarian, Transform to Healthy, Transform to Chinese,Transform to Indian, Scale by a Multiplier, Transform to Gluten-Free, Transform to Vegan, Transform to Pescatarian, Transform from Pescatarian

Main program:
The main file has a user interface that allows the user to determine what the program should do. It call methods in transform and parse to get the recipes/data and print out the recipe(s) in a human-friendly format (to the console).

Instructions for running our recipe parser and transformations and viewing the output:
1. Open the terminal and run the command: python3 main_file.py
2. Follow the prompt to enter your URL and choose your transformation(s)
3. Once you enter your designated inputs, you should be able to view the original parsed recipe and the transformed recipe!

Thank You!
