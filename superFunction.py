class Parent:
    def func1(self):
        print("Function 1")


class Child(Parent):
    def func2(self):
        super().func1()


ob = Child()
ob.func1()