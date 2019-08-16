# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Learning Objectives
* What is Unit testing and how to implement it in a large project
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
* How to create a MySQL database
* How to create a MySQL user and grant it privileges
* What ORM means
* How to map a Python Class to a MySQL table
* How to handle 2 different storage engines with the same codebase
* How to use environment variables

### Requirements
## Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge cases

## SQL Scripts
* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
* Your files will be executed with SQLAlchemy version 1.2.x
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc

### More Info
![info0](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png)

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

### 0. Fork me if you can!
In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:

* “Who did this code?”
* “How it works?”
* “Where are unittests?”
* “Where is this?”
* “Why did they do that like this?”
* “I don’t understand anything.”
* “… I will refactor everything…”
But the worst thing you could possibly do is to redo everything. Please don’t do that! Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!

For this project you will fork this codebase:

* update the repository name to AirBnB_clone_v2
* update the README.md with your information but don’t delete the initial authors
If you are the owner of this repository, please create a new repository named AirBnB_clone_v2 with the same content of AirBnB_clone

### 1 Bug free!
### 2. Console improvements
### 3. MySQL setup development 
### 4. MySQL setup test
### 5. Delete object 
### 6. Delete object 
### 7. DBStorage - User
### 8. DBStorage - Place
### 9. DBStorage - Review
### 10. DBStorage - Amenity... and BOOM!

#### Authors
* [George Solorio](https://github.com/GeorgeSolorio)
* [Tim Assavarat](https://github.com/tassavarat)
