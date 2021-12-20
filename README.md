# APIs for Attention Statistic
APIs for Statistics of User's Attention in Learning
MySQL Database API
## Environments
* Ubuntu 20.04 or Mac
* Python >= 3.8
## Requirements
### MySQL
Required MySQL Client, libmysqlclient-dev   
Ubuntu:
```bash
$ sudo apt-get install mysql-client libmysqlclient-dev
```
### Python3 Dependencies
```bash
$ pip3 install -r requirements.txt
```
#### Dependencies List:
```
* fastapi
* mysql-connector-python
* mysqlclient
* SQLAlchemy
* uvicorn   
```
   
If python version < 3.8:
```bash
$ pip3 install typing_extensions
```
### Database Config
Before run server, create database config file first.   
Config file location: {PROJECT_DIR}/app/common/config.json.  
format:
```json
{
  "Database": {
    "MYSQL_USER": "username",
    "MYSQL_PASSWORD": "password",
    "MYSQL_HOST": "host url",
    "MYSQL_PORT": 3306,
    "MYSQL_DATABASE": "database name"
  }
}
```
## Usage
Running Server:
```bash
$ python3 app/main.py
```
In your browser:
```
http://0.0.0.0:9000/{API URL}
```
## Documentation
In your browser:
```
http://0.0.0.0:9000/docs
```
If you access root page, redirect at docs page.
