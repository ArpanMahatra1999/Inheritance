class Parent:
    def func1(self):
        print("This is func1.")


class Child1(Parent):
    def func2(self):
        print("This is func2.")


class Child2(Parent):
    def func3(self):
        print("This is func3.")


ob1 = Child1()
ob2 = Child2()
ob1.func1()
ob2.func1()