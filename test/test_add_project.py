from model.project import Project


def test_add_project(app):
    #app.session.login("administrator", "root")
    test_project = Project(name='test_project', discription='test_discription')
    app.project.add(test_project)
