# SQL injection vulnerability allowing login bypass

### Given:

- SQL injection vulnerability in login function.

### Task:

- perform SQL injectio that logs in to the application as the administrator

### Analysis:
--------------

- we have a login page in my account section with username and password fields.
- fuzz username field with 'administrator' and password field with single quote('), we get 500 internal server error. i.e. vulnerability is confirmed.
- the basic query could be `SELECT * FROM USERS WHERE username='some_username' and password='some_password'`
- inserting username as administrator and commenting out the rest of the query part:
    `SELECT * FROM USERS WHERE username='administrator'-- -' and password='some_password'`

- remember to add ' to close the username's string part.

- payload => administrator'-- -

=> task completed, logged in as administrator.

