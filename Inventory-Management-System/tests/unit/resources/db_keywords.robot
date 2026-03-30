*** Settings ***
Library    DatabaseLibrary

*** Variables ***
${DB_PATH}    ${CURDIR}/../ims.db

*** Keywords ***

Connect DB
    Connect To Database
    ...    sqlite3
    ...    database=${DB_PATH}

Disconnect DB
    Disconnect From Database

Create Employee Table
    Execute Sql String    CREATE TABLE IF NOT EXISTS employee (eid INTEGER PRIMARY KEY, name TEXT, email TEXT, gender TEXT, contact TEXT, dob TEXT, doj TEXT, pass TEXT, utype TEXT, address TEXT, salary TEXT)

Create Product Table
    Execute Sql String    CREATE TABLE IF NOT EXISTS product (pid INTEGER PRIMARY KEY, name TEXT, price REAL, qty INTEGER, status TEXT)

Reset Tables
    Execute Sql String    DELETE FROM employee
    Execute Sql String    DELETE FROM product