from student import Student


class StudentCMS(object):

    def __init__(self):
        self.students = []

    @staticmethod
    def menu():
        print('-' * 80)
        print('欢迎使用学生管理系统V1.0')
        print('【1】添加学生信息')
        print('【2】删除学生信息')
        print('【3】修改学生信息')
        print('【4】查询学生信息')
        print('【5】遍历所有学生信息')
        print('【6】保存学生信息到文件')
        print('【7】退出学生管理系统')
        print('-' * 80)

    def get_StudentInfo(self):
        # self.load_file_data()
        for value in self.students:
            print(value)

    def add_student(self):
        # 接收用户输入
        name = input('请输入学生姓名：')
        age = input('请输入学生年龄：')
        mobile = input('请输入学生电话：')

        if not self.query_student(name):
            student = Student(name, age, mobile)
            self.students.append(student)
            self.save_data_to_file()
            print(f'恭喜您，学生信息添加成功！')
        else:
            print('该学生已经存在！')

    def del_student(self):
        # 接收用户输入
        name = input('请输入要删除的学生姓名：')
        if self.query_student(name):
            for v in self.students:
                if v.name == name:
                    print(f'{v.name}已删除')
                    self.students.remove(v)
                    self.save_data_to_file()
                    break
        else:
            print('该学生不存在！')

    def modify_student(self):
        # 接收用户输入
        name = input('请输入要修改的学生姓名：')

        # 查找对应学生
        if self.query_student(name):
            for i in self.students:
                if i.name == name:
                    value = input('请输入要修改的信息(姓名or年龄or电话)：')
                    if value == '姓名':
                        new_name = input('请输入姓名：')
                        # 修改姓名
                        i.name = new_name
                    elif value == '年龄':
                        new_age = input('请输入年龄：')
                        i.age = new_age
                    elif value == '电话':
                        new_mobile = input('请输入电话：')
                        i.mobile = new_mobile
                    self.save_data_to_file()
                    print('修改成功！')
                    break
        else:
            print('该学生不存在！')

    def query_student(self, name):
        res = None
        for v in self.students:
            if v.name == name:
                res = v
        return res

    def search_student(self):
        # 接收用户输入
        res = None
        name = input('请输入要查询的学生姓名：')
        for v in self.students:
            if v.name == name:
                res = v
                break
        if res:
            print(f'姓名：{res.name}，年龄：{res.age}，电话：{res.mobile}')
        else:
            print('该学生不存在！')

    # 写入到文件中
    def save_data_to_file(self):
        with open('student.txt', 'w', encoding='utf-8') as file:
            for v in self.students:
                file.write(str(v.name) + '  ' + str(v.age) + '  ' + str(v.mobile) + '\n')
        file.close()
        print('保存学生信息到指定文件成功！')

    # 读取文件内容
    def load_file_data(self):

        try:
            file = open('student.txt', 'r', encoding='utf-8')
        except:
            file = open('student.txt', 'w', encoding='utf-8')
        else:
            # 读取全部内容
            # content = file.read()
            # 按行读取，将数据放在列表中
            content = file.readlines()
            # 每次读取一行数据
            # content = file.readline()
            # print(content)
            for i in content:
                # 设置print 不换行
                # print(i, end='')
                i = list(i.strip('\n').split('  '))
                # 以对象的方式加入
                stu = Student(i[0], i[1], i[2])
                self.students.append(stu)
            # print(self.students)
        finally:
            file.close()

    def start(self):
        self.load_file_data()
        while True:
            self.menu()

            a = input('请输入您要执行的功能编号：')

            if not a.isdigit():
                print('很抱歉，您的输入有误，请输入一个数字！')
                continue
            else:
                user_num = int(a)

            if user_num == 1:
                # print('添加学生信息')
                self.add_student()
            elif user_num == 2:
                # print('删除学生信息')
                self.del_student()
            elif user_num == 3:
                # print('修改学生信息')
                self.modify_student()
            elif user_num == 4:
                # print('查询学生信息')
                self.search_student()
            elif user_num == 5:
                self.get_StudentInfo()
                # print('遍历所有学生信息')
            elif user_num == 6:
                self.save_data_to_file()
            elif user_num == 7:
                print('退出系统成功，感谢您使用本系统！')
                break
            else:
                print('很抱歉，您的输入有误，请重新输入！')
