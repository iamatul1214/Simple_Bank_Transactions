from Db_Connection import sql_connection
import numpy as np
import pandas as pd
from datetime import datetime
import os

class Bank_Account:
    try:
        def __init__(self,hostname,username,password,dbname):
            self.balance=5000   ## min balance required
            sql = sql_connection(host=hostname,username=username,password=password)
            self.dbObject = sql.connect_to_db(dbname)
            self.cursor = self.dbObject.cursor()
            print("*******************Welcome to the Bank**************************")
    
        def deposit(self):
            pass
    
        def withdraw(self,account_id,amount):
            try:
                withdraw_amount_procedure = "Withdraw"
                args=[account_id, amount]
                cursor = self.dbObject.cursor()
                # self.cursor.callproc(withdraw_amount_procedure,args=args)
                cursor.callproc(withdraw_amount_procedure,args=args)
                self.dbObject.commit()
                print(f"Withdrawal of amount {amount} is successfull")
                for results in cursor.stored_results():
                    print(results.fetchall())
                # raise DatabaseError("Enter amount more than 0")
            except Exception as e:
                print(f"Error occured while withdrawing {e}")
            finally:
                cursor.close()
    
        def display_amount(self,account_id):
            try:
                withdraw_procedure = 'display_amount'
                args = [account_id]
                cursor = self.dbObject.cursor()
                # self.cursor.callproc(withdraw_procedure,args=args)
                cursor.callproc(withdraw_procedure,args=args)
                for results in cursor.stored_results():
                    result = np.float_(results.fetchall())
                    amount = result[0][0]
                print(f"Amount in the bank account is = Rs {amount}")
            except Exception as e:
                print(f"Exception occured while retrieving the balance amount {e}")
            finally:
                cursor.close()

        def retrieve_transactions(self,from_date,to_date):
            try:
                trans_history = 'transaction_history'
                args=[from_date,to_date]
                transactions=[]
                cursor = self.dbObject.cursor()
                cursor.callproc(trans_history,args=args)
                for results in cursor.stored_results():
                    result = results.fetchall()
                for result in result:
                    print(result)
                    transactions.append(result)
                df = pd.DataFrame(transactions,columns=['Date','user_id','bank_account_id','withdrawn_amt'])
                print(f"The transacation details from {from_date} to {to_date} looks like :\n\n {df}")

                ## saving the transaction into excel
                time = datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")
                filename = time +'_'+"transaction"+".csv"
                filename = os.path.join("account_statement",filename)
                df.to_csv(filename)
                print(f"Saved the transaction dataframe into excel file at location : {filename}")

            except Exception as e:
                print(f"Exception occured while retreiving the transcations by calling procedure {trans_history} : {e}")
            finally:
                cursor.close()


        def insert_record(self,table_name,values):
            try:
                # values = (1005,'2005', '3005',1,8500)
                query = f"INSERT INTO {table_name} VALUES {values}"
                cursor = self.dbObject.cursor()
                cursor.execute(query)
                self.dbObject.commit()
                print("record inserted")
            except Exception as e:
                self.dbObject.rollback()
                print(f"Exception occured while inserting records into the table {table_name} : {e}")
            finally:
                cursor.close()
    


        def insert_bulk_records(self,table_name,list_values):
            try:
                for i in range(len(list_values)):
                    # print(f"First set of values to be inserted = {list_values[i]}")
                    query = f"INSERT INTO {table_name} VALUES {list_values[i]}"
                    print(query)
                    # query = "INSERT INTO bank_account VALUES (%i,%i)"
                    cursor = self.dbObject.cursor()
                    cursor.execute(query)
                    self.dbObject.commit()
                    print(f" {i+1} record inserted")

            except Exception as e:
                 self.dbObject.rollback()
                 print(f"Exception occured while inserting records as bulk into the table {table_name} : {e}")
            finally:
                cursor.close()
    
    except Exception as e:
        print(e)
            


if __name__ == '__main__':
    try:
        b = Bank_Account(hostname='localhost',username='root',password='Akshat1214', dbname='ineuron_tech_assignment')
    except Exception as e:
        print(e)