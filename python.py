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

#Range function
n = 100
for i in range(n):
    if i % 2 == 0:
        print(i)