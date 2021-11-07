# 1. if else

if __name__ == '__main__':
    # try:
    #     n = int(input().strip())
    # except (ValueError, TypeError):
    #     print('input is not integer.')
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0:
        if n in range(2, 6) or n > 20:
            print('Not Weird')
        else:
            print('Weird')



#  2. Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)



#  3. Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)



# 4. Loop

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)


# 5. Write a function

def is_leap(year):
    # return (
    #     year % 4 == 0 and
    #     (
    #         year % 400 == 0 or
    #         year % 100 != 0
    #     )
    # )

    leap = False
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        leap = True
    return leap



# 6. Print Function

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(1,n+1):
        a.append(i)
    print(''.join(str(i) for i in a))


# 7. List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # d = {
    #     'a': [1, 2, 3],
    #     'b': [4, 5, 6]
    # }
    # x = [i for k in d for i in d[k]]

    # x = [
    #     i for i in range(10) 
    #     if i % 2 == 0
    # ]

    # print (
    #     [
    #         [a, b, c] 
    #         for a in range(0, x + 1) 
    #         for b in range(0 , y + 1) 
    #         for c in range(0, z + 1) 
    #         if a + b + c != n 
    #     ]
    # )

    list1 = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                list2 =[]
                list2.append(i)
                list2.append(j)
                list2.append(k)
                sumNumber = 0
                for number in list2:
                    sumNumber += number
                if sumNumber != n:
                    list1.append(list2)
    print(list1)


# 8. Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newArr = []
    arr = list(arr)
    maxNumber = max(arr)
    for i in arr:
        if i != maxNumber:
            newArr.append(i)
    print(max(newArr))



# 9. Nested Lists

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    min_score = min(arr, key = lambda x: x[1])
    arr_copy = arr.copy()
    min_score = min(arr, key = lambda x: x[1])
    [
        arr_copy.remove(i) 
        for i in arr 
        if i[1] == min_score[1]
    ]
    min_score = min(arr_copy, key = lambda x: x[1])
    arr_copy.sort(key = lambda x: x[0])
    [print(i[0]) for i in arr_copy if i[1] == min_score[1]]



# 10. Finding the percentage

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    mark = student_marks[query_name]
    print("{0:.2f}".format(sum(mark) / len(mark)))




# 11. List

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        line = input().split()
        if line[0] == 'insert':
           arr.insert(int(line[1]), int(line[2]))
        elif line[0] == 'print':
            print(arr)
        elif line[0] == 'remove':
            arr.remove(int(line[1]))
        elif line[0] == 'append':
            arr.append(int(line[1]))
        elif line[0] == 'sort':
            arr.sort()
        elif line[0] == 'pop':
            arr.pop()
        else:
            arr.reverse()




# 12. Tuples

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    integer_list = tuple(integer_list)
    print(hash(integer_list))


# 13. sWAP cASE

def swap_case(s):
    string = []
    char = ''
    for i in s:
        if i.islower():
            char = i.upper()
        else:
            char = i.lower()
        string.append(char)
    return ''.join(string)


# 14. Merge the Tools
def merge_the_tools(string, k):
    for i in range(int(len(string) / k)):
        arr = string[
            (i * k) : ((i+1) * k)
        ]
        unique = []
        for i in arr:
            if i not in unique:
                unique.append(i)
        print(''.join(unique))


# 15. Time delta
from datetime import datetime
def time_delta(t1, t2):
    first = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')

    # delta = first - second
    # delta_seconds = int(delta.total_seconds())
    # delta_seconds_abs = abs(delta_seconds)

    # return str(delta_seconds_abs)
    # return '{0}'.format(delta_seconds_abs)
    # return '%d' % delta_seconds_abs
    # return f'{delta_seconds_abs}'

    return str(
        abs(
            int(
                (first-second).total_seconds()
            )
        )
    )


# 16. String Split and Join

def split_and_join(line):
    return '-'.join(line.split(' '))


# 17. What's Your Name?

def print_full_name(first, last):
    print('Hello {0} {1}! You just delved into python.'.format(first, last))

