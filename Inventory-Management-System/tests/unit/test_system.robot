*** Settings ***
Resource    resources/db_keywords.robot

*** Test Cases ***

Create Employee
    Connect DB
    Create Employee Table
    Reset Tables

    Execute Sql String    INSERT INTO employee(eid,name,email,pass,utype) VALUES (1,'Juan','juan@test.com','1234','Admin')

    ${result}=    Query    SELECT * FROM employee WHERE eid=1
    Should Not Be Empty    ${result}

    Disconnect DB


Update Employee
    Connect DB
    Create Employee Table
    Reset Tables

    Execute Sql String    INSERT INTO employee(eid,name) VALUES (1,'Juan')
    Execute Sql String    UPDATE employee SET name='Pedro' WHERE eid=1

    ${result}=    Query    SELECT name FROM employee WHERE eid=1
    Should Be Equal    ${result[0][0]}    Pedro

    Disconnect DB


Delete Employee
    Connect DB
    Create Employee Table
    Reset Tables

    Execute Sql String    INSERT INTO employee(eid,name) VALUES (1,'Juan')
    Execute Sql String    DELETE FROM employee WHERE eid=1

    ${result}=    Query    SELECT * FROM employee WHERE eid=1
    Should Be Empty    ${result}

    Disconnect DB


Create Product
    Connect DB
    Create Product Table
    Reset Tables

    Execute Sql String    INSERT INTO product(pid,name,price,qty,status) VALUES (1,'Laptop',1000,10,'Active')

    ${result}=    Query    SELECT * FROM product WHERE pid=1
    Should Not Be Empty    ${result}

    Disconnect DB


Update Product Stock
    Connect DB
    Create Product Table
    Reset Tables

    Execute Sql String    INSERT INTO product(pid,name,price,qty,status) VALUES (1,'Laptop',1000,10,'Active')
    Execute Sql String    UPDATE product SET qty=5 WHERE pid=1

    ${result}=    Query    SELECT qty FROM product WHERE pid=1
    Should Be Equal As Integers    ${result[0][0]}    5

    Disconnect DB


Product Becomes Inactive
    Connect DB
    Create Product Table
    Reset Tables

    Execute Sql String    INSERT INTO product(pid,name,price,qty,status) VALUES (1,'Laptop',1000,1,'Active')
    Execute Sql String    UPDATE product SET qty=0, status='Inactive' WHERE pid=1

    ${result}=    Query    SELECT status FROM product WHERE pid=1
    Should Be Equal    ${result[0][0]}    Inactive

    Disconnect DB