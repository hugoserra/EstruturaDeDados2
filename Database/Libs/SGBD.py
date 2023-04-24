from Libs.Database import DatabaseFixed
class SGBD:

    def __init__(self,type="fixed"):
        self.type = type
        self.database = None
        self.config()

    def config(self):
        if(self.type == "fixed"):
            self.database = DatabaseFixed()
            self.database.set_database_archive("Metadados/DB.txt")

    def set_attribute(self,name,value):
        self.database.register.set_attribute(name,value)

    def write(self):
        self.database.write()

    def read(self):
        return self.database.read()
