from usda import UsdaClient
client = UsdaClient('rfMvRseGhasTej6Ogcpj5gxidNqUtckuXjJIcOcM')

foods_search = client.search_foods('coffee, instant, regular, prepared with water', 1)
coffee = next(foods_search)

report = client.get_food_report(coffee.id)
print(report.food)
print(report.food_group)
print(report.nutrients)
print(dir(report))