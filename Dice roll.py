import random
def main():
    again = True
    while (again):
        try:
            dice = str(input("Do you want to roll a 6 sided dice?: (y/n) "))
            if dice == "y":      
                print("The roll is a: ",random.randrange(1,6))
        except ValueError:
            print("Enter (y/n) only")
        do_again = input("Do you want to roll again?: (y/n) ")
        if do_again != "y":
            again = False
main()

