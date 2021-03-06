# APIs for Attention Statistic
APIs for Statistics of User's Attention in Learning
MySQL Database API
## Documentation
Notion:   
https://robust-trowel-8ac.notion.site/Attention-Statistics-API-1f11b5926cb34762a6ce34ef25f2e064
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
### Database Config
Before run server, create database config file first    
Config file location: {PROJECT_DIR}/app/common/config.json   
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
OpenAPI Docs - In your browser:
```
http://0.0.0.0:9000/docs
```

