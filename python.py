# print('Hello World!')

#Print statement print(value, end='')
l = [1, 2, 3, 4]
print(l)
print(len(l))

#Fibonnaci Sequence
a , b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

#For statements
l = ['the', 'cat', 'in', 'the', 'hat']
for w in l:
    print(w, len(w))

# #Range function range(start, end, step)
n = 100
for i in range(50, n, 2):
    print(i)

# #Range function range(length)
for i in range(10):
    if i % 2 == 0:
        print(i)

# #Iterating over a list using range and len
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(l)):
    if i % 2 == 0:
        print(l[i])

l = ['spiderman', 'ironman', 'thor', 'hulk', 'captain america']
for i in range(len(l)):
    if i % 2 != 0:
        print(l[i])

#List keyword
print(list(range(4)))

#If and else if statements
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(l)):
    if i == 0:
        print('zero')
    elif i % 2 == 0:
        print('even')
    else:
        print('odd')

#Defining a function
def fibs(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b

fibs(10)

#Returning a list
def fibs2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fibs2(n))

#Default args. Defaults will only be evaluated once
def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) #[1]
print(f(2)) #[1, 2]
print(f(3)) #[1, 2, 3]

#Default args. If you do not want default shared between subsequent calls:
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1)) #[1]
print(f2(2)) #[2]
print(f2(3)) #[3]

#"Splat"? operator for parameters
def cheeseshop(*cheese):
    for c in cheese:
        print(c)

print(cheeseshop('brie', 'cheddar', 'swiss', 'mozzerella'))

#Any formal parameters after *args are keyword only parameters
def concat(*args, sep='/'):
    return sep.join(args)

print(concat('mercury', 'venus', 'earth', 'mars'))

#Iteration
l = [1, 3, 2, 5, 6, 7, 8, 12, 13, 15, 16]
def iterate(l):
    nl = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            nl.append(l[i])
    return nl

print(iterate(l)) #[2, 6, 8, 12, 16]

l = [1, 3, 2, 5, 6, 7, 8, 12, 13, 15, 16]
def iterate2(l):
    nl = []
    for i in l:
        if i % 2 == 0:
            nl.append(i)
    return nl

print(iterate2(l)) #[2, 6, 8, 12, 16]

#Unpacking argument lists with * operator
l = [2, 10]
print(list(range(*l)))

#Delivering keyword args via dictionary
d = {'voltage': '4 million volts', 'state': 'fried', 'action': 'zapped'}
def computer(voltage, state='fine', action='powered on'):
    print('This computer just ate ' + voltage)
    print('now, its ' + state + ' and ' + action, end='. ')

computer(**d)
computer('500 volts') 

#Lambda Expression / Anonymous (nameless) Functions

#Saving lambda function to variable for use
g = lambda x: 3*x + 2
print(g(2)) 

#Basic use of lambda function
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(1)
print(f(1)) #2
print(f(50)) #51

#Using lambda to sort by each pairs index 1 alphabetically
pairs = [(5, 'five'), (4, 'four'), (8, 'eight'), (1, 'one')]
print(pairs)
pairs.sort(key=lambda pair: pair[1])
print(pairs)

#Using lambda to sort list of names alpgabetically by last name
authors = ['JR Tolkien', 'JK Rowling', 'Tennesse Williams', 'Junie B Jones', 'Topsy Krett']
print(authors)
authors.sort(key=lambda name: name.split()[-1])
print(authors)

#Proper documentation strings
def find_sum(n, i):
    """This function returns sum of two numbers
    """
    return n+i

print(find_sum(9, 7))




