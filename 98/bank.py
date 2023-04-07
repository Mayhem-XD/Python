import sys, os, joblib
import bank_util as bu
from account import Account

# 계좌는 계좌번호, 소유주, 잔액으로 구성됨
# 계좌번호는 생성된 시점의 시간,분,초 6자리로 구성됨
filename = 'account.jl'
if os.path.exists(filename):
    acc_list = joblib.load(filename)
else:
    acc_list = [
        Account('142603', '홍길동', 10000)
    ]

while True:
    try:
        menu = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4:출금, 5:종료> '))
    except:
        print('잘못된 명령입니다.\n')
        continue

    if menu == 5:
        joblib.dump(acc_list, filename)
        sys.exit()

    if menu == 1:
        bu.create_account(acc_list)
    elif menu == 2:
        for acc in acc_list:
            print(acc)
    elif menu == 3:
        bu.deposit(acc_list)
    elif menu == 4:
        bu.withdraw(acc_list)
    print()   