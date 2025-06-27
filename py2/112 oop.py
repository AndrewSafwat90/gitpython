class A:
    def meth1(self):
        print("Method 1 from class A")
        raise NotImplementedError(
            "This method should be overridden in subclasses")


class B(A):
    def meth1(self):
        print("Method 1 from class B")


s1 = B()
s1.meth1()  # This will call meth1 from class A
