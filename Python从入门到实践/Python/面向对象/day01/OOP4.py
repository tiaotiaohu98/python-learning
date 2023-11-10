from os import name


class Person(object):
    
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
    
    def eat(self):
        self.weight += 0.2
        
    def run(self):
        self.weight -= 0.1
    
    def __str__(self):
        return f'姓名：{self.name}, 体重：{self.weight:.1f}斤！'
    
    
xm = Person('小明', 75.0)
xm.eat()
xm.run()
print(xm)