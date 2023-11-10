from re import S


class Student(object):
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def print_grade(self):
        if self.grade >= 90:
            print(f'姓名：{self.name}, 成绩：优秀')
        elif self.grade >= 80:
            print(f'姓名：{self.name}, 成绩：良好')
        elif self.grade >= 70:
            print(f'姓名：{self.name}, 成绩：中等')
        elif self.grade >= 60:
            print(f'姓名：{self.name}, 成绩：合格')
        else:
            print(f'姓名：{self.name}, 成绩：不及格')
            
            
s1 = Student('张三', 90)
s1.print_grade()
