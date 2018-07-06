class adder:
    result = 0
    def add(self , num):
        self.result = self.result +  num
        return self.result
myAdd = adder()
print(myAdd.add(9))
print(myAdd.add(2))

myAdd2 = adder()
print(myAdd.add(19))
print(myAdd.add(22))

myAdd3 = adder()
print(myAdd.add(409))
print(myAdd.add(22))