class cis():
    def normal_method(self,x,y):
        self.x = x
        self.y = y
        self.z =self.x + self.y
        print(self.z)

    @staticmethod
    def static_method(x,y):
        z=x+y
        print(z)

    @classmethod
    def class_method(cls,x,y):
        z=x+y
        print(z)

obj = cis()
# obj.normal_method(2,4)
# obj.static_method(4,6)
obj.class_method(10,20)