import configparser
import os

import easyargs
from cursesmenu import *
from cursesmenu.items import FunctionItem
from cursesmenu.items import SubmenuItem

from ttime import teamwork
from ttime.conf_helper import initialize_config
from ttime.user_helper import get_projects, select_projects, select_tasks

configfile_name = os.getenv("HOME") + ".config.ini"

config = configparser.ConfigParser()
config.read('.config.ini')

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
    if rebuild_projects != "false":
        print('###REBUILDING PROJECTS###')
        # get_projects()

    main_menu()


def main_menu():
    # create the menu object
    this_menu = CursesMenu("Teamwork Time", "Menu")

    # create the menu items
    rebuild_projects = FunctionItem("Rebuild Project Cache", get_projects, [instance, project_ids, config])
    select_project = FunctionItem("Select Project", select_projects, [config], should_exit=True)

    # build the menu
    this_menu.append_item(rebuild_projects)
    this_menu.append_item(select_project)

    # show the menu
    this_menu.show()
    this_menu.clear_screen()
    return select_project.get_return()


if __name__ == "__main__":
    project = main_menu()
    task = select_tasks(config, project)
    task_id = config.get(project, task)

    map = {
        "entry_date": input("Date: \n"),
        "description": input("Description: \n"),
        "start_time": input("Start time: \n"),
        "duration": input("Duration: \n"),
        "is_billable": input("Billable (0 or 1): \n")
    }

    instance.save_project_task_time_entry(task_id, map["entry_date"], map["duration"], map["description"], map["start_time"])
