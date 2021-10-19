index = 0

width = 80
title = '南开大学软件学院通讯录管理系统v0.01a'
str_lst = [
    '添加数据请按[a]',
    '查看数据请按[s]',
    '删除数据请按[d]',
    '修改数据请按[m]',
    '返回菜单请按[q]'
]
choices = ['a', 's', 'd', 'm', 'q']
fmt = '{0:^{1}}'
lst_fmt = '{:<5}{:<15}{:<20}{:<20}{:<20}'


class Student:
    # 属性
    id = 0
    name = ''
    qq = ''
    tel = ''
    mail = ''

    # 构造方法
    def __init__(self, name, qq, tel, mail):
        global index
        index += 1
        self.id = index
        self.name = name
        self.qq = qq
        self.tel = tel
        self.mail = mail


# 函数
def create(name, qq, tel, mail):
    s = Student(name, qq, tel, mail)
    global studentDB
    studentDB.append(s)
    print('{0:~^{1}}'.format('修改/添加数据', width-4))
    print('{:<4}{:<14}{:<20}{:<19}{:<19}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
    print(lst_fmt.format(s.id, s.name, s.qq, s.tel, s.mail))
    print('~' * width)
    print('添加成功！')


def find():
    print('{0:~^{1}}'.format('通讯录数据列表', width-4))
    print('{:<4}{:<14}{:<20}{:<19}{:<19}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
    for st in studentDB:
        print(lst_fmt.format(st.id, st.name, st.qq, st.tel, st.mail))
    print('~' * width)


def delete(sid):
    for s in studentDB:
        if s.id == sid:
            studentDB.remove(s)
            print('删除成功')


def update(sid, name, qq, tel, mail):
    for s in studentDB:
        if s.id == sid:
            if name != ' ':
                s.name = name
            if qq != ' ':
                s.qq = qq
            if tel != ' ':
                s.tel = tel
            if mail != ' ':
                s.mail = mail
            print('{0:~^{1}}'.format('修改/添加数据', width - 4))
            print('{:<4}{:<14}{:<20}{:<19}{:<19}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
            print(lst_fmt.format(s.id, s.name, s.qq, s.tel, s.mail))
            print('~' * width)
            print('修改成功！')
            break

def check(str):
    for ch in str:
        if ch < '0' or ch > '9':
            return False
    return True

print('#' * width)
print(fmt.format(title, width))
print()
for s in str_lst:
    if 'q' in s:
        print('{0:>{1}}'.format(s, width-4))
    else:
        print(fmt.format(s, width))
print('#' * width)

studentDB = []

while True:
    choose = input('请输入相应的命令(返回菜单请按q): ')
    if choose == 'a':
        name = input('请输入您的姓名: ')
        qq = input('请输入您的QQ号码: ')
        while not check(qq):
            qq = input('QQ格式不合法，请重试: ')
        tel = input('请输入您的电话号码: ')
        while not check(tel):
            tel = input('电话号码格式不合法，请重试: ')
        mail = input('请输入您的邮箱: ')
        create(name, qq, tel, mail)
    elif choose == 's':
        find()
    elif choose == 'd':
        flag = False
        stu_id = int(input('请输入学生序号: '))
        for st in studentDB:
            if st.id == stu_id:
                flag = True
                break
        if flag:
            delete(stu_id)
        else:
            print('该序号不存在！')
            continue
    elif choose == 'm':
        flag = False
        stu_id = int(input('请输入学生序号: '))
        for st in studentDB:
            if st.id == stu_id:
                flag = True
                break
        if flag:
            name = input('请输入您的姓名(若不修改，请输入空格): ')
            qq = input('请输入您的QQ号码(若不修改，请输入空格): ')
            tel = input('请输入您的电话号码(若不修改，请输入空格): ')
            mail = input('请输入您的邮箱(若不修改，请输入空格): ')
            update(stu_id, name, qq, tel, mail)
        else:
            print('该序号不存在！')
            continue
    elif choose == 'q':
        exit(0)
    else:
        print('非法输入，请重试！')
