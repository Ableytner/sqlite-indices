# SQLite Indices
This project has been created to show the advantages of using indices when searching big databases.

# Getting started

## Generating a test database:

### TestSpeed.create_db(digits: int)
This function creates a database with two tables, both having the following properties:

* first_name: changing for each element
* sure_name: always "Smith"
* people_id: the primary key

### Example:
Passing 3 into digits will generate a database with 35152 ((26^3)*2) elements.

In this example, first_name goes from aaa to zzz, sure_name is always Smith, and people_id goes from 1 to 17576. 

All of this is happening twice, with and without indices.

## Testing search time:

### TestSpeed.start_tests(first_name: str)
This function takes the previously created database and searches for the given first_name, printing out how long searching for it took with and without indices.

**The given first_name has to have the exact number of symbols that was used as digits while creating the database!**

### Example:
Passing "rbt" into first_name takes the previously created database and measures the time it took searching with and without indices.

# Example results
Using a database with 5 digits, the following results could be measured:

* Without indices: 0.5428 s (542.8 ms)
* With indices: 0.0020 s (2 ms)
