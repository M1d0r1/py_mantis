import random


def test_clear_projects_helper(app):
    while app.project.count()>0:
        app.project.navigate_to_manage_projects_page()
        old_projects = app.project.get_project_list()
        project = random.choice(old_projects)
        app.project.delete_by_name(project.name)

