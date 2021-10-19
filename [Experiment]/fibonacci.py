# 递归方法
def fibonacci_1(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


# 一般方法
def fibonacci_2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        yield a



print('递归方法: ')
num = int(input('请输入数字n: '))
for i in range(num):
    print(fibonacci_1(i), end=' ')
print()

print('一般方法: ')
num = int(input('请输入数字n: '))
for i in fibonacci_2(num):
    print(i, end=' ')
print()
