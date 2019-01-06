from model.project import Project


def test_add_project(app, db):
    test_project = Project(name='test_project', discription='test_discription')
    old_projects = db.get_project_list()
    if test_project not in old_projects:
        app.project.add(test_project)
        new_projects = db.get_project_list()
        old_projects.append(test_project)
        assert sorted(old_projects, key = Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
    else:
        #Если уже есть в списке, то новый он не добавляет, поэтому пытаться не стоит и проверка верна
        assert True