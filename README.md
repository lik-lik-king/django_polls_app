# Django Polls Application

This is a web-based application created using Django framework that allows users to view and vote in polls.

## Features

1. Users can view the list of polls.
2. Users can vote in each poll.
3. Users can view the results of each poll.
4. The application has an admin panel that allows managing (create, update, delete) the polls.

## Technology

1. Python 3
2. Django Framework
3. MySQL Database

## Installation

Before you start, make sure you have Python and pip installed on your machine.

1.  clone the repository to your local machine: `git clone https://github.com/yourusername/yourrepository.git`

2. Navigate to the project directory:


bash
Copy code
cd yourrepository
Install the required modules:

bash
Copy code
pip install -r requirements.txt
Running the Application
To start the application, navigate to the project directory and run:

bash
Copy code
python manage.py runserver
This will start the server at http://127.0.0.1:8000/.

Navigate to http://127.0.0.1:8000/polls to use the application.

## Installing Python dependencies

1. This project uses pip to manage Python dependencies.
2. Navigate to the base directory of the project, the same location as the `requirements.txt` file.
3. Run `pip install -r requirements.txt` to install all Python dependencies.

   The `requirements.txt` file includes `mysqlclient`, which is the MySQL client library that Django uses to interact with the MySQL database. It was installed with the command `pip install mysqlclient`.

   Note: `<version>` should be replaced with the version of `mysqlclient` you're using. If you're unsure, running `pip show mysqlclient` in your terminal will display information about your installed `mysqlclient` package, including the version.


## Managing Environment Variables in Django with python-dotenv

   This project uses python-dotenv to load environment variables from a .env file. In order to run this project locally, you'll need to create your own .env file in the root directory of the project and define the following variables:

Copy code
```
DJANGO_SECRET_KEY=<your Django secret key>
DB_NAME=<your database name>
DB_USER=<your database user>
DB_PASSWORD=<your database password>
DB_HOST=<your database host>
DB_PORT=<your database port>
```
Please replace <your Django secret key>, <your database name>, <your database user>, <your database password>, <your database host>, and <your database port> with your actual values.

Do not include your .env file in any version control system. It contains sensitive data that should not be shared. If you're using git, the .env file is already included in the .gitignore file and will not be tracked.

The use of environment variables and .env files is a common practice to manage project settings. It provides a few benefits:

Security: It prevents sensitive data from being shared publicly.
Flexibility: It allows each developer to have their own settings. This is particularly useful when working in a team where each developer might have their own database setup.
Organization: It helps keep configuration values separate from the codebase, which is a best practice in software development.


Enjoy the app!
