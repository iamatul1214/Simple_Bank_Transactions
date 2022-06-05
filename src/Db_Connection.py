import mysql.connector


class sql_connection:   
        def __init__(self, host, username, password):
            self.host=host
            self.username=username
            self.password=password

        def connect_to_db(self,dbname):
            try:
                mydb=mysql.connector.connect(host=self.host, username=self.username,password=self.password)
                print(mydb)
                cursor=mydb.cursor()
                query = "USE ineuron_tech_assignment"
                cursor.execute(query)
                output=cursor.fetchall()
                if(len(output) ==0):
                    print(f"connected to database {dbname}")
                return mydb
            except Exception as e:
                print(f"error occured while connecting to db : {dbname} as {e}")
            # finally:
            #     if mydb.is_connected():
            #         cursor.close()
            #         mydb.close()
            #         print("Database connection is closed")
