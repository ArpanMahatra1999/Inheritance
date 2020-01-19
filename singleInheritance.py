class Parent:
    def func1(self):
        print("This is func1.")


class Child(Parent):
    def func2(self):
        print("This is func2.")


ob = Child()
ob.func1()