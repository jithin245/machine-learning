#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

total_poi = len([1 for person in enron_data.keys() if enron_data[person]['poi'] is True])
print "Total No of POIs ", total_poi

with open('../final_project/poi_names.txt', 'r') as file:
    file.readline()
    file.readline() #Skip First 2 lines
    
    print "Original Total No of POIs " , len([1 for line in file if line != ''])


print 'James Prentice\'s total stock value ', enron_data['PRENTICE JAMES']['total_stock_value']
print 'Mails sent from wesley colwell to POI\'s ', enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print 'CEO - total payments ', enron_data['SKILLING JEFFREY K']['total_payments']
print 'Chairman - total payments ', enron_data['LAY KENNETH L']['total_payments']
print 'CFO - total payments ', enron_data['FASTOW ANDREW S']['total_payments']


print 'No. of person with salary NaN ', len([1 for person in enron_data.keys() if enron_data[person]['salary'] != 'NaN'])
print 'No. of person with email NaN ', len([1 for person in enron_data.keys() if enron_data[person]['email_address'] != 'NaN'])

total = len(enron_data.keys())
print 'Total No of Persons ', total
print 'No. of persons with total payments NaN ', len([1 for person,data in enron_data.items() if data['total_payments'] == 'NaN'])

print 'Percent of POI with total payments NaN ' ,len([1 for person, data in enron_data.items()  \
           if data['total_payments'] == 'NaN' and data['poi'] is True])/float(total_poi)
