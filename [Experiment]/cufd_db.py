import pymysql
db = pymysql.connect(host='localhost',
                     database='mydb',
                     user='root',
                     password='root')
cursor = db.cursor()

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

# 函数
def create(name, qq, tel, mail):
    sql_insert = """INSERT INTO students(name, qq, tel, mail) VALUES (%s, %s, %s, %s)"""
    param = (name, qq, tel, mail)
    cursor.execute(sql_insert, param)
    db.commit()
    cursor.execute("SELECT MAX(id) FROM students")
    newid = cursor.fetchone()[0]
    print('{0:~^{1}}'.format('修改/添加数据', width - 4))
    print('{:<4}{:<14}{:<20}{:<19}{:<19}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
    print(lst_fmt.format(newid, name, qq, tel, mail))
    print('~' * width)
    print('添加成功！')


def find():
    sql_find = """SELECT * FROM students"""
    cursor.execute(sql_find)
    rs = cursor.fetchall()
    print('{0:~^{1}}'.format('通讯录数据列表', width-4))
    print('{:<4}{:<14}{:<20}{:<19}{:<19}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
    for ars in rs:
        print(lst_fmt.format(ars[0], ars[1], ars[2], ars[3], ars[4]))
    print('~' * width)


def delete(sid):
    sql_delete = """DELETE FROM students WHERE id = %s"""
    cursor.execute(sql_delete, (sid,))
    db.commit()
    print('删除成功!')


def update(sid, name, qq, tel, mail):
    cursor.execute("SELECT * FROM students WHERE id = %s", (sid,))
    rs = cursor.fetchall()
    origin = list(rs[0])
    if name != ' ':
        origin[1] = name
    if qq != ' ':
        origin[2] = qq
    if tel != ' ':
        origin[3] = tel
    if mail != ' ':
        origin[4] = mail
    newdata = origin[1:]
    newdata.append(sid)
    sql_update = """UPDATE students SET name = %s, qq = %s, tel = %s, mail = %s WHERE id = %s"""
    cursor.execute(sql_update, tuple(newdata))
    db.commit()
    print('{0:~^{1}}'.format('修改/添加数据', width - 4))
    print('{:<4}{:<14}{:<20}{:<19}{:<19}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
    print(lst_fmt.format(newdata[4], newdata[0], newdata[1], newdata[2], newdata[3]))
    print('~' * width)
    print('修改成功!')


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
        stu_id = input('请输入学生序号: ')
        sql_findid = """SELECT id FROM students WHERE id = %s"""
        cursor.execute(sql_findid, (stu_id,))
        if cursor.fetchone() != None:
            delete(stu_id)
        else:
            print('该序号不存在！')
            continue
    elif choose == 'm':
        stu_id = input('请输入学生序号: ')
        sql_findid = """SELECT id FROM students WHERE id = %s"""
        cursor.execute(sql_findid, (stu_id,))
        if cursor.fetchone() != None:
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
