from CardOwner import CardOwner

def print_menu():
    ### Prints ATM Options to the User
    print("Please choose from one of the following options")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

def deposit(CardOwner):
    try:
        deposit = float(input("How much will you like to deposit?: "))
        CardOwner.set_balance(CardOwner.get_balance + deposit)
        print("Transaction successful. Your new balance is: ", str(CardOwner.get_balance()))

    except:
        print("Invalid input")

def withdraw(CardOwner):
    try:
        withdraw = float(input("How much will you like to withdraw: "))
        ###Verify if user has enough balance to make such withdrawal
        if(CardOwner.get_Balance() < withdraw):
            print("Sorry, Insufficient balance :(")
        else:
            CardOwner.set_Balance(CardOwner.get_Balance() - withdraw)
            print("Withdrawal Successful :). Your new balance is: ", str(CardOwner.get_balance()))
    except:
        print("Invalid Input") 

def check_balance(CardOwner):
    print("Your Account balance is: ", CardOwner.get_Balance())


if __name__ == "__main__":
    current_user = CardOwner ("","","","","")

    ###Creating A Dummy Repository of card Owners
    list_of_CardOwners =[]
    list_of_CardOwners.append(CardOwner("1234567","1234","Justice","Edwin","100000.56"))
    list_of_CardOwners.append(CardOwner("234567","2345","Kobby","Joe","5000.23"))
    list_of_CardOwners.append(CardOwner("345678","3456","Edwryu","Phoenix","70000.56"))
    list_of_CardOwners.append(CardOwner("456789","4567","Edwin","Wonder","56000"))


    ### Prompt user for debit card number and validate
    DebitCardNum = ""
    while True:
        try:
            DebitCardNum = input("Please enter your credit card number ")
            ### Check Card number against dummy repository
            DebitMatch = [holder for holder in list_of_CardOwners if holder.CardNumber == DebitCardNum]
            if(len(DebitMatch) > 0):
                current_user = DebitMatch[0]
                break
            else:
                print("Invalid Card Number")
        except:
            print("Invalid Card Number")

    
    ### Prompt for PIN
    while True:
        try:
            UserPin = int(input("Input your PIN: ").strip())
            if(current_user.get_Pin() == UserPin):
                break
            else:
                print("Invalid PIN. Please try again")
        except:
            print("Invalid PIN. Please try again")

    ### Print options now that they are logged in
    print("Welcome ", current_user.get_FirstName(), ":)")
    option = 0
    while (True):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again")

        if(option == 1):
            deposit(current_user)

        elif(option == 2):
            withdraw(current_user)

        elif(option == 3):
            check_balance(current_user)

        elif(option == 4):
            break

        else:
            option = 0

        print("Thank you. Have a nice day")


