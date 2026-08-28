class FamilyMember:
    def __init__(self, eyecolour, height):
        self.eyecolour = eyecolour
        self.height = height
        
class Kid(member):
    def __init__(self, eyecolour, height, name, age, hobby):
        self.name = name
        self.age = age
        super().__init__(eyecolour, height)
        print(f"Ts kid:s name is (self.name).")
        print(f"His age is(self.age).")
        print(f"(self.name) likes (hobby).")
        print(f"His eye colour is (eyecolour) and his height is (height)cm")
        print(issubclass(Kid, familymember))