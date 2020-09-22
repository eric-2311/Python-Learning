# print('Hello World!')

# list = [1, 2, 3, 4]
# print(list)
# print(len(list))

#Fibonnaci Sequence
a , b = 0, 1
while a < 10:
    print(a, end = ',')
    a, b = b, a+b

#For statements
list = ['the', 'cat', 'in', 'the', 'hat']
for w in list:
    print(w, len(w))

#Range function range(start, end, step)
n = 100
for i in range(50, n, 2):
    print(i)

#Range function range(length)
for i in range(10):
    if i % 2 == 0:
        print(i)

#Iterating over a list using range and len
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list)):
    if i % 2 == 0:
        print(i)