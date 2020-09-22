#COMMON USEFUL LIST METHODS
#----------------------------

#append - adds an item to the end of the list
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.append('giraffe')
print(l) #l = ['donky', 'dragon', 'dinosaur', 'elephant', 'monkey', 'giraffe']

#extend - extends a list with all items from iterable
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.extend(['giraffe', 'unicorn', 'hippogriff'])
#l = ['donky', 'dragon', 'dinosaur', 'elephant', 'monkey', 'giraffe', 'unicorn', 'hippogriff']
print(l)

#insert - insert(i, x) where i is index to insert, and x is value. Will error if value not found
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.insert(2, 'troll')
print(l)

#remove - remove(x) removes the first item in the list whose value == x
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.remove('elephant')
print(l)

#pop - pop(i) removes the item at the given position and returns it.
#if no value is given pop(), will default to last item
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
print(l.pop(1))
print(l.pop())

#clear - removes all items from the list
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.clear()
print(l)