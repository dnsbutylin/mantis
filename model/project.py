

class Project:
    def __init__(self, name=None, discription=None):
        self.name = name
        self.discription = discription

    def __repr__(self):
        return '%s:%s' % (self.name, self.discription)

