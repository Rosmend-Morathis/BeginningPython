def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)


num = int(input('请输入数字n: '))
print(factorial(num))
