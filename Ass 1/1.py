while 1:
    try:
        class rectangle:
            a = int(input())
            b = int(input())
            def area(self):
                return self.a*self.b
            def perimeter(self):
                return 2*(self.a+self.b)
        a = rectangle()
        print(a.area())
        break
    except:
        print("Invalid")