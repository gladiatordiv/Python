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

class developer(Employee):
    raise_amt=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,prog_lang,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.full_name)
# dev_1=developer('divya','chauhan',50000,'Python')
# dev_2=developer('Sakshi','Parihar',50000,'Java')
# mgr_1=Manager('sneha','chauhan',50000,[dev_1])
# print(mgr_1.first)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
