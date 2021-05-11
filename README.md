# SimplePasswordDatabase

The project is a database in which user data for different internet sites are held.
The database is a simple textfile, where data are held according to the following pattern:
"page_name,page_type,user_name,user_login,password".

Using the program you can do the following things: list data for every user for every page, list all data
grouped by a page type or print data just for one page type. You can also modify the data and introduce a new user.

The main feature of the project is that data held in the textfile are encrypted with Vigenère cipher.

The projects consists of the following files:
- main.py - this is where the user service is handled
- encrypting.py - here are placed all the functions responsible for encrypting and decrypting the database
- user.py - contains a User class
- web_page.py - contains WebPage class
- test_main.py - contains unit tests for encrypting functions and some functions in main.py
- test_user.py - contains unit tests for methods from User class

The project contains the following classes:
- User - holds information about a praticular user: name, login and password. Provides methods for 
  changing password and login, and generating a random password.
- WebPage - holds information about a particular page: name, type and a list of all users of that page, who are
  listed in the database. Provides methods for adding and removing a user from the page.
  
