# Papysql


This Library is an interface between Pandas and sqlite3. It gives the possibility to access sql databases and view the tables as pandas DataFrames.

## Installation

The library can be installed through pip:

```
pip install papysql
```  

Alternatively you can download the scripts from here, the main functions are located in papysql/papysql.py file that you can place in the same folder and import in your workspace..

After importing the library it have to read the database with the command

```
import papysql as pps

db = pps.read(PathToDb)

```

You can then access data in the db with functions list_tables and display_table e.g.


```
pps.list_tables(db)
#It lists all the tables in the database

pps.display_table(NameOfTheTable,db)
#It returns the specific table in format of a Pandas Dataframe Object

```
Finally the Function ExecuteScriptFromFile is work in progress and serves to execute a SQL script from a text file

Future implementation will be aimed at modify and creating tables
