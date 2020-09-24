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
#WILL MUTATE LIST IN PLACE
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


#USING A LIST AS A QUEUE
#-----------------------

queue = ['monkey', 'elephant', 'dinosaur', 'dragon', 'donkey']

#Using a deque constructor
from collections import deque
deq = deque(queue)
print(deq)

#Adding to back of queue
deq.append('hippo')
print(deq)

#Removing from front of queue
print(deq.popleft())
print(deq)

#Adding to front of the queue
deq.insert(0, 'ant')
print(deq)

#Removing from back of the queue
deq.pop()
print(deq)


#LISTS COMPREHENSION
#-------------------
#A concise way to create lists


#Finding the first 10 square nums usinf for loop
#leaves the variable x in memory after loop completion
def find_first_n_sq_nums(n):
    squares = []
    for x in range(n):
        squares.append(x**2)
    return squares

print(find_first_n_sq_nums(10))


#Finding the first 20 square nums using list() constructor
#and map(function, iterable)
def list_first_n_sq_nums(n):
    return list(map(lambda x: x**2, range(n)))

print(list_first_n_sq_nums(20))


#Finding the first 20 square nums list comprehension
squares = [x**2 for x in range(20)]
print(squares)


#Chaining together multiple for and if clauses
l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 2, 7, 4]
same_combos = [(x, y) for x in l1 for y in l2 if x == y]
print(same_combos)


#The above is the same as saying:
def nested_same_combos(l1, l2):
    pairs = []
    for x in l1:
        for y in l2:
            if x == y:
                pairs.append((x, y))
    return pairs
print(nested_same_combos(l1, l2))


#Flattening listcomp
listcomp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for l in listcomp for num in l]
print(flattened)


#Transposing a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

#Nested for loop
def transpose(matrix):
    transposed = []
    for i in range(len(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed
        
print(transpose(matrix))


#Nested listcomp
def nested_transpose(matrix):
    transposed = []
    for i in range(len(matrix)):
        transposed.append([row[i] for row in matrix])
    return transposed

print(nested_transpose(matrix))


#Nested listcomp
transposed = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transposed)


#BUBBLE SORT ALGORITHM
#---------------------
def bubble_sort(numbers):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                prev = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = prev     
                sorted = False
    return numbers


#BINARY SEARCH ALGORITHM
#-----------------------
def binary_search(list, target):
    start = 0
    end = len(list)-1

    while start <= end:
        mid = start + end
        if list[mid] == target:
            return mid

        if list[mid] > target:
            end = mid - 1
        elif list[mid] < target:
            start = mid + 1

    return None

example_list = [1, 2, 3, 4, 5, 7, 12, 26, 18]
print(binary_search(example_list, 7)) 


#     SETS
#---------------

