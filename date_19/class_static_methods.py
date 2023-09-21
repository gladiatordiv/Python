class Employee:
    raise_amount=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    
    @classmethod
    def setraiseamount(cls,amount):
        cls.raise_amt=amount
    

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday() == 6:
            return False
        return True
Employee.setraiseamount(1.05)
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Divya','Chauhan',50000)
# print(emp_1.raise_amt)


# emp_srt_1='Divya-chauhan-50000'
# emp_srt_2='sneha-chauhan-50000'
# emp_srt_3='sakshi-parihar-50000'

# first,last,pay=emp_srt_1.split('-')
# new_emp_1=Employee(first,last,pay)
# print(new_emp_1.__dict__)
import datetime
my_date=datetime.date(2023,9,18)
print(Employee.is_workday(my_date))



# static method example
class Math_:
    @staticmethod
    def calculate_circle_area(radius):
        return 3.14 * radius * radius
radius = 5
area = Math_.calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}.")
