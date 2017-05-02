import configparser

import easyargs
import pudb
from cursesmenu import *
from cursesmenu.items import FunctionItem

from ttime import teamwork
from ttime.conf_helper import *
from pick import pick

configfile_name = "config.ini"

config = configparser.ConfigParser()
config.read('config.ini')

initialize_config(config, configfile_name)
project_ids = {}
base_uri = config['user']['company'] + ".teamwork.com"
api_key = config['user']['api_key']
instance = teamwork.Teamwork(base_uri, api_key)

@easyargs
def main(rebuild_projects="false"):
    """
    teamwork time wootwoot
    :param rebuild_projects: rebuild the project list cache
    """
    if rebuild_projects == "true":
        print('###REBUILDING PROJECTS###')
        get_projects()

    menu()


def select_project():
    title = "###PROJECT LIST###"
    options = []
    config_dict = dict(config.items('projects'))
    for key, value in config_dict:
        options.append(key)

    option, index = pick(options, title)


def get_projects():
    projects = instance.get_projects()
    for project in projects:
        project_ids[project['name']] = project['id']

    print("###ADDING PROJECT LIST TO CONFIG###")
    add_config(config, "projects", project_ids)

    # pudb.set_trace()
    for project_name, project_id in project_ids.items():
        tasks = instance.get_project_tasks(int(project_id))
        tasks_ids = {}

        for task in tasks:
            tasks_ids[task['todo-list-name']] = task['todo-list-id']

        print("###ADDING {} TASKS TO CONFIG###".format(project_name).upper())
        add_config(config, project_name, tasks_ids)



def menu():
    # create the menu object
    this_menu = CursesMenu("Teamwork Time", "Menu")

    # create the menu items
    rebuild_projects = FunctionItem("Rebuild Project Cache", get_projects())
    select_project = FunctionItem("Select Project", select_project())

    # build the menu
    this_menu.append_item(rebuild_projects)
    this_menu.append_item(select_project)

    # show the menu
    this_menu.show()


if __name__ == "__main__":
    main()
