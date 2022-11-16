import csv
from county_dictionary import CountyDictionary
'''
Program: csv_import_to_class_object_assignment.py
Author: Joshua M. McGinley
Last date modified: 11/15/2022

 CSV Import to Class Object Assignment
What you're building
For this assignment, you'll be importing the full list of counties of Iowa and their demographics, creating a
dictionary of objects from the data, and applying some methods and math to the data.
How you'll do it

    Start by downloading this CSV file:  Iowa 2010 Census Data Population Income.csv
    Create a class with attributes for all of the columns in the data.
    Import the data in a dictionary of objects, one for each county.
    Either delete the objects for "Iowa State" and "United States" or programatically avoid creating objects from
    them in the first place.  You must do this within your program and not on the CSV file itself.  Data cleansing
    such as this is commonplace in data analytics and editing the source data in many cases is not an option.
    Using a method, find the population/household for Dallas County and print it in the console
    Find the total population for Iowa by adding up the population across all counties and print it in the console

Notes/Hints

    If you find that you are having troubles, for troubleshooting, you may want to create a simple csv to import
    so you aren't dealing with 100 rows of data.  Just make sure that your final submission is based on the CSV
    provided for you.
    Remember that your first row in the file is headers so don't create an object from it by mistake
    Since the numbers in this file have commas, you'll need to strip them out to complete the pop/household and
    total Iowa population work

'''

county = {}

with open('Iowa_2010_Census_Data_Population_Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    county = {}
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[1])] = CountyDictionary(row[0], row[2], row[3], row[4], row[5], row[6])

#print(county['Dallas'].pop)

def pop_per_household(county):
    num_pop = int(county['Dallas'].pop.replace(',',''))
    num_household = int(county['Dallas'].num_households.replace(',',''))
    pop_per_house = num_pop / num_household
    print('Number of people per home:', pop_per_house)

def total_pop(county):
    del county['Iowa State']
    del county['United States']
    pop_sum = 0
    for key in county:
        pop_sum += int(county[key].pop.replace(',',''))
    print('Iowa\'''s population is:', pop_sum)

dal = pop_per_household(county)
pop_iowa = total_pop(county)
