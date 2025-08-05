class employee:
    salarry = 100000
    increment = 10000

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * self.increment   

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        slef.increment = ((salary/self.salary) -1))*100

e = employee()
#print(e.salaryAfterIncrement)
e.ssalaryAfaterIncrement
print(e.increment)