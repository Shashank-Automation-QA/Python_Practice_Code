                                                                        #reader (for list output)

#WAP read data from the csv file using reader........

import os
import csv
with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\test.csv") as file:
    obj=csv.reader(file)
    for data in obj:
        print(data)

                                                                    #DictReader  (for dictonary output)

#WAP read data from the csv file using dictreader........

with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\test.csv") as file:
    obj=csv.DictReader(file)
    for data in obj:
        print(data)

                                                                      #using writer      #writerrow (for entering one data)  

        

#WAP write data from the csv file using writerow........     #writerow use for entering one record only

with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\test.csv","w") as file:
    write_obj=csv.writer(file)
    write_obj.writerow(["Tesla",500,37.6])
    p=write_obj.writerow
    p(["Tesla",500,37.6])
                                                                        #using writer    #writerows   (for entering more than one data )



#WAP write data from the csv file using writerows........    #writerows use for entering more than one record

with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\test.csv","a" ,newline="") as file:       #newline="\r\n" it will give next alternate line for printing
    write_obj=csv.writer(file)                                                                                   #newline="" it will print in next line
    c=write_obj.writerows
    data=["Tesla",700,37.6],["Tesla",800,37.6]
    c(data)

                                                                #using DictWriter 

#WAP write data from the csv file using writerow........     #writerow use for entering one record only

with open(r"C:\Users\singh\OneDrive\Desktop\mam\Alpha5\files\csv_files\shashank.csv","w",newline="") as file:
    write_obj=csv.DictWriter(file,["Name","id","value"])
    write_obj.writeheader()
    write_obj.writerows([{"Name":"car","id":500,"value":37.6}])
   

                                                                                                                        
