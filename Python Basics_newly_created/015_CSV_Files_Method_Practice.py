# CSV means comma separated file basically it is used to store tabular data such as a spreadsheet or database
# A csv file stores tabular data(number and text) in plain text.
# Each line of file is a data record.
# Each record consist of one or more fields separated by commas.
# For working with CSV file we have an inbuilt module name CSV.

#**********************************  CSV Reading Methods  **************************************************

#--->  csv.reader(csvfile)            >>>  It will give output in list formate
#--->  csv.DictReader(csv_file)       >>>  It will give output in dict formate

#Below we will see the example of reading csv file using reader() method.
import os
import csv
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files\csv_files")
with open(r"data.csv","r") as file:
    rows= csv.reader(file)
    for row in rows:
        print(row)     #output will be in list format

        # ['E_name', 'E_ID']
        # []
        # ['John', '8']
        # []
        # ['John', '8']
        # []
        # ['John', '8']
        # []

#Below we will see the example of reading csv file using DictReader() method.
import os
import csv
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files\csv_files")
with open(r"data.csv","r") as file:
    rows=csv.DictReader(file)
    for row in rows:
        print(row)     #output will be in dict format

        # {'E_name': 'John', 'E_ID': '8'}
        # {'E_name': 'John', 'E_ID': '8'}
        # {'E_name': 'John', 'E_ID': '8'}

#**********************************  CSV Writing Methods  **************************************************

#--->  csv.writer(csvfile)                                          >>>> This method helps out to create object
#--->  csv.DictWriter(csv_file, field names in form of list)        >>>> This method helps out to create object

#Below are some methods which helps to write data in csv file using object which is created by above mention methods

#--->  writer_obj.writerow()      >> write single data and data could be list or dict
#--->  writer_obj.writerows()     >> write multiple data, and data should be list of iterables
#--->  writer_obj.writeheader()   >> write header in the file using the fieldnames specifies

import os
import csv
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files\csv_files")
with open(r"Tavnat_Practice.csv","w") as file:   #It will create file with name "Tavnat_Practice.csv"
    #Below lines are for creating headings on CSV File
    dict_writer_obj = csv.DictWriter(file,["Product", "Belongs", "Price"])   #With DictWriter only we can create CSV headings
    dict_writer_obj.writeheader()

    #Below lines is for adding data on CSV File with Dict formate because we created object for DictWriter
    dict_writer_obj.writerow({"Product":"coke", "Belongs":"Coca Cola", "Price":13})

    #Below lines is for adding data on CSV File with normal formate because we created normal write object
    normal_writer_object = csv.writer(file)
    normal_writer_object.writerow(["Pepsi","Coca Cola",14])  #we have to enter data in form of list for writerow()
    normal_writer_object.writerows([("Sprite","Coca Cola",15),("Lemonade","Coca Cola",18)])  #we have to enter data in form of list of tuples for writerows()

#********************************************   Activity  *****************************************************************

#WAP to read all the names fo the employees from employee.csv file.
import os
import csv
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files\csv_files")
with open(r"employees.csv") as file:
    csv_reader_obj = csv.reader(file)
    header=next(csv_reader_obj)        # This line is for skipping the header
    for row in csv_reader_obj:
        print(row[0])

#WAP to print only salaries which are greater than 70000
import os
import csv
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files\csv_files")
with open(r"employees.csv","r") as file:
    csv_reader_obj = csv.reader(file)
    header=next(csv_reader_obj)
    for row in csv_reader_obj:
        if int(row[3]) >= 70000:
            print(row)

#WAP to print only salaries which are greater than 70000 using DictReader()
import os
import csv
os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\files\csv_files")
with open(r"employees.csv","r") as file:
    dict_reader_obj = csv.DictReader(file)
    header=next(dict_reader_obj)
    for row in dict_reader_obj:
        if int(row["pay"]) >= 70000:
            print(row)
