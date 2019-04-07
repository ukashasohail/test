class cis():
    def normal_method(self,x,y):
        self.x= x
        self.y= y
        self.z = self.x + self.y
        print(self.z)

    @staticmethod
    def static_method(x,y):
        z=x+y
        print(z)

    @classmethod
    def class_method(cls,x,y):
        z=x+y
        print('class method',z)


obj = cis()
# obj.normal_method(2,4)
# cis.static_method(2,4)
# cis.class_method(2,4)