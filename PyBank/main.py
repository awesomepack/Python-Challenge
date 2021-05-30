''' 
PyBank Main Script
Authored by: Merari Cisneros
* Read Financial data from CSV source
'''
#Importing dependencies
import os , csv



# Reading in the data in PyBank CSV

file = os.path.join('PyBank' , 'Resources' , 'PyBank.csv');

with open(file , 'r') as Fdata:

    Fdata_reader = csv.reader(Fdata  , delimiter = ',');

    header = next(Fdata_reader);


    Months = []; #stores dates
    PL = []; #stores profit/loss info

    for row in Fdata_reader:

        Months.append(row[0]);
        PL.append(int(row[1]));


        


print(len(Months));
print(sum(PL));