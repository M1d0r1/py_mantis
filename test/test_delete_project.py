from model.project import Project
import random


def test_delete_project(app):
    app.project.navigate_to_manage_projects_page()
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_by_name(project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key = Project.key_by_name) == sorted(new_projects, key = Project.key_by_name)
