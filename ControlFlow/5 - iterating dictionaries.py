# 1. Iterating through dictionaries
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for food in basket_items:
   if food in fruits:
       result += basket_items[food]



# Solution:
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for object, count in basket_items.items():
   if object in fruits:
       result += count
print("There are {} fruits in the basket.".format(result))
