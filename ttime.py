from configparser import ConfigParser
import teamwork
import os
import easyargs

configfile_name = "config.yaml"


@easyargs
def main():
    """teamwork time wootwoot"""
    # Check if there is already a configuration file
    if not os.path.isfile(configfile_name):
        # Create the configuration file as it doesn't exist yet
        company = input("Please enter Company Name: ")
        api_key = input("Please enter API Key: ")

        cfgfile = open(configfile_name, 'w')

        # Add content to the file
        Config = ConfigParser.ConfigParser()
        Config.add_section('user')
        Config.set('user', 'company', company)
        Config.set('user', 'api_key', api_key)
        Config.write(cfgfile)
        cfgfile.close()


if __name__ == "__main__":
    main()
