import math
def user_info(prompt):
    while (True):
        try:
            radius = float(input(prompt))
            if radius < 0:
                print ("Nevgative number(s) not allowed. Enter a positive.")
                continue
            break
        except ValueError:
                print ("Enter a whole number or a floating number")
    return radius

def main():
    do_cal = True
    while (do_cal):
        print ("This program is a estimator of ctlinder cost in USD")
        radius = user_info("What is the radius in feet: ")
        height = user_info ("What is the height in feet: ")
        cost = user_info("what is the cost per pint for a coating: ")
    #calculation
        s_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
    #each pint = $50
        much = s_area / 50
        new_much = (math.ceil(much))
        print ("This is the how many pints are needed",math.ceil(much))
        price = math.ceil(much) * cost
        
        print("The cost is: $", "%.2f"%price)
        agian = input("Do you want to preform another calculation y/n: ")
        if (agian != "y"):
            do_cal = False
main()
