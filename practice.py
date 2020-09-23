# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square 
# after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. 
# You may assume the parameter is positive.

# Examples:

# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect

def find_next_square(sq):
    import math
    num = math.sqrt(sq)
    print(num)
    if num.is_integer():
        return ((num*2)+1) + sq
    else:
        return -1

# There is a bus moving in the city, and it takes and drop some people in each bus stop.

# You are provided with a list (or array) of integer arrays (or tuples). Each integer array 
# has two items which represent number of people get into bus (The first item) and number of 
# people get off the bus (The second item) in a bus stop.

# Your task is to return number of people who are still in the bus after the last bus 
# station (after the last array). Even though it is the last bus stop, the bus is not empty 
# and some people are still in the bus, and they are probably sleeping there :D

def number(bus_stops):
    on = 0
    off = 0
    for x in range(len(bus_stops)):
        for y in range(len(bus_stops[x])):
            if y == 0:
                on += bus_stops[x][y]
            else:
                off += bus_stops[x][y]
    if on - off <= 0:
        return 0
    else:
        return on - off

#Lit Comprehension
def number2(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except 
# for the last two names, which should be separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''

def namelist(names):
    s = ''
    l = []
    
    for n in names:
        l.append(n.values())
        
    name_list = [name for n in l for name in n]
    
    for i in range(len(name_list)):
        if i == len(name_list)-1 and i != 0:
            s += ' & ' + name_list[i]
        elif i == 0:
            s += name_list[i]
        else:
            s += ', ' + name_list[i]
            
    return s