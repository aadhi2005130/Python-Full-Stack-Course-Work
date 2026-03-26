print('-------------welcome=------')
-------------welcome=------
acc_num = input("Enter the account number: ")
pin = input("Enter the pin: ")
if acc_num in data and data[acc_num]['pin']==pin:
    print("Login successful")
    while True:
        menu()
        ch = input("Enter your choice: ").lower()
        if ch=='c':
            check_balance(acc_num)
        elif ch=='d':
            deposit(acc_num)
        elif ch=='w':
            withdraw(acc_num)
        elif ch=='v':
            view_transactions(acc_num)
        elif ch=='p':
            change_pin(acc_num)
        elif ch=='e':
            print("-------Thank you--------")
            break
        
            
