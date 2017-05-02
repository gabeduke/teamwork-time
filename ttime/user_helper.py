from pick import pick

from ttime.conf_helper import add_config


def get_projects(instance, project_ids, config):
    projects = instance.get_projects()
    for project in projects:
        project_ids[project['name']] = project['id']

    print("###ADDING PROJECT LIST TO CONFIG###")
    add_config(config, "projects", project_ids)

    for project_name, project_id in project_ids.items():
        tasks = instance.get_project_tasks(int(project_id))
        tasks_ids = {}

        for task in tasks:
            tasks_ids[task['todo-list-name']] = task['todo-list-id']

        print("###ADDING {} TASKS TO CONFIG###".format(project_name).upper())
        add_config(config, project_name, tasks_ids)


def select_projects(config):
    title = "###PROJECT LIST###"
    options = []
    config_dict = dict(config.items('projects'))
    for key, value in config_dict.items():
        options.append(key)

    #pudb.set_trace()
    option, index = pick(options, title)
    return option
