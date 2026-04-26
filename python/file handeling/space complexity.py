def prints(n):
    if n <= 0:
        return
    print("Codingal")
    print(n)

    print(n // 2)

    print("code recursionTimeComplexity")

print(10)

def sum_n(n):
    if n <= 0:
        return 0
    return n * (n+1) // 2

print(sum_n(5))

def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
a=[12,3,4,15]
arraysum(a)

def sum1(n):
    if n <=0:
        return 0
    
    for i in a:
        sum=sum+i
    return sum
a=[12,3,4,15]
arraysum(a)

def sum1(n):
    if n <= 0:
        return 0
    return n + sum1(n-1)

print(sum1(5))
