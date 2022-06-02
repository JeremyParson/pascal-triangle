def max_num (a, b, c):
    return max(a, b, c)

def mult_list (numbers, amount):
    return [x * amount for x in numbers]

def rev_string (str):
    return ''.join([str[i] for i in reversed(range(len(str)))])

def num_within (target, start, end):
    return target in range(start, end)

def pascal (n):
    if n == 1:
        print(n)
        return [n]
    result = pascal(n - 1)
    row = []
    for i in range(n):
        if i - 1 < 0 or i == len(result):
            row.append(1)
            continue
        row.append(result[i - 1] + result[i])
    print(row)
    return row

print(max_num(100, 5, 32))
print(rev_string("Hello World"))
print(mult_list([1, 2, 3, 4], 2))
pascal(50)