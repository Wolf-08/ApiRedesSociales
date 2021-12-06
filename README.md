# ApiRedesSociales
## Virtual Env
To star the serve first create a virtual env. The version of python that was used is 3.10
`python -m venv C:\backend\venv` and then activate the virtual env `venv\Scripts\activate`

## Development 
For run  use  `uvicorn main:app --reload`  in the path of the file main.py

## Database 
To create the database and the data for test run the file encuestas.sql that creates the database, the table, and some inserts for test the API
Just change the configuration of user and password on the file config/db.py corresponding to your enviroment of Mysql

