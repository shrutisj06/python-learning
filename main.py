class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def show_Details(self):
        print("role:",self.role)
        print("department:",self.department)
        print("salary:",self.salary)


class Engineer(Employee):
    def __init__(self, name, age,role,department,salary ):
        self.name=name
        self.age=age
        super().__init__(role,department,salary)
        super().show_Details()

emp1=Engineer("shruti",19,"developer","IT",50000)
print("name:",emp1.name)
print("age:",emp1.age)
print("role:",emp1.role)
print("department:",emp1.department)
print("salary:",emp1.salary)

emp2=Engineer("dimple",20,"HR","ABC",40000)

print("name:",emp2.name)
print("age:",emp2.age)
print("role:",emp2.role)
print("deparment:",emp2.department)
print("salary:",emp2.salary)
