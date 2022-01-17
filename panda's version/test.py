import random

item_chances = {
    'item_1': 95,
    'item_2': 95,
}





for i in range(100):
	selected = random.choices(
    list(item_chances.keys()), weights=list(item_chances.values()), k=1)
	print(selected)


#for item in set(selected):
#    print(f'{item}: {selected.count(item)}')