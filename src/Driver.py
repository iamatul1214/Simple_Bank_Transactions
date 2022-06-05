import argparse
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
    b.display_amount(account_id=2002)
    # b.withdraw(account_id=2001, amount=4000)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()


