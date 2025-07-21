import pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})
df_cards = pd.read_csv("cards.csv", dtype = str).to_dict(orient="records")
df_security = pd.read_csv("card_security.csv", dtype =str )

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availibility to no. """
        df.loc[df["id"] == self.hotel_id,"available"] = "no"
        df.to_csv("hotels.csv", index = False)

    def availibile (self):
        """Check if its avalible first"""
        availibility = df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        if availibility == "yes":
            return True
        else: False

class SpaPackage():
    def add_package():
        print("Spa Package added successfully")

class ReserveTicket:
    def __init__(self,customer_name, hotell):
        self.customer_name = customer_name
        self.hotell = hotell

    def generate(self):
        return f"""Reservation successfull! Name: {self.customer_name} & Hotel name: {self.hotell}"""

class CreditCard:
    def __init__(self,num):
        self.num = num        

    def validate(self,expiration, holder,cvc):
        card_data = {"number": self.num, "expiration" : expiration, "holder" : holder, "cvc" : cvc}
        if card_data in df_cards:
            return True
        else: False
    pass

class SecureCard(CreditCard):
    def authenticate(self,input_password):
        password = df_security.loc[df_security["number"] == self.num, "password"].squeeze()
        if password == input_password:
            return True
        else: return False

if __name__ == "__main__":
    print(df)
    id = input("Enter hotel ID: ")
    hotel = Hotel(id)

    if hotel.availibile():
        credit_card = SecureCard(num = "5678")
        if credit_card.validate(expiration="12/28", cvc="456", holder="JANE SMITH"):
            if credit_card.authenticate("mypass"):
                hotel.book()
                name = input("Enter your name: ")
                reservatation  = ReserveTicket(name,hotel)
                print(reservatation.generate())
                question = input("Do you want a spa package? Y/N ")
                if question == "Y" or "y":
                    SpaPackage.add_package()
            else: print("Card Authentication Failed")
        else: print("Payment Unsuccsessful")    
    else: 
        print("Hotel is not free")