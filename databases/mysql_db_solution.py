from mysql import connector
import os

class MySQLDB():
    
    USER = os.environ['PASSWORD_DB']
    PASSWORD =""
    HOST = os.environ['HOST_NAME']
    DATA_BASE = "mydatabase_python"
    
    def __init__(self):
        self.create_database(self.DATA_BASE)
        
    def create_database(self,db_name):
        try:
            mydb = connector.connect(
                host=self.HOST,
                user=self.USER,
                password=self.PASSWORD
            )

            mycursor = mydb.cursor()
            query_sql = "CREATE DATABASE " + db_name
            
            mycursor.execute(query_sql)
        except connector.errors.DatabaseError:
            print("The DB mydatabase_python alredy exist")
        
    def connection_db(self):
        mydb = connector.connect(
            host=self.HOST,
            user=self.USER,
            password=self.PASSWORD,
            database=self.DATA_BASE
        )    
        
        return mydb
    
    def run_query(self,query):
        mydb = self.connection_db()
        
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        print("Query executed")
        for x in myresult:
            print(x)
        
        return myresult
        
    def insert_values(self,values):
        mydb = self.connection_db()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        mycursor = mydb.cursor()
        mycursor.execute(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        
if __name__ == "__main__":
    obj = MySQLDB()
    
    #create table
    #obj.run_query("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    #show tables
    obj.run_query("SHOW TABLES")
    #Insert into
    val = ("John P", "Highway 23",)
    obj.insert_values(val)
    #select all
    obj.run_query("SELECT * FROM customers")
    #selec and where
    obj.run_query("SELECT * FROM customers WHERE address ='Highway 21'")
    obj.run_query("SELECT * FROM customers ORDER BY name")
    
        
               