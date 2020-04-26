### **HOW TO START**
- `python app.py`

### **TO MAKE THIS WORK(CRUD OPERATIONS).**
1. need **mysql** db with root as username and no password.(or change credentials in config.py)
2. create **flaskdb** schema
    - ```create database flaskdb;```
3. create table 'cdr'.
    - `create table cdr(
        cdr_id INT NOT NULL AUTO_INCREMENT,
        origin_num INT,
        termi_num INT,
        call_duration DECIMAL,
        PRIMARY KEY ( cdr_id ));`

### **APIs:**
1. Get all CDRs.
    - **GET** - http://127.0.0.1:5000/
2. Get CDR.
    - **GET** - http://127.0.0.1:5000/cdr/<ID>
3. Delete CDR.
    - **DELETE** - http://127.0.0.1:5000/cdr/<ID>
4. Create CDR.
    - **POST** - http://127.0.0.1:5000/save
        - Content-Type: application/json
        - Payload: `{"termi_num": 123, "origin_num": 456, "call_duration":10 }`

**Useful**: `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';`