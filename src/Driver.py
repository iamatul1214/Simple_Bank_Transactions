import argparse
import yaml
from Bank_account import Bank_Account
def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    print(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def main(config_path):
    config = read_yaml(config_path)
    hostname = config['DB']['hostname']
    username = config['DB']['username']
    password = config['DB']['password']
    db_name = config['DB']['db_name']

    print("executing driver")
    b = Bank_Account(hostname=hostname,username = username,password=password, dbname=db_name)
    # b.display_amount(account_id=2002)
    # b.withdraw(account_id=2002, amount=1)
    # b.display_amount(account_id=2002)
    # values = (1006,2006, 3006,1,50000)
    # b.insert_record(table_name='bank_account',values=values)
    # values_bulk = [(1007,2007, 3007,1,5000),(1008,2008, 30068,1,6750)]
    # print(type(values_bulk))
    # b.insert_bulk_records(table_name='bank_account',list_values=values_bulk)
    
    print("\n*********CHOOSE FROM BELOW OPTIONS***************\n")
    # print(" Press 1 to check balance \n Press 2 to withdraw amount \n Press 3 to insert a record\n Press 4 to exit")
    # user_choice = int(input("Enter your choice from above menu"))
    user_choice = 0
    while user_choice != 4:
        print(" Press 1 to check balance \n Press 2 to withdraw amount \n Press 3 to insert a record\n Press 4 to exit")
        user_choice = int(input("Enter your choice from above menu"))
        if user_choice == 1:
            account_id = int(input("Please enter the account id to check the balance"))
            b.display_amount(account_id=account_id)
        elif user_choice == 2:
            account_id = int(input("Please enter the account id to withdraw money from"))
            amount=int(input("Please enter the amount to withdraw"))
            b.withdraw(account_id = account_id, amount = amount)
        elif user_choice == 3:
            table_name = str(input("Enter the table name eg- bank_account"))
            userid = int(input("Please enter the user id"))
            account_id = int(input("Please enter the account id"))
            account_num = int(input("Please enter the account number"))
            user_active = int(input("Please enter 0 if user not active and 1 if user is active"))
            amount = int(input("Please enter the amount"))
            values = (userid,account_id,account_num,user_active,amount)
            b.insert_record(table_name=table_name, values=values)
        elif user_choice==4:
            print("Exiting the menu........")
            break
        else:
            print("\nInvalid choice entered\n")





if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()
    main(config_path=parsed_args.config)


