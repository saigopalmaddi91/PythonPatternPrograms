class Outer:
    def __init__(self):
        print("Outer Class Constructor invoked - Object created")

    class Inner:
        def __init__(self):
            print("Inner Class Constructor invoked - Object created")

        class NestedInner:
            def __init__(self):
                print("Nested Inner Class Constructor invoked - Object created")

            def method(self):
                print("Nested Inner Class Method Invoked....")

outer = Outer()
inner = outer.Inner()
nestedinner = inner.NestedInner()
nestedinner.method()

# Outer().Inner().NestedInner().method()