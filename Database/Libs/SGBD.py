from Libs.Database import DatabaseFixedSize,DatabaseFixedFields,DatabaseSizeBytes
class SGBD:

    def __init__(self,type="fixed_size"):
        self.type = type
        self.database = None
        self.config()

    def config(self):
        if(self.type == "fixed_size"):
            self.database = DatabaseFixedSize()
            self.database.set_database_archive("Metadados/DB_fixed_size.txt")
        elif(self.type == "fixed_fields"):
            self.database = DatabaseFixedFields()
            self.database.set_database_archive("Metadados/DB_fixed_fields.txt")
        elif(self.type == "size_in_bytes"):
            self.database = DatabaseSizeBytes()
            self.database.set_database_archive("Metadados/DB_size_bytes.txt")

    def set_attribute(self,name,value):
        self.database.register.set_attribute(name,value)

    def write(self):
        self.database.write()

    def read(self):
        return self.database.read()
