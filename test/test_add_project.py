from model.project import Project
from utils.randomdata import RandomData


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.navigate_to_manage_projects_page()
    new_project = Project(name="Name " + RandomData.get_random_string(), status="stable", inherit=True, view_status="public", description="Desc")
    old_projects = app.project.get_project_list()
    app.project.create(new_project)
    new_projects = app.project.get_project_list()
    old_projects.append(new_project)
    print(old_projects)
    print(new_projects)
    assert sorted(old_projects, key = Project.return_name) == sorted(new_projects, key = Project.return_name)
