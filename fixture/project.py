

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add(self, project):
        wd = self.app.wd
        self.open_projects_manager()
        self.click_create_new_project()
        self.fill_project_form(project.name, project.discription)
        self.click_add_project()

    def delete_first(self):
        wd = self.app.wd
        self.open_projects_manager()
        # Выбираем проект (1й row-1), удаляем, подтверждаем удаление
        wd.find_element_by_css_selector("tr.row-1 > td > a").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

#    def project_list_is_empty(self):
#        wd = self.app.wd
#        self.open_projects_manager()
#        try:
#            wd.find_element_by_css_selector("tr.row-1 > td > a").click()
#            self.open_projects_manager()
#            return False
#        except:
#            return True

    def count(self):
        wd = self.app.wd
        self.open_projects_manager()
        c = wd.find_elements_by_css_selector('tr.row-1')
        c1 = wd.find_elements_by_css_selector('tr.row-2')
        return len(c) + len(c1) - 1

    def click_add_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_project_form(self, name, description):
        wd = self.app.wd
        wd.find_element_by_name("name").send_keys(name)
        wd.find_element_by_name("description").send_keys(description)

    def click_create_new_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def open_projects_manager(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

