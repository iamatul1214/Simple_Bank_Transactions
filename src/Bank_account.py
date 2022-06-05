from Db_Connection import sql_connection
import numpy as np

class Bank_Account:
    try:
        def __init__(self,hostname,username,password,dbname):
            self.balance=5000   ## min balance required
            sql = sql_connection(host=hostname,username=username,password=password)
            self.dbObject = sql.connect_to_db(dbname)
            self.cursor = self.dbObject.cursor()
            print("*******************Welcome to the Bank**************************")
    
        def deposit(self):
            amount=float(input("\n Enter amount to be Deposited: "))
            self.balance += amount
            print(f"\n Amount Deposited : {amount}")
    
        def withdraw(self,account_id,amount):
            try:
                withdraw_amount_procedure = "Withdraw"
                args=[account_id, amount]
                cursor = self.dbObject.cursor()
                # self.cursor.callproc(withdraw_amount_procedure,args=args)
                cursor.callproc(withdraw_amount_procedure,args=args)
                # self.dbObject.commit()
                for results in cursor.stored_results():
                    print(results.fetchall())
                raise DatabaseError("Enter amount more than 0")
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
    except Exception as e:
        print(e)
    
            


if __name__ == '__main__':
    try:
        b = Bank_Account(hostname='localhost',username='root',password='Akshat1214', dbname='ineuron_tech_assignment')
    except Exception as e:
        print(e)