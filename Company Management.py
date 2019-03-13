from abc import ABC, abstractmethod
 
class Employee(ABC):
 
    def __init__(self, hr_emp_sal=1.1,sl_emp_sal=1.3,mgr_sal=1.5,exec_sal=1.8,bas_sal=5000,lst = [],x ='',y = '',z1=0,x1='',z = 0):
        self. hr_emp_sal =  hr_emp_sal
        self.sl_emp_sal= sl_emp_sal
        self.mgr_sal = mgr_sal
        self.exec_sal = exec_sal
        self.bas_sal = bas_sal
        self.lst =lst
        self.x  = ''
        self.y = y
        self.z1 = 0
        self.x1  =''
        self.z = 0
        
        super(Employee, self).__init__()
        
    @abstractmethod
    def execute(self):
        pass

class HourlyEmployee(Employee):
    def execute(self):
        pass
 
 
class SalariedEmployee(Employee):
    def execute(self):
        pass 
 
 
class Manager(Employee):
    def execute(self):
        pass 
 
 
class Executive(Employee):
    def execute(self):
        pass

class Company(Employee):
        def execute(self):
            pass
        
    
        def hire(self,x,y,z=1):
                if (x,y,z) not in self.lst:
                    if  y=='Hourly Employee':
                        z = self.hr_emp_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    elif y == 'Salaried Employee':
                        z = self.sl_emp_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    elif y=='Manager':
                        z=self.mgr_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    elif  y=='Executive':
                        z=self.exec_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    else:
                        print('try again.')
                else:
                    print('Employee already exists.')
        def fire(self,x,y,z):
                if (self,x,y,z) in self.lst:
                    self.lst.remove((self,x,y,z))
                    print(f'Employee {x} removed.')
                else:
                    print('Employee not found.')

        def se(self):
               print(self.lst)

        def promotion(self,x,y,z):
                x1=x
                if (self,x,y,z) in self.lst:
                    if y=='Hourly Employee':
                        y1='Salaried Employee'
                        print(f'{x1} was promoted to {y1}.')
                        z1=self.sl_emp_sal*self.bas_sal
                        self.lst.append((self,x1,y1,z1))
                        self.lst.remove((self,x,y,z))
                    elif y=='Salaried Employee':
                        y1='Manager'
                        print(f'{x1} was promoted to {y1}.')
                        z1=self.mgr_sal*self.bas_sal
                        self.lst.append((self,x1,y1,z1))
                        self.lst.remove((self,x,y,z))
                    elif y=='Manager':
                        y1='Executive'
                        print(f'{x1} was promoted to {y1}.')
                        z1=self.exec_sal*self.bas_sal
                        self.lst.append((self,x1,y1,z1))
                        self.lst.remove((self,x,y,z))
                    else:
                        print('No promotion available.')
                else:
                    print('Employee not found.')
