class calculater:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square is {self.n*self.n}")

    def cube(self):
        print(f"cube is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"Square root is {self.n**0.5}")

a = calculater(4)
a.square()
a.cube()
a.square_root()