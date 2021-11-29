#task_1
a = int(input('>>'))
b = int(input('>>'))
def my_sum(a, b):
    count = 0
    for i in range(a, b, 1):
        if (i % 2 == 0):
            count += i
    return count
print(my_sum(a, b))

#task_2
n = int(input('enter an integer:'))
def my_function(num):
    count = 0
    for i in range(1, n + 1):
        count += i
    return count
print(my_function(n))

#task_3
a = int(input('enter int number:'))
b = int(input('enter int number:'))
c = int(input('enter int number:'))
x = int(input('enter int number:'))
def my_problem(a, b, c, x):
    return a * x ^ 2 + b * x + c
print(my_problem(a, b, c, x))

#task_4
n = int(input('Enter a number between 0 and 20:'))
def number_to_words(n):
    my_list = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    my_secondlist = {10: 'десять', 20: 'двадцать'}
    n1 = n % 10
    n2 = n - n1
    if n < 10:
        return my_list.get(n)
    elif n >= 10 and n in my_secondlist:
        return my_secondlist.get(n)
    else:
        return my_secondlist.get(n2) + ' ' + my_list.get(n1)
print(number_to_words(n))