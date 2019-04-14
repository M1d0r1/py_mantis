from model.project import Project
from utils.randomdata import RandomData
import random


def test_delete_project(app):
    if app.project.count() == 0:
        project = Project(name=RandomData.get_random_string())
        app.project.create(project)
    app.project.navigate_to_manage_projects_page()
    old_projects = app.soap.get_project_list(username=app.username, password=app.password)
    project = random.choice(old_projects)
    app.project.delete_by_name(project.name)
    new_projects = app.soap.get_project_list(username=app.username, password=app.password)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.key_by_name) == sorted(new_projects, key=Project.key_by_name)
