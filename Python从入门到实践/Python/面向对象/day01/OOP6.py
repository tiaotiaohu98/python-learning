from re import A


class Atm(object):
    
    def __card(self):
        print('插卡')
        
    def __auth(self):
        print('密码')
        
    def __input(self):
        print('金额')
        
    def __take_money(self):
        print('取款')
        
    def __bill(self):
        print('账单')
        
    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__take_money()
        self.__bill()
        
atm = Atm()
atm.withdraw()
        