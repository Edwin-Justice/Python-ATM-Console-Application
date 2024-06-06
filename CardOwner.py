###Creating The Cardhplder Class and initalizing it

class CardOwner():
    def __init__(self, CardNumber, Pin, Firstname, Lastname, Balance):
        self.CardNumber = CardNumber
        self.Pin = Pin
        self.FirstName = Firstname
        self.Lastname = Lastname
        self.Balance = Balance
    
    ###Creating Our Getter Methods
    def get_CardNumber(self):
        return self.CardNumber
    
    def get_Pin(self):
        return self.Pin
    
    def get_Firstname(self):
        return self.FirstName
    
    def get_Lastname(self):
        return self.Lastname
    
    def get_Balance(self):
        return self.Balance
    
    ###Creating Our Setter Methods
    def set_CardNumbers(self, newval):
        self.CardNumber = newval

    def set_Pin(self, newval):
        self.Pin = newval

    def get_Firstname(self, newval):    
        self.FirstName = newval

    def set_Lastname(self, newval):
        self.Lastname = newval

    def set_Balance(self, newval):
        self.Balance = newval

    def print_details(self):
        print("Card Number: ", self.CardNumber)
        print("Pin: ", self.CardNumber)
        print("First Name: ", self.CardNumber)
        print("Last Name: ", self.CardNumber)
        print("Balance: ", self.CardNumber)