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