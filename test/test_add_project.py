from model.project import Project
from utils.randomdata import RandomData


def test_add_project(app, json_projects):
    app.project.navigate_to_manage_projects_page()
    new_project = json_projects
    new_project.name = json_projects.name + RandomData.get_random_string()
    old_projects = app.soap.get_project_list(username=app.username, password=app.password)
    app.project.create(new_project)
    new_projects = app.soap.get_project_list(username=app.username, password=app.password)
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.key_by_name) == sorted(new_projects, key=Project.key_by_name)
