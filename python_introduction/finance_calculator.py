#I want to know if an item is on the shoppin list

item_shop = ["apple","orange","grape"]
item_found = False

while not item_found:
 item = input("Find Item (use q to exit)").lower()
 if item == "q":
  break
 if item in item_shop:
    item_found = True
    print(f"{item} is in the shopping list")
 else: 
   print(f"{item} not on the list")      