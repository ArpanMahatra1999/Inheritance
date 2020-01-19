class Parent1:
    def func1(self):
        print("This is func1.")


class Parent2:
    def func2(self):
        print("This is func2.")


class Child(Parent1,Parent2):
    def func3(self):
        print("This is func3.")


ob = Child()
ob.func1()
ob.func2()