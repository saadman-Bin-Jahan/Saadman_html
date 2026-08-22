class IOString():
    
    def __init__(self):
        self.stri = ""
        
    def get_String(self):
        self.stri = input("Enter String : ")
    
    def print_String(self):
        print("Result is : ", self.stri.upper())
        
strl = IOString()

strl.get_String()
strl.print_String()