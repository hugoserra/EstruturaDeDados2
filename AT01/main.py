import sys

class Archive:

    def __init__(self,archive_name):
        self.archive = None
        self.archive_name = archive_name
        self.validation_status = "passed";


    def validate(self):

        self.check_if_exist()
        self.check_if_not_empty()
        self.check_first_param()
        self.check_second_param()

        if(self.validation_status == "passed"):
            return True
        else:
            self.archive = None
            return False


    def check_if_exist(self):
        if(self.validation_status != "passed"):
            return False

        try:
            archive = open(self.archive_name,'r')
            self.archive = archive
        except Exception as e:
            self.validation_status = "The chosen file does not exist."


    def check_if_not_empty(self):
        if(self.validation_status != "passed"):
            return False

        if(not self.archive.read()):
            self.validation_status = "The file appears to be empty."

        self.archive.seek(0, 0)


    def check_first_param(self):
        if(self.validation_status != "passed"):
            return False

        first_line = self.archive.readline()
        try:
            first_line = int(first_line)
        except Exception as e:
            self.validation_status = "The first parameter must be an integer"


    def check_second_param(self):
        if(self.validation_status != "passed"):
            return False

        second_line = self.archive.readline()
        if(not second_line):
            self.validation_status = "The second parameter has not been defined."
            return False

        if(len(second_line) > 2):
            self.validation_status = "The second parameter needs to be char type."
            return False

        if(not (second_line[0] == 'c' or second_line[0] == 'd' or second_line[0] == 'r')):
            self.validation_status = "The second parameter must be equal to 'c', 'd', or 'r'."


    def archive_reseted(self):
        self.archive.seek(0, 0)
        return self.archive


    def get_first_param(self):
        if(self.validation_status == "passed"):
            return int(self.archive_reseted().readlines()[0])


    def get_second_param(self):
        if(self.validation_status == "passed"):
            return self.archive_reseted().readlines()[1][0]



class SortAlgoritms:

    def __init__(self,lenght,option):
        self.lenght = lenght
        self.option = option
        print(lenght)
        print(option)




class Main:

    def __init__(self):
        self.start()


    def start(self):
        InputFile = Archive(sys.argv[1])
        if(InputFile.validate()):
            SortAlgoritms(InputFile.get_first_param(), InputFile.get_second_param())
        else:
            print(InputFile.validation_status)




MainOBJ = Main()
