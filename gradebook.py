import statistics
# gradebook.py
# Display the average of each student's grade.
# Display the average for each assignment.

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]
# Vars for student grades
gradebookst1 = gradebook[0]
gradebookst2 = gradebook[1]
gradebookst3 = gradebook[2]
gradebookst4 = gradebook[3]
gradebookst5 = gradebook[4]
gradebookst6 = gradebook[5]
gradebookst7 = gradebook[6]
gradebookst8 = gradebook[7]
gradebookst9 = gradebook[8]
gradebookst10 = gradebook[9]

# Ass. Avg. math
print("Assignment Averages:")
column0 = []
for column in gradebook:
    element_in_column_0 = column[0]
    column0.append(element_in_column_0)
print("Assignment 1: ", "{:.2f}".format(statistics.mean(column0)))

column1 = []
for column in gradebook:
    element_in_column_1 = column[1]
    column1.append(element_in_column_1)
print("Assignment 2: ", "{:.2f}".format(statistics.mean(column1)))

column2 = []
for column in gradebook:
    element_in_column_2 = column[2]
    column2.append(element_in_column_2)
print("Assignment 3: ", "{:.2f}".format(statistics.mean(column2)))

column3 = []
for column in gradebook:
    element_in_column_3 = column[3]
    column3.append(element_in_column_3)
print("Assignment 4: ", "{:.2f}".format(statistics.mean(column3)))

column4 = []
for column in gradebook:
    element_in_column_4 = column[4]
    column4.append(element_in_column_4)
print("Assignment 5: ", "{:.2f}".format(statistics.mean(column4)))

column5 = []
for column in gradebook:
    element_in_column_5 = column[5]
    column5.append(element_in_column_5)
print("Assignment 6: ", "{:.2f}".format(statistics.mean(column5)))

column6 = []
for column in gradebook:
    element_in_column_6 = column[6]
    column6.append(element_in_column_6)
print("Assignment 7: ", "{:.2f}".format(statistics.mean(column6)))

column7 = []
for column in gradebook:
    element_in_column_7 = column[7]
    column7.append(element_in_column_7)
print("Assignment 8: ", "{:.2f}".format(statistics.mean(column7)))

column8 = []
for column in gradebook:
    element_in_column_8 = column[8]
    column8.append(element_in_column_8)
print("Assignment 9: ", "{:.2f}".format(statistics.mean(column8)))

column9 = []
for column in gradebook:
    element_in_column_9 = column[9]
    column9.append(element_in_column_9)
print("Assignment 10: ", "{:.2f}".format(statistics.mean(column9)))

column10 = []
for column in gradebook:
    element_in_column_10 = column[10]
    column10.append(element_in_column_10)
print("Assignment 11: ", "{:.2f}".format(statistics.mean(column10)))

column11 = []
for column in gradebook:
    element_in_column_11 = column[11]
    column11.append(element_in_column_11)
print("Assignment 12: ", "{:.2f}".format(statistics.mean(column11)))

column12 = []
for column in gradebook:
    element_in_column_12 = column[12]
    column12.append(element_in_column_12)
print("Assignment 13: ", "{:.2f}".format(statistics.mean(column12)))

column13 = []
for column in gradebook:
    element_in_column_13 = column[13]
    column13.append(element_in_column_13)
print("Assignment 14: ", "{:.2f}".format(statistics.mean(column13)))

column14 = []
for column in gradebook:
    element_in_column_14 = column[14]
    column14.append(element_in_column_14)
print("Assignment 15: ", "{:.2f}".format(statistics.mean(column14)))

# Student Averages
print("Student Averages:")
print("Student 1: ", "{:.2f}".format(statistics.mean(gradebookst1)))
print("Student 2: ", "{:.2f}".format(statistics.mean(gradebookst2)))
print("Student 3: ", "{:.2f}".format(statistics.mean(gradebookst3)))
print("Student 4: ", "{:.2f}".format(statistics.mean(gradebookst4)))
print("Student 5: ", "{:.2f}".format(statistics.mean(gradebookst5)))
print("Student 6: ", "{:.2f}".format(statistics.mean(gradebookst6)))
print("Student 7: ", "{:.2f}".format(statistics.mean(gradebookst7)))
print("Student 8: ", "{:.2f}".format(statistics.mean(gradebookst8)))
print("Student 9: ", "{:.2f}".format(statistics.mean(gradebookst9)))
print("Student 10: : ", "{:.2f}".format(statistics.mean(gradebookst10)))


