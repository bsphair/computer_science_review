General Interview Questions
===========================

## Table of Contents
* [General](#general)
  * [What is a database?](#general-database-description)
  * [What is a DBMS?](#general-dbms)
  * [What is a RDMS?](#general-rdbms)
  * [How is DBMS different from RDBMS?](#general-dmbs-rdbms-differences)
  * [Advantages of DBMS?](#general-dbms-advantages)
  * [What do you understand by Data Redundancy?](#general-data-redundancy)
  * [What are the various types of relationships in Database? Define them](#general-db-relationships)
  * [Explain the terms ‘Record’, ‘Field’ and ‘Table’ in terms of database.](#general-record-field-table)
  * [What is a Relational Database View](#general-view-definition)
  * [Relational Database View Advantages/Disadvantages](#general-view-advatages-disadvantages)
  * [What do you understand by Functional dependency?](#general-func-depend-def)
  * [What do you understand by the ER model?](#general-er-model-def)
  * [What is the Primary Key](#general-primary-key)
  * [What is the Composite Key](#general-composite-key)
  * [What is the Unique Key](#general-unique-key)
* [Normalization](#normalization)
  * [Explain Normalization](#normalization-definition)
  * [Explain De-Normalization](#normalization-denormalization-definition)
  * [What are the different types of Normalization?](#normalization-bcnf)
  * [What is BCNF?](#normalization-types)
* [SQL](#sql)
  * [What is SQL?](#sql-definition)
  * [How many SQL statements are used? Define them.](#sql-statements-definitions)
  * [DDL Examples](#sql-ddl-examples)
  * [DML Examples](#sql-ddl-examples)
  * [DCL Examples](#sql-dcl-examples)
  * [What is the difference between a View and a Table?](#sql-view-table)
  * [What does the HAVING clause do?](#sql-having-clause)
* [Joins](#joins)
  * [Inner JOIN](#joins-inner)
  * [Natural JOIN](#joins-natural)
  * [Cross JOIN](#joins-cross)
  * [Right JOIN](#joins-right)
  * [Left JOIN](#joins-left)
  * [Outer/Full JOIN](#joins-outer-full)
* [References](#references)

###
## General

### <a name="general-database-description"/> What is a database?
Database is an organized collection of related data where the data is stored and organized to serve some specific purpose.

### <a name="general-record-field-table"/> Explain the terms ‘Record’, ‘Field’ and ‘Table’ in terms of database.
* <b>Record:</b> Record is a collection of values or fields of a specific entity. For Example, An employee, Salary account, etc.

* <b>Field:</b> A field refers to an area within a record that is reserved for specific data. For Example, Employee ID.

* <b>Table:</b> Table is the collection of records of specific types. For Example, the Employee table is a collection of records related to all the employees.

### <a name="general-view-definition"/> What is a Relational Database View
* A searchable object in a database that is defined by a query
* Though a view doesn’t store data, some refer to a views as “virtual tables,” you can query a view like you can a table
* A view can combine data from two or more table, using joins, and also just contain a subset of information.  This makes them convenient to abstract, or hide, complicated queries.

### <a name="general-dbms"/> What is a DBMS?
DBMS stands for Database Management System. It is a collection of application programs which allow the user to organize, restore and retrieve information about data efficiently and as effectively as possible.

Some popular DBMS’s are MySql, Oracle, Sybase, etc.

### <a name="general-dmbs-rdbms-differences"/> How is DBMS different from RDBMS?
The key difference here, compared to DBMS, is that RDBMS stores data in the form of a collection of tables and relations can be defined between the common fields of these tables. Most modern database management systems like MySQL, Microsoft SQL Server, Oracle, IBM DB2 and Amazon Redshift are based on RDBMS.

### <a name="general-rdbms"/> What is a RDMS?
Relational Database Management System(RDBMS) is based on a relational model of data that is stored in databases in separate tables and they are related to the use of a common column. Data can be accessed easily from the relational database using Structured Query Language (SQL).

### <a name="general-dbms-advantages"/> Advantages of DBMS? 
* Data is stored in a structured way and hence redundancy is controlled.
* Validates the data entered and provide restrictions on unauthorized access to the database.
* Provides backup and recovery of the data when required.
* It provides multiple user interfaces.

### <a name="general-data-redundancy"/> What do you understand by Data Redundancy?

Duplication of data in the database is known as data redundancy. As a result of data redundancy, duplicated data is present at multiple locations, hence it leads to wastage of the storage space and the integrity of the database is destroyed.


### <a name="general-db-relationships"/> What are the various types of relationships in Database? Define them
* <b>One-to-one</b>: One table has a relationship with another table having the similar kind of column. Each primary key relates to only one or no record in the related table.
* <b>One-to-many</b>: One table has a relationship with another table that has primary and foreign key relations. The primary key table contains only one record that relates to none, one or many records in the related table.
* <b>Many-to-many</b>: Each record in both the tables can relate to many numbers of records in another table.

### <a name="general-view-advatages-disadvantages"/> Relational Database View Advantages/Disadvantages
* <b>Advantages</b>
  * As there is no physical location where the data in the view is stored, it generates output without wasting resources.
  * Data access is restricted as it does not allow commands like insertion, updation, and deletion.

* <b>Disadvantages</b>
  * The view becomes irrelevant if we drop a table related to that view.
  * Much memory space is occupied when the view is created for large tables.

### <a name="general-func-depend-def"/> What do you understand by Functional dependency?
A relation is said to be in functional dependency when one attribute uniquely defines another attribute.

Example:
```
R is a Relation, X and Y are two attributes. T1 and T2 are two tuples. Then,

T1[X]=T2[X] and T1[Y]=T2[Y]

Means, the value of component X uniquely define the value of component Y.

Also, X->Y means Y is functionally dependent on X.
```

### <a name="general-er-model-def"/> What do you understand by the ER model?
E-R model is an Entity-Relationship model which defines the conceptual view of the database.

The E-R model basically shows the real-world entities and their association/relations. Entities here represent the set of attributes in the database.

### <a name="general-primary-key"/> What is the Primary Key
<b>Primary Key<b> is that column of the table whose every row data is uniquely identified. Every row in the table must have a primary key and no two rows can have the same primary key. Primary key value can never be null nor can it be modified or updated.

### <a name="general-composite-key"/> What is the Composite Key
<b>Composite Key</b> is a form of the candidate key where a set of columns will uniquely identify every row in the table.

### <a name="general-unique-key"/> What is the Unique Key
A <b>Unique key</b> is the same as the primary key whose every row data is uniquely identified with a difference of null value i.e. Unique key allows one value as a NULL value.


## Normalization

### <a name="normalization-definition"/> Explain Normalization
The process of removing redundant data from the database by splitting the table in a well-defined manner in order to maintain data integrity. This process saves much of the storage space.

### <a name="normalization-denormalization-definition"/> Explain De-Normalization
The process of adding up redundant data on the table in order to speed up the complex queries and thus achieve better performance.

### <a name="normalization-types"/> What are the different types of Normalization?
* <b>First Normal Form (1NF):</b> A relation is said to be in 1NF only when all the entities of the table contain unique or atomic values.
* <b>Second Normal Form (2NF):</b> A relation is said to be in 2NF only if it is in 1NF and all the non-key attribute of the table is fully dependent on the primary key.
* <b>Third Normal Form (3NF):</b> A relation is said to be in 3NF only if it is in 2NF and every non-key attribute of the table is not transitively dependent on the primary key.

### <a name="normalization-bcnf"/> What is BCNF?
BCNF is the Boyce Code Normal form. It is the higher version of 3Nf which does not have any multiple overlapping candidate keys.

## Joins

### <a name="joins-inner"/> Inner JOIN
Inner JOIN is also known as a simple JOIN. This SQL query returns results from both the tables having a common value in rows.

### <a name="joins-natural"/> Natural JOIN
This is a type of Inner JOIN that returns results from both the tables having the same data values in the columns of both the tables to be joined.

### <a name="joins-cross"/> Cross JOIN
Cross JOIN returns the result as all the records where each row from the first table is combined with each row of the second table.

### <a name="joins-right"/> Right JOIN
Right JOIN is also known as Right Outer JOIN. This returns all the rows as a result from the right table even if the JOIN condition does not match any records in the left table.

### <a name="joins-left"/> Left JOIN
Left JOIN is also known as Left Outer JOIN. This returns all the rows as a result of the left table even if the JOIN condition does not match any records in the right table. This is exactly the opposite of Right JOIN.

### <a name="joins-outer-full"/> Outer/Full JOIN
Full JOIN return results in combining the result of both the Left JOIN and Right JOIN.

## SQL

### <a name="sql-definition"/> What is SQL?
Structured Query language, SQL is an ANSI(American National Standard Institute) standard programming language that is designed specifically for storing and managing the data in the relational database management system (RDBMS) using all kinds of data operations.

### <a name="sql-statements-definitions"/> How many SQL statements are used? Define them.
SQL statements are basically divided into three categories, DDL, DML, and DCL.

* <b>Data Definition Language (DDL)</b> commands are used to define the structure that holds the data. These commands are auto-committed i.e. changes done by the DDL commands on the database are saved permanently.
* <b>Data Manipulation Language (DML)</b> commands are used to manipulate the data of the database. These commands are not auto-committed and can be rolled back.
* <b>Data Control Language (DCL)</b> commands are used to control the visibility of the data in the database like revoke access permission for using data in the database.

### <a name="sql-ddl-examples"/> What are some DDL examples?
* CREATE to create a new table or database.
* ALTER for alteration.
* TRUNCATE to delete data from the table.
* DROP to drop a table.
* RENAME to rename a table.

### <a name="sql-dml-examples"/> What are some DML examples?
* INSERT to insert a new row.
* UPDATE to update an existing row.
* DELETE to delete a row.
* MERGE for merging two rows or two tables.

### <a name="sql-dcl-examples"/> What are some DCL examples?
* COMMIT to permanently save.
* ROLLBACK to undo the change.
* SAVEPOINT to save temporarily.


### <a name="sql-view-table"/> What is the difference between a View and a Table?


### <a name="sql-having-clause"/> What does the HAVING clause do?



## References

[https://www.softwaretestinghelp.com/database-interview-questions/](https://www.softwaretestinghelp.com/database-interview-questions/)





