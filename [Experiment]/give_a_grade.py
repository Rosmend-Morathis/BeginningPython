while True:
    grade = float(input('请输入成绩: '))
    if grade < 60:
        print('D')
    elif grade < 70:
        print('C')
    elif grade < 90:
        print('B')
    else:
        print('A')
