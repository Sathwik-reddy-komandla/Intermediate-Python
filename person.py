class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def __str__(self) -> str:
        return 'Hello I am person'


class Worker(Person):

    def __init__(self,name,age,role,salary):
        super().__init__(name,age)
        self.role=role
        self.salary=salary

    def cal_yearly_salary(self):
        return self.salary*12


worker=Worker('sathwik',21,'Engineer',1200000)

print(worker.cal_yearly_salary())