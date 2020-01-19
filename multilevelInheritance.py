class Parent:
    def func1(self):
        print("This is func1.")


class Child1(Parent):
    def func2(self):
        print("This is func2.")


class Child2(Child1):
    def func3(self):
        print("This is func3.")


ob = Child2()
ob.func1()
ob.func2()