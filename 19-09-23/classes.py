class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Divya','Chauhan',50000)
print(emp_1.__dict__)