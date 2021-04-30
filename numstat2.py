# Challenge: Number Stats 2
import statistics
# open file
while (True):
    try:
        name_of_file = input("What is the name of the file you are uploading: ")
        open_file = open(name_of_file, "r")
    except:
        print("Can not locate file")
        continue
    else:
        print("The file you selected is", name_of_file)
        break
numbers_list =[]
# file = (name_of_file)
# convert file to a int
for number in open_file:
    numbers = int(number)
    numbers_list.append(numbers)

# Summary
while (True):
    try:
        # Count
        add = sum(numbers_list)
        print ("Sum: ", add)
        numbers_in_file = len(numbers_list)
        print("Count: ", numbers_in_file)     
        average = sum(numbers_list) / len(numbers_list)
        print("Average: ", average)
        maximum_value = max(numbers_list)
        print("Maximum: ", maximum_value)
        minimum = min(numbers_list)
        print("Minimum: ", minimum)
        range_of_num = max(numbers_list) - min(numbers_list)
        print("Range: ", range_of_num)
        median_value= statistics.median(numbers_list)
        print("Median: ", median_value)
        mode = statistics.mode(numbers_list)
        print("Mode: ", mode)

    except:
        print("The file selected does not include only numbers")
    break

open_file.close()



