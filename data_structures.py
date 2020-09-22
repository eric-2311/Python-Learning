#COMMON USEFUL LIST METHODS
#----------------------------

#append - append(x) adds an item to the end of the list
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.append('giraffe')
print(l) #l = ['donky', 'dragon', 'dinosaur', 'elephant', 'monkey', 'giraffe']


#extend - extend(iterable) extends a list with all items from iterable
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.extend(['giraffe', 'unicorn', 'hippogriff'])
#l = ['donky', 'dragon', 'dinosaur', 'elephant', 'monkey', 'giraffe', 'unicorn', 'hippogriff']
print(l)


#insert - insert(i, x) where i is index to insert, and x is value. Will error if value not found
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.insert(2, 'troll')
print(l) #['donkey', 'dragon', 'troll', 'elephant', 'monkey']


#remove - remove(x) removes the first item in the list whose value == x
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.remove('elephant')
print(l) #['donkey', 'dragon', 'dinosaur', 'monkey']


#pop - pop(i) removes the item at the given position and returns it.
#if no value is given pop(), will default to last item
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
print(l.pop(1)) #'dragon'
print(l.pop()) #'monkey'


#clear - removes all items from the list
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.clear()
print(l) #[]


#index - index(x) returns 0 based index of list where value == x
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
print(l.index('dragon')) #1


#count - count(x) returns number of times x appears in list
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey', 'monkey']
print(l.count('monkey')) #2


#sort - sort(key=None, reverse=False) sorts list based on criteria
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.sort()
print(l) #['dinosaur', 'donkey', 'dragon', 'elephant', 'monkey']

l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.sort(reverse=True)
print(l) #['monkey', 'elephant', 'dragon', 'donkey', 'dinosaur']

l = [5, 3, 7, 9, 2, 1, 0, 4, 12]
l.sort()
print(l) #[0, 1, 2, 3, 4, 5, 7, 9, 12]


#reverse - reverses items of the list in place
l = ['donkey', 'dragon', 'dinosaur', 'elephant', 'monkey']
l.reverse()
print(l) #['monkey', 'elephant', 'dinosaur', 'dragon', 'donkey']


#copy - returns a shallow copy of the list
l = ['monkey', 'elephant', 'dinosaur', 'dragon', 'donkey']
print(l.copy()) #['monkey', 'elephant', 'dinosaur', 'dragon', 'donkey']


#USING A LIST AS A STACK
#-----------------------

stack = ['monkey', 'elephant', 'dinosaur', 'dragon', 'donkey']

#Stack from back to front
#------------------------
#Adding item to back of the stack
def add_to_stack(x):
    stack.append(x)
    return stack

print(add_to_stack('whale')) #['monkey', 'elephant', 'dinosaur', 'dragon', 'donkey', 'whale']

#Removing item from back of stack
def remove_from_stack():
    return stack.pop()

print(remove_from_stack())
print(stack)

#Peeking from end of stack
def peek():
    return stack[-1]

print(peek())


#Stack from front to back
#------------------------
#Adding item to front of stack
def add_to_stack2(x):
    stack.insert(0, x)
    return stack

print(add_to_stack2('bulbasaur'))

#Removing item from front of stack
def remove_from_stack2():
    return stack.pop(0)

print(remove_from_stack2())
print(stack)

#Peeking at start of stack
def peek2():
    return stack[0]

print(peek2())