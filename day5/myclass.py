class Myclass:
    name = " "

    def fun1(self):
        print("Hello guys....")

    def fun2(self,name):
        self.name=name

    def fun3(self):
        print("Value is ",self.name)


m1 = Myclass()
m1.fun1()
m1.fun2("Jay Kaneriya")
m1.fun3()