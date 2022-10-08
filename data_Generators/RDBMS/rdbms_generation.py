import sys
sys.path.insert(1, '/Users/julitorresma/Desktop/capstoneFinal/data_Generators')
from utils import *
import shutil
import random 
from datetime import datetime
import json
import pandas as pd
import os
import psycopg2
"""
RDBMS tables:
Transaction
	id int,
	Customer_id int,
	Transaction_ts timestamp,
	Amount int
Customer
	Id int,
	First_name STRING,
	Last_name STRING,
	Phone_number int,
	Address string
"""
def exportToCsv(cursor, table_name):
    sql = f"copy (SELECT * FROM {table_name}) TO '/Users/julitorresma/Desktop/capstoneFinal/data_Generators/RDBMS/{table_name}.csv' DELIMITER ';' CSV HEADER;"
    cursor.execute(sql)
    return 
def insertQueries(size, cursor):
    id_list_transaction = randomlistID(1, size)
    id_list_costumer = randomlistID(1, size)
    time_stamp = listTimeStamp(size)
    first_names = getFirstNames(size)
    last_names = getLastNames(size)
    amounts = getRandomAmounts(size)
    phones = generatePhoneNumbers(size)
    address = randomCities(size)

    for i in range(size):

        postgres_insert_query = """ INSERT INTO capstone.Transaction (id, Customer_id, Transaction_ts, Amount) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (id_list_transaction[i], id_list_costumer[i], time_stamp[i], amounts[i])
        cursor.execute(postgres_insert_query, record_to_insert)

        postgres_insert_query = """ INSERT INTO capstone.Customer (id, FIRST_NAME, LAST_NAME, Phone_number, Address) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (id_list_transaction[i], first_names[i], last_names[i], phones[i], address[i])
        cursor.execute(postgres_insert_query, record_to_insert)
    

def mainGenerator(size):
    #Establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='julitorresma', password='270700', host='127.0.0.1', port= '5432'
    )
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Doping Transaction table if already exists.
    cursor.execute("DROP TABLE IF EXISTS capstone.Transaction")
    #Creating table as per requirement
    sql ='''CREATE TABLE capstone.Transaction(
    id INT PRIMARY KEY,
    Customer_id INT,
    Transaction_ts CHAR(30),
    Amount INT)
    '''
    cursor.execute(sql)
    cursor.execute("DROP TABLE IF EXISTS capstone.Customer")
    #Creating table as per requirement
    sql ='''CREATE TABLE capstone.Customer(
    id INT PRIMARY KEY,
    FIRST_NAME CHAR(30) NOT NULL,
    LAST_NAME CHAR(30),
    Phone_number CHAR(30),
    Address CHAR(40)
    )'''
    cursor.execute(sql)

    insertQueries(100, cursor)

    exportToCsv(cursor, "capstone.Customer")
    exportToCsv(cursor, "capstone.Transaction")

    print("Tables created successfully........")
    conn.commit()
    #Closing the connection
    conn.close()

mainGenerator(100)