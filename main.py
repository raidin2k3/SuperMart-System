import item
import customers
#main menu
def MainMenu():
    print("1: Item Database")
    print("2: Customer Database")
    n=int(input("Choose Option[1/2]:"))
    if n==1:
        item.items()
    elif n==2:
        customers.registry()
