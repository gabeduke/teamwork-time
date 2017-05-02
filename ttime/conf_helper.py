import os


def initialize_config(config, configfile_name):
    # Check if there is already a configuration file
    if not os.path.isfile(configfile_name):
        # Create the configuration file as it doesn't exist yet
        company = input("Please enter Company Name: ")
        api_key = input("Please enter API Key: ")
        config['user'] = {
            'company': company,
            'api_key': api_key
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


def add_config(config, section, conf):
    assert isinstance(conf, dict)
    config[section] = conf

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
