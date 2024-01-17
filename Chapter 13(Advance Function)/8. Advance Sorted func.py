# Advance Sorted() function
# With List()
fruits = ['Grapes', 'Mango', 'Apple']
fruits.sort()    #List has its own sort method for sorting in alphabetically
print(fruits)


# With Tuple()
# NOTE - Tuple has no sorted method because it immutable
# with the sorted function in tuple. soretd function catch all the item form tuple
# and make a sorted list.
fruits_2 = ('Grapes', 'Mango', 'Apple')
# fruits2.sort()    #Does not work
sort_tuple = sorted(fruits_2)    # Make their own another list
print(sort_tuple)


# With Set()
# NOTE - Smae as tuple
fruits_3 = {'Grapes', 'Mango', 'Apple'}
# fruits_3.sort()    # Does not work
sort_set = sorted(fruits_3)
print(sort_set)




bikes = [
    {'model': 'Honda cd70', 'Price': 70000 },
    {'model': 'Yamaha YBR 150', 'Price': 190000},
    {'model': 'Honda cd125', 'Price': 125000},
]

_sort_ = sorted(bikes, key= lambda a: a['Price'], reverse=True)
print(_sort_)