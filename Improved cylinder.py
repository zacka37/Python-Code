import math

def cal(prompt):
    while (1):
        try:
            r = float(input(prompt))
            if r < 0:
               print ("Enter a positive number")
               continue
            break
        except ValueError:
            print ("Enter only a number")
    return r

#Radius
def main():
    do_calculation = True
    while (do_calculation):
    
        r = cal("What is the Radius: ")
        h = cal("What is the Height: ")

        volume = math.pi * r**2 * h
        print ("The volume is: ", volume)

        another_calculation = input("Do you want to perform another calculation? (y/n): ")
        if (another_calculation != "y"):
            do_calculation = False
main()

