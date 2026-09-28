print('This file contains models for the application.')

# DATA PREPARATION
# how to read & write csv files

# WRITING CSV FILES
import csv # importing the csv library or class
with open('students.csv', 'w', newline='') as f:  # with make sure to close the file after we are done with it .
    writer = csv.writer(f) # creating a object 

    # calling different methods/functions of the writer object to write data to the file
    writer.writerow(['Name', 'Age', 'Grade']) 
    writer.writerow(['Alice', 20, 'A'])
    writer.writerow(['Bob', 22, 'B'])
    writer.writerow(['Charlie', 21, 'C'])

# this will create a new csv file called students.csv with the following content:
# Name,Age,Grade

# with : a safety wrapper - gurantees the files get properly closed when you are done
# open('students.csv', 'w', newline=''): fucntion actually opens the file : first argument is the file name
# w: write mode - if the file already exists, it will be overwritten

# students.csv , 'w' (write mdoe) : do you have a studnets.csv file in your  current working directory? 
#               if not, it creates one. if yes, it overwrites the existing file.
# as f: creates a file object called f that you can use to write to the file
# csv.writer(f): Wraps the open file with the tool csv which knows how to write data into csv file -- so basically 
#             we are assigning a object " writer = csv.writer(f) " which is a writer object that can write data to the file f in csv format

# READING CSV FILES
with open('students.csv', 'r') as f:
    reader = csv.reader(f) # creating a reader object to read data from the file & it red the data in teh file .

    # calling different methods/functions of the reader object to read data from the file
    for row in reader:
        print(row) # printing each row of the csv file