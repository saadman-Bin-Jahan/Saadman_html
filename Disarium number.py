class Disarium:
    def __init__(self, number):
        self.number = number

    def is_disarium(self):
        digits = str(self.number)
        total = sum(int(digit) ** (i+1) for i, digit in enumerate(digits))
        return total == self.number

    def show(self):
        if self.is_disarium():
            print(self.number, "is a Disarium number")
        else:
            print(self.number, "is NOT a Disarium number")

nums = [89, 135, 75, 518]
for n in nums:
    Disarium(n).show()
