# Below all methods are used to handle the directories

# getcwd() ==>> get current working directory
# mkdir(dir_name)   ==>> create a new directory
# chdir(dir_name)   ==>> changing the directory
# rmdir(dir_name)   ==>> remove directory
# listdir(dir_name) ==>> used to get the list of all files and directories in the specified directory if
                       # we want specify any directory the list of files and directories in the current working
                       # directory will be returned

import os
print(os.getcwd())

os.chdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created")
print(os.getcwd())

os.mkdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\Demo")
print(os.getcwd())

os.listdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\Demo")
print(os.getcwd())

os.rmdir(r"C:\Users\shashank.singh\PycharmProjects\Python_Practice_Code\Python Basics_newly_created\Demo")
print(os.getcwd())