class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def email(self):
        return '{}.{}@celebaltech.com'.format(self.first,self.last)
    @property
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    '''@full_name.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last'''
emp_1=Employee('Corey','Schafer')
emp_2=Employee('Divya','Chauhan')
emp_1.fullname='Sneha Chauhan'
print(emp_1.full_name)


# class python:
#     def __init__(self):
#         self._age=0
#     @property
#     def age(self):
#         print("getter")
#         return self._age
#     @age.setter
#     def age(self,x):
#         if(x<20):
#             raise ValueError("Below eligibility criteria")
#         print("setter method")   
#         self._age = x   
# John = python()   
    
# John.age = 25  
    
# print(John.age)  
