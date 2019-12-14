class University():
    def __init__(self):
        self.name= "UEK"
    def print_name(self):
        print(self.name)
    def AGH(self, new_name):
            self.name = new_name

uni = University()
uni.print_name()
uni.AGH(input("Wprowadź nazwę:"))
uni.print_name()