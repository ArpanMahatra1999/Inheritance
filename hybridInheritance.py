class Parent:
    def func1(self):
        print("func1")


class Child1(Parent):
    def func2(self):
        print("func2")


class Parent2:
    def func3(self):
        print("func3")


class Child2(Parent, Parent2):
    def func4(self):
        print("func4")


ob1 = Child1()
ob1.func1()

ob2 = Child2()
ob2.func1()
ob2.func3()