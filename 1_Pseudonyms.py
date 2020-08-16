#Makes pseudonyms out of existing names
import csv
import random

first_path = '/mnt/c/Users/mattb/Desktop/Code/Python/1_Pseudonyms_files/Firstnames.csv' 
last_path = '/mnt/c/Users/mattb/Desktop/Code/Python/1_Pseudonyms_files/Names_2010Census.csv'
first_name = []
last_name = []

#finds first names
with open(first_path) as f_obj:
    for line in enumerate(f_obj):
        seperated_name = (line[1].split(','))[1]
        seperated_name = seperated_name.split('"')
        seperated_name = seperated_name[1]
        first_name.append(seperated_name)

#finds last names
with open(last_path) as f_obj:
    for line in enumerate(f_obj):
        seperated_name = (line[1].split(','))[0]
        seperated_name = seperated_name.lower()
        seperated_name = seperated_name.capitalize()
        last_name.append(seperated_name)

print(random.choice(first_name), random.choice(last_name))

        
