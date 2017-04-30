import configparser
from teamwork import teamwork
import os
import easyargs
import pudb

configfile_name = "config.ini"
project_ids = {}

# Check if there is already a configuration file
if not os.path.isfile(configfile_name):
    # Create the configuration file as it doesn't exist yet
    company = input("Please enter Company Name: ")
    api_key = input("Please enter API Key: ")
    set_config = configparser.ConfigParser()
    set_config['user'] = {
        'company': company,
        'api_key': api_key
    }
    with open('config.ini', 'w') as configfile:
        set_config.write(configfile)

config = configparser.ConfigParser()
config.read('config.ini')

company_url = config['user']['company'] + ".teamwork.com"
api_key = config['user']['api_key']
instance = teamwork.Teamwork(company_url, api_key)


@easyargs
def main():
    """teamwork time wootwoot"""
    get_projects()


def get_projects():
    projects = instance.get_projects()
    for project in projects:
        project_ids[project['name']] = project['id']

    for name, id in project_ids.items():
        print("Project name: " + name)
        print(instance.get_project_times(int(id)))

if __name__ == "__main__":
    main()
