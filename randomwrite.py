import random
random_number_file_name = "randomnum.txt"

def user(prompt):
    while (True):
        try:
            start = int(input(prompt))
            if start < 0:
                print ("Only positive number(s) are allowed")
                continue
            break
        except ValueError:
                print ("Please enter a whole number")
    return start
def main():
    

    start = user("What is the lowest the random number should be: ")
    end = user("What is the highest the random number should be: ")
    how_many_num = user("How many random number(s) should there be: ")
    try:
        random_number_file = open(random_number_file_name, "w")
        for i in range(how_many_num):

            random_value = random.randint(start, end)
            print (random_value)  

            random_number_file.write(str(random_value))
            random_number_file.write("\n")
        random_number_file.close()
    except:
        print ("The highest number is lover then the lowest number")

main()

