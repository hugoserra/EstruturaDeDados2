from Libs.Database import DatabaseFixedSize,DatabaseFixedFields,DatabaseSizeBytes,DatabaseDelimiter
class SGBD:

    def __init__(self,type="fixed_size"):
        self.type = type
        self.database = None
        self.config()

    def config(self):
        if(self.type == "fixed_size"):
            self.database = DatabaseFixedSize()
            self.database.set_database_archive("Data/DB_fixed_size.txt")
        elif(self.type == "fixed_fields"):
            self.database = DatabaseFixedFields()
            self.database.set_database_archive("Data/DB_fixed_fields.txt")
        elif(self.type == "size_in_bytes"):
            self.database = DatabaseSizeBytes()
            self.database.set_database_archive("Data/DB_size_bytes.txt")
        elif(self.type == "delimiter"):
            self.database = DatabaseDelimiter()
            self.database.set_database_archive("Data/DB_delimiter.txt")

    def set_attribute(self,name,value):
        self.database.register.set_attribute(name,value)

    def write(self):
        self.database.write()

    def read(self):
        return self.database.read()
