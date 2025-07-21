import pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})
df_cards = pd.read_csv("cards.csv", dtype = str).to_dict(orient="records")
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

class ReserveTicket:
    def __init__(self,customer_name, hotell):
        self.customer_name = customer_name
        self.hotell = hotell

    def generate(self):
        return f"""Reservation successfull! Name: {self.customer_name} & Hotel name: {self.hotell}"""

class CreditCard:
    def __init__(self,num):
        

    def validate:
    

    pass

if __name__ == "__main__":
    print(df)
    id = input("Enter hotel ID: ")
    hotel = Hotel(id)

    if hotel.availibile():
        hotel.book()
        name = input("Enter your name: ")
        reservatation  = ReserveTicket(name,hotel)
        print(reservatation.generate())
    else: 
        print("Hotel is not free")