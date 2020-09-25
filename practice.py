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

# Your task is to write a function which returns the sum of following 
# series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# Examples:
# SeriesSum(1) => 1 = "1.00"
# SeriesSum(2) => 1 + 1/4 = "1.25"
# SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

def series_sum(n):
    num = 1
    denom = 4
    terms = [1]
    
    while len(terms) < n:
        new_num = num/denom
        terms.append(new_num)
        denom += 3
    
    if sum(terms) == 0:
        return str(format(0, '.2f'))
    elif n == 0:
        return str(format(0, '.2f'))
    else:
        return str(format(sum(terms), '.2f'))

#List comprehension
def series_sum2(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

# As the name may already reveal, it works basically like a Fibonacci, 
# but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
# And, worse part of it, regrettably I won't get to hear non-native Italian 
# speakers trying to pronounce it :(

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting 
# input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? 
# As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence 
# by once place, you may be tempted to think that we would get the same sequence 
# shifted by 2 places, but that is not the case and we would get:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci 
# function that given a signature array/list, returns the first n elements - signature 
# included of the so seeded sequence.

# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then 
# return an empty array (except in C return NULL) and be ready for anything else 
# which is not clearly specified

def tribonacci(signature, n):
    seq = [signature[0], signature[1], signature[2]]
    
    if n == 1:
        return [signature[0]]
    elif n == 2: 
        return [signature[0], signature[1]]
    elif n == 0:
        return []
    
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2] + seq[-3])
        
    return seq

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything 
# but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# eg:

# validate_pin("1234") == True
# validate_pin("12345") == False
# validate_pin("a234") == False

def validate_pin(pin):
    l = list(pin)
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    if len(pin) == 0:
        return False
    elif len(l) != 4 and len(l) != 6:
        return False
        
    for i in range(len(l)):
        if l[i] not in nums:
            return False
        
    return True

#List comprehension
def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# Write a function that when given a URL as a string, parses out just the 
# domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    symbols = ['/', '.', ':']
    prefix = ['www', 'http', 'https']
    l = list(url)
    
    for x in symbols:
        while x in l:
            l.insert(l.index(x), '#')
            l.remove(x)
            
    m = ''.join(l)
         
    m = list(m.split('#'))
    
    for x in m:
        n = ''
        if n in m:
            m.remove(n)        
    
    for x in prefix:
        while x in m:
            if x in prefix:
                m.remove(x)
            
    return m[0]

# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) 
# and a positive integer p

# we want to find a positive integer k, if it exists, such as the sum of the 
# digits of n taken to the successive powers of p is equal to k * n.
# In other words:

# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers

def dig_pow(n, p):
    str_num = list(str(n))
    
    for i in range(len(str_num)):
        str_num[i] = int(str_num[i])
    
    prod = 0
    i = 0
    
    while i < len(str_num):
        prod += str_num[i]**p
        p += 1
        i += 1
        
    result = str(prod/n).split('.')
    
    if result[0] == '0':
        return -1
    elif int(result[1]) > 0:
        return -1
    else:
        return int(result[0])

# You are going to be given a word. Your job is to return the middle 
# character of the word. If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"

def get_middle(s):
    
    if len(s) == 1:
        return s
    elif len(s) == 2:
        return s[:2]
    
    if len(s) % 2 != 0:
        return s[len(s)//2]
    else:
        return s[(len(s)//2)-1] + s[len(s)//2]

# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an 
# empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(source_array):
    odds = list(filter(lambda x: x % 2 == 1, source_array))
    odds.sort()
    
    j = 0
    
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odds[j]
            j += 1
            
    return source_array

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) 
# where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

# Example 1:
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

# Example 2:
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.

# Example 3:
# Input: rating = [1,2,3,4]
# Output: 4

# Constraints:

# n == rating.length
# 1 <= n <= 200
# 1 <= rating[i] <= 10^5


def numTeams(rating):
    '''I am so ashamed of this, give me some time to
    refactor T_T'''

    from itertools import permutations
    
    if rating == sorted(rating):
        return len(rating)
    
    perms = list(permutations(rating))
    
    for i in range(len(perms)):
        perms[i] = perms[i][:3]
        
    l = list(filter(lambda x: x[0] < x[1] and x[1] < x[2], perms))
    m = list(filter(lambda x: x[0] > x[1] and x[1] > x[2], perms))
    
    # print(l)
    
    l = list(filter(lambda x: rating.index(x[0]) < rating.index(x[1]), l))
    l = list(filter(lambda x: rating.index(x[1]) < rating.index(x[2]), l))
    l = list(filter(lambda x: rating.index(x[0]) < rating.index(x[1]), l))
    l = list(filter(lambda x: rating.index(x[0]) < rating.index(x[2]), l))
    
    print(l)
    
    m = list(filter(lambda x: rating.index(x[0]) < rating.index(x[2]), m))
    m = list(filter(lambda x: rating.index(x[1]) < rating.index(x[2]), m))
    m = list(filter(lambda x: rating.index(x[0]) < rating.index(x[1]), m))
    m = list(filter(lambda x: rating.index(x[0]) < rating.index(x[2]), m))
    
    print(m)
    
    result = []
    
    for x in l:
        if x not in result:
            result.append(x)
            
    for x in m:
        if x not in result:
            result.append(x)
            
    return len(result)

def num_teams(rating):
    '''More optimized solution for num_teams :)'''
    import pdb
    # pdb.set_trace()
    teams = 0
    x = 0

    while x <= len(rating)-2:
        y = x + 1
        while y <= len(rating)-1:
            z = y + 1
            while z < len(rating):
                if rating[x] < rating[y] and rating[y] < rating[z]:
                    teams += 1
                    l.append([rating[x], rating[y], rating[z]])
                elif rating[x] > rating[y] and rating[y] > rating[z]:
                    teams += 1
                    l.append([rating[x], rating[y], rating[z]])

                z += 1
            y += 1
        x += 1

    
    print(l)
    print(teams)
