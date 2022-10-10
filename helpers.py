import yaml


def get_db_configs(config_file):
    """
    get db config from yml file
    args: 
        - config_file: config file path
    returns:
        - host
        - db
        - user
        - password
    """
    with open(f"{config_file}", "r") as stream:
        try:
            db_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return db_config["host"], db_config["db"], db_config["user"], db_config["password"]
