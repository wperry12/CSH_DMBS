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
    conn = openConnection()
    cursor = conn.cursor()
    query = "SELECT * FROM administrators WHERE username = %s AND password = %s"
    cursor.execute(query, (login, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result if result else None

# def checkLogin(login, password):

#     return ['jdoe', 'John', 'Doe', 'jdoe@csh.com']


'''
List all the associated admissions records in the database by staff
'''
def findAdmissionsByAdmin(login):
    conn = openConnection()
    cursor = conn.cursor()
    query = """
        SELECT * FROM admissions
        WHERE admin_username = %s
        ORDER BY 
            discharge_date DESC NULLS LAST,
            patient_name ASC,
            admission_type DESC
    """
    cursor.execute(query, (login,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# def findAdmissionsByAdmin(login):

#     return


'''
Find a list of admissions based on the searchString provided as parameter
See assignment description for search specification
'''
def findAdmissionsByCriteria(searchString):
    conn = openConnection()
    cursor = conn.cursor()
    query = """
        SELECT * FROM admissions
        WHERE 
            (LOWER(admission_type) LIKE LOWER(%s) OR
            LOWER(department) LIKE LOWER(%s) OR
            LOWER(patient_name) LIKE LOWER(%s) OR
            LOWER(condition) LIKE LOWER(%s))
            AND (discharge_date IS NULL OR discharge_date > CURRENT_DATE - INTERVAL '2 years')
        ORDER BY 
            discharge_date ASC NULLS FIRST,
            patient_name ASC
    """
    searchPattern = f"%{searchString}%"
    cursor.execute(query, (searchPattern, searchPattern, searchPattern, searchPattern))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
# def findAdmissionsByCriteria(searchString):

#     return


'''
Add a new addmission 
'''
def addAdmission(type, department, patient, condition, admin):
    conn = openConnection()
    cursor = conn.cursor()
    query = """
        INSERT INTO admissions (admission_type, department, patient_name, condition, admin_username)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """
    cursor.execute(query, (type, department, patient, condition, admin))
    admission_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return admission_id
# def addAdmission(type, department, patient, condition, admin):
    
#     return


'''
Update an existing admission
'''
def updateAdmission(id, type, department, dischargeDate, fee, patient, condition):
    conn = openConnection()
    cursor = conn.cursor()
    query = """
        UPDATE admissions
        SET 
            admission_type = %s,
            department = %s,
            discharge_date = %s,
            fee = %s,
            patient_name = %s,
            condition = %s
        WHERE id = %s
    """
    cursor.execute(query, (type, department, dischargeDate, fee, patient, condition, id))
    conn.commit()
    cursor.close()
    conn.close()
    
# def updateAdmission(id, type, department, dischargeDate, fee, patient, condition):
    

#     return
