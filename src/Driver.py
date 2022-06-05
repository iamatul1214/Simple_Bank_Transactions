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
    values_bulk = [(1007,2007, 3007,1,5000),(1008,2008, 30068,1,6750)]
    print(type(values_bulk))
    b.insert_bulk_records(table_name='bank_account',list_values=values_bulk)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()
    main(config_path=parsed_args.config)


