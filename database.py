#!/usr/bin/env python3
import psycopg2
from database_connection import openConnection

#####################################################
##  Database Connection
#####################################################

'''
Connect to the database using the connection string
'''

'''
Validate staff based on username and password
'''


def checkLogin(login, password):

    return ['jdoe', 'John', 'Doe', 'jdoe@csh.com']


'''
List all the associated admissions records in the database by staff
'''
def findAdmissionsByAdmin(login):

    return


'''
Find a list of admissions based on the searchString provided as parameter
See assignment description for search specification
'''
def findAdmissionsByCriteria(searchString):

    return


'''
Add a new addmission 
'''
def addAdmission(type, department, patient, condition, admin):
    
    return


'''
Update an existing admission
'''
def updateAdmission(id, type, department, dischargeDate, fee, patient, condition):
    

    return
