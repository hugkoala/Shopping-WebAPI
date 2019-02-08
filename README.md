Shopping-WebAPI
========



| Method |              Url                               | Description     |
| ------ | ---------------------------------------------- | --------------- |
| POST   | http://[host_name]/login                       | 會員登入          |
| POST   | http://[host_name]/cart                        | 商品加入至購物車   |
| POST   | http://[host_name]/order                       | 購物車結帳         |
| GET    | http://[host_name]/user/action_log/[user_id]   | 查詢會員購物明系列表 |
| POST   | http://[host_name]/users                       | 註冊              |
| POST   | http://[host_name]/user/credit                 | 會員增加額度       |
| GET    | http://[host_name]/user/[user_account]         | 查詢會員資料       |
| DELETE | http://[host_name]/cart                        | 購物車移除商品      |
| GET    | http://[host_name]/carts                       | 查詢購物車項目列表  |

## **Getting Started**

### **Requirements**
    flask
    hashlib
    sqlalchemy
    jsonschema
    Oracle

### **DB Setting**
+ Adjust [db.ini](src/dao/db.ini) to setting Oracle DB
+ execute [DB.sql](tests/DB.sql) to create schema


### **Console**
    git clone https://github.com/hugkoala/Shopping-WebAPI.git
    cd Shopping-WebAPI/src/
    python -u main.py

### **Unit Test**
+ [Unit Test](tests)
+ execute test_XXX.py in folder

### **Test**
+ import [shopping.postman_collection.json](tests/shopping.postman_collection.json) to Postman

    
   

