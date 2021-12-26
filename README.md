# EXAMPLE PyQt5

## install requirements
```
pip install -r requirements
```

## create database mysql
```
CREATE DATABASE pyqt5;
USE pyqt5

CREATE TABLE users (
    id int AUTO_INCREMENT PRIMARY KEY,
    username varchar(100),
    email varchar(100),
    password varchar(100)
);
```

## RUN FORM
```
python form.py
```
