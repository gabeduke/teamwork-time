import configparser

import easyargs
from cursesmenu import *
from cursesmenu.items import FunctionItem

from ttime import teamwork
from ttime.conf_helper import initialize_config
from ttime.user_helper import get_projects, select_projects

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
    if rebuild_projects != "false":
        print('###REBUILDING PROJECTS###')
        #get_projects()

    menu()


def menu():
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
    selection = menu()
    print(selection)
