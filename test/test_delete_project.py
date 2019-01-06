from model.project import Project


def test_delete_first_project(app):
    #app.session.login("administrator", "root")
    test_project = Project(name='test_project', discription='test_discription')
    count = app.project.count()
    if count == 0:
        app.project.add(test_project)
    app.project.delete_first()


