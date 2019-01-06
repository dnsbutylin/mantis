from model.project import Project


def test_delete_first_project(app, db):
    test_project = Project(name='test_project', discription='test_discription')
    count = len(db.get_project_list())
    if count == 0:
        app.project.add(test_project)
    old_projects = db.get_project_list()
    app.project.delete_first()
    new_projects = db.get_project_list()
    old_projects.remove(test_project)
    assert old_projects == new_projects

