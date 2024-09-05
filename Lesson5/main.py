"""Importing the csv module"""
import csv

"""Opening the customers.csv file"""
with open('Lesson5/customers.csv', 'r') as file:
  csv_reader = csv.reader(file)
  

  for csv in csv_reader:
    """Iterating through csv file and reading specified information"""

    id = csv[0]
    first_name = csv[2]
    last_name= csv[3]
    email_address = csv[9]
    
    """Displaying the customer details"""
    print(f"Customemail_addressr #{id}, {first_name} {last_name}, {email_address}")