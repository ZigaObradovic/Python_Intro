from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script 2")
    favourite_drink("Coffe")
    favourite_food("sushi")
    print("Goodbye!")

if __name__ =="__main__":
    main()