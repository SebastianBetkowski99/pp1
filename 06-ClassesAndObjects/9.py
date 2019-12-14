class University():
    def __init__(self):
        self.name= "UEK"
    def print_name(self):
        print(self.name)
    #def AGH(self, new_name):
     #       self.name = new_name
    def set_fullname(self,new_fullname):
            self.fullname = new_fullname
    def print_fullname(self):
        print(self.fullname)
uni = University()
uni.set_fullname(input('Wprowadź nazwę: '))
uni.print_fullname()