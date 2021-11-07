# 18. Mutations

"""
Mutable / immutable:
- Mutable: list, dict.
    l1 = [1, 2, 3]
    l2 = l1  # pass by reference
    l1.append(4)
    l1[2] = 333
    print(l2) -> [1, 2, 333, 4]

    d1 = {'a': 1, 'b': 2}
    d2 = d1
    d2['c'] = 3
    print(d1) -> {'a': 1, 'b': 2, 'c': 3}

- Immutable: tuple, str, int, v.v.
    t1 = (1, 2, 3)
    t1[1] = 'aaa' -> exception
    t1 = (1,)

    x = 'hello'
    y = x  # pass by value
    x = 'internet'
    print(y) -> 'hello'

    x = 'hello'
    x = x.upper()
    print(x) -> 'HELLO'
"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)


# 19. Find a string

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].find(sub_string) == 0:
            count += 1
    return count

# 20. String validators

if __name__ == '__main__':
    string = input()
    print(any([char.isalnum() for char in string]))
    print(any([char.isalpha() for char in string]))
    print(any([char.isdigit() for char in string]))
    print(any([char.islower() for char in string]))
    print(any([char.isupper() for char in string]))

    all(char.isalnum() for char in string)


# 21. Text Alignment

thickness = int(input())
char = 'H'

# Top Cone
height = thickness
for i in range(height):
    left_cone = (char * i).rjust(thickness - 1)
    right_cone = (char * i).ljust(thickness - 1)
    top_cone = left_cone + char + right_cone
    print(top_cone)

    # Top Pillars
height = thickness + 1
for i in range(height):
    left_pillar = (char * thickness).center(thickness * 2)
    right_pillar = (char * thickness).center(thickness * 6)
    top_pillars = left_pillar + right_pillar
    print(top_pillars)

    #  Middle Belt
height = (thickness + 1) // 2
for i in range(height):
    middle_belt = (char * thickness * 5).center(thickness * 6)
    print(middle_belt)

    # Bottom Pillars
height = thickness + 1
for i in range(height):
    left_pillar = (char * thickness).center(thickness * 2)
    right_pillar = (char * thickness).center(thickness * 6)
    bottom_pillars = left_pillar + right_pillar
    print(bottom_pillars)

    # Bottom Cone
height = thickness
for i in range(height):
    left_cone = (char * (thickness - i - 1)).rjust(thickness)
    right_cone = (char * (thickness - i - 1)).ljust(thickness)
    bottom_cone = (left_cone + char + right_cone).rjust(thickness * 6)
    print(bottom_cone)



# 22. Text wrap

def wrap(string, max_width):
    result = ''
    for i in range(0, len(string), max_width):
        result += string[i: i+max_width] + '\n'
    return result


# 23. Capitalize

def solve(s):
    arr = s.split(' ')
    arr = [i.capitalize() for i in arr]
    return ' '.join(arr)


# 24. itertools.product()
from itertools import product
A = map(int, input().split())
B = map(int, input().split())
A = list(A)
B = list(B)
AxB = list(product(A, B))
print(*AxB)


# 25. collections.Counter()
from collections import Counter

number_shoes = int(input())
list_of_sizes = list(map(int, input().split()))
counter_sizes = Counter(list_of_sizes)
number_customers = int(input())
money = []

for i in range(number_customers):
    buy = list(map(int, input().split()))
    size = buy[0]
    price = buy[1]
    if size in counter_sizes.keys() and counter_sizes[price] != 0:
        counter_sizes[buy[0]] = counter_sizes[buy[0]] - 1
        money.append(buy[1])
print(sum(money))



# 26. itertools.permutations(iterable[, r])
from itertools import permutations
string, size = input().split()
perms = list(permutations(sorted(string), int(size)))
for i in range(len(perms)):
    perms[i] = ''.join(perms[i])
[print(i) for i in perms]

