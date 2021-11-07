# 27: Introduction to Sets
def average(array):
    array = set(array)
    return sum(array) / len(array)



# 28: DefaultDict Tutorial
from collections import defaultdict
try:
    size_A, size_B = map(int, input().split(' '))
    group_A = defaultdict(list)
    group_B = list()

    for i in range(size_A):
        group_A[input()].append(i+1)  # REVIEW: cách 2 đầu toán tử
    for j in range(size_B):
        group_B.append(input())

    for k in group_B:
        if k in group_A:
            print(*group_A[k])
        else:
            print(-1)
except (ValueError):  # REVIEW: 1 execption thì không cần ngoặc
    print('Could not convert data to an integer.')



# 29: Calendar Module
import calendar
try:
    month, day, year = map(int, input().split())
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())

    weekday = calendar.weekday(year, month, day)
    day_name = calendar.day_name[weekday]
    print(day_name.upper())
except ValueError:
    print('Oops!  That was no valid number.  Try again...')



# 30: exceptions
for i in range(int(input())):
    try:
        a, b= map(int, input().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)



# 31: Collections.namedtuple()

from collections import namedtuple
try:
    n = int(input())
    header = input().split()
    total = 0
    Student = namedtuple('Student', header)
    for i in range(n):
        infor = input().split()
        student = Student(*infor)
        total += int(student.MARKS)
    print('{:.2f}'.format(total / n))
except (TypeError, ValueError, ZeroDivisionError) as e:
    print('Error Code:', e)





# 32: Collections.OrderedDict()

from collections import OrderedDict

ordd = OrderedDict()
try:
    n = int(input())
    for i in range(n):
        name, space, price = input().rpartition(' ')
        ordd[name] = ordd.get(name, 0) + int(price)
    for j in ordd:
        print(j, ordd[j])
except ValueError as e:
    print('Error Code:', e)




# 33: Symmetric Difference
try:
    size_a = int(input())
    a = set(input().split())
    size_b = int(input())
    b = set(input().split())
    if size_a != len(a) and size_b !=len(b):
        print('Size không khớp')
    else:
        # print(a^b)
        result = a.symmetric_difference(b)
        print('\n'.join(sorted(result, key = int)))  # keyword argument thì ko cần cách giữa 2 đầu dấu =
except ValueError as e:
    print('Error code:', e)




# 34: Collections.deque()

from collections import deque

de = deque()
try:
    n = int(input())
    for _ in range(n):
        line = input().split()
        if len(line) > 1:
            getattr(de, line[0])(line[1])
        else:
            getattr(de, line[0])()
    print(*de)
except (ValueError, AttributeError) as e:
    print('Error code:', e)




# 35: Set .add()

try:
    country = set()  # REVIEW: biến số nhiều thì nên đặt tên là số nhiều. VD: countries
    n = int(input())
    for _ in range(n):
        country.add(input())
    print(len(country))
except ValueError as e:
    print('Error code', e)



# 36: Incorrect Regex
#  long

import re

n = int(input())
for _ in range(n):
    try:
        re.compile(input())
        print('True')
    except re.error:
        print('False')



# 37: Set .discard(), .remove() & .pop()

try:
    n = int(input())
    s = set(map(int, input().split()))
    
    if n != len(s):
        print('size không khớp')
    
    number_cmd = int(input())
    
    for _ in range(number_cmd):
        line = input().split()
        
        if len(line) > 1:
            getattr(s, line[0])(int(line[1]))
        else:
            getattr(s, line[0])()
    
    print(sum(s))

except ValueError as e:
    print('Error code: ', e)





# 38: Set .union() Operation

try:
    size_a = int(input())
    a = set(input().split())
    size_b = int(input())
    b = set(input().split())
    if size_a != len(a) and size_b != len(b):
        print('size khong khop')
    c = a.union(b)
    # c = a | b
    print(len(c))
except ValueError as e:
    print('Error code:', e)



# 39: Set .intersection() Operation

try:
    size_a = int(input())
    a = set(input().split())
    size_b = int(input())
    b = set(input().split())
    if size_a != len(a) and size_b != len(b):
        print('size khong khop')
    c = a.intersection(b)
    # c = a & b
    print(len(c))
except ValueError as e:
    print('Error code:', e)




# 40: Set .difference() Operation

try:
    size_a = int(input())
    a = set(input().split())
    size_b = int(input())
    b = set(input().split())
    if size_a != len(a) and size_b != len(b):
        print('size khong khop')
    c = a.difference(b)
    # c = a - b
    print(len(c))
except ValueError as e:
    print('Error code:', e)




# 41: Set .symmetric_difference() Operation

try:
    size_a = int(input())
    a = set(input().split())
    size_b = int(input())
    b = set(input().split())
    if size_a != len(a) and size_b != len(b):
        print('size khong khop')
    c = a.symmetric_difference(b)
    # c = a ^ b
    print(len(c))
except ValueError as e:
    print('Error code:', e)




# 42: Set Mutations

try:
    size = int(input())
    A = set(input().split())
    if size != len(A):
        print('size khong khop')
    number_operations =  int(input())
    for _ in range(number_operations):
        operation, size = input().split()
        list_ = set(input().split())
        if int(size) != len(list_):
            print('size khong khop')
        else:
            getattr(A, operation)(list_)
    print(sum(map(int, A)))
except ValueError as e:
    print('Error code:', e)





# 43: Itertools.combinations()

from itertools import combinations
try:
    string, size =  input().split()
    string = sorted(string)
    for i in range(int(size)):
        l = list(combinations(string, i + 1))
        [print("".join(j)) for j in l]
except ValueError as e:
    print('Error code:', e)

