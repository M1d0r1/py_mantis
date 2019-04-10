class Project:
    def __init__(self, name, status = "development", inherit = True, view_status = "public", description = "default"):
        self.name = name
        self.status = status
        self.inherit = inherit
        self.view_status = view_status
        self.description = description

    def __eq__(self, other):
        return (self.name == other.name)

    def __repr__(self):
        return "Project:name=%s" % (self.name)

    def return_name(self):
        return self.name
