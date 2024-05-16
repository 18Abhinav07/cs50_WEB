import mysql.connector
from mysql.connector import authentication

db_config = {
    'host' :'localhost',
    'user' : 'ryuk',
    'password' : 'ryuk@SQL@5',
    'auth_plugin': 'mysql_native_password',  # I have'mysql_caching_sha2_password' thus i need to specify 
     # the config file for the authentication file.  
}

database = mysql.connector.connect(**db_config)    


cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE DBMS_PROJECT")
print("All done")