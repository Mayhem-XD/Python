class Account:
    def __init__(self,ano,owner,balance):
        self.ano = ano
        self.owner = owner
        self.__balance = balance            # 0<=balance<10000000

    def deposit(self,amount):
        if self.__balance + amount >= 10000000:
            print('천만원 이상은 잔액으로 가져갈 수 없습니다.')
            return
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance - amount < 0:
            print('잔액이 부족합니다')
            return
        self.__balance -= amount

    def __str__(self):
        return f'계좌번호는 {self.ano}, 소유주는 {self.owner}, 잔액은 {self.__balance:9,d}원 입니다.'