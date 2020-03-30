class P:
    def __init__(self,x):
        self.__x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if (x < 18):
            print("Sorry you age is below eligibility criteria")
            raise IOError
        else:
            print("Eligible")
            self.__x = x
p1 = P(int(input("Enter Your age : ")))
print(p1.x)
