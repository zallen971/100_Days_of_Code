import os
from art import logo
print(logo)
print("Welcome to the secret auction!\n")

name = input("Enter the name of the bidder: ")
bid = int(input("What's your bid: $"))

bid_dict = [
    {
        "user": name,
        "number": bid
    },
]

#Defined function to add users to bid_dict dictionary list
def add_user(bid_dict):
        name = input("Enter the name of the bidder: ")
        bid = int(input("What's your bid: $"))
        new_bid = {
            "user": name,
            "number": bid
        }
        bid_dict.append(new_bid)
        return bid_dict

#Clears terminal - Tested in VScode
def clear():
    system = os.name
    
    if system == "nt":
        os.system("cls")
    else:
        os.system("clear")


continue_bid = input("\nIs there another who wants to bid? ")


#While continue bid is yes
while continue_bid == "yes":
    clear()
    print(logo)
        
    add_user(bid_dict)
    continue_bid = input("Is there another who wants to bid? ")
    highest_bid = max(bid["number"] for bid in bid_dict)
    highest_bidder = [bid["user"] for bid in bid_dict if bid["number"] == highest_bid][0]

    #if continue bid is no then print the winning bid and who won
    if continue_bid == "no":
        clear()
        print(logo)
        print(f"The highest bid was: ${highest_bid}.")
        print(f"Winner: {highest_bidder}")
        
    