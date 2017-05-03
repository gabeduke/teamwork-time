from pick import pick

from ttime.conf_helper import add_config


def get_projects(instance, project_ids, config):
    projects = instance.get_projects()
    for project in projects:
        this_project = project['name']
        project_ids[this_project.lower()] = project['id']

    print("###ADDING PROJECT LIST TO CONFIG###")
    add_config(config, "projects", project_ids)

    for project_name, project_id in project_ids.items():
        tasks = instance.get_project_tasks(int(project_id))
        tasks_ids = {}

        for task in tasks:
            tasks_ids[task['todo-list-name']] = task['todo-list-id']

        print("###ADDING {} TASKS TO CONFIG###".format(project_name).upper())
        add_config(config, project_name.lower(), tasks_ids)


def select_projects(config):
    title = "###PROJECT LIST###"
    options = []
    config_dict = dict(config.items('projects'))
    for key, value in config_dict.items():
        options.append(key)

    option, index = pick(options, title)
    return option


def select_tasks(config, project):
    title = "###TASK LIST###"
    options = []
    config_dict = dict(config.items(project))
    for key, value in config_dict.items():
        options.append(key)

    option, index = pick(options, title)
    return option
