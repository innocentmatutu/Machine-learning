from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary
    #concrete method(same for all subclasses)
    def display_info(self):
        print(f'Name: {self.name}, Role: {self.get_role()}, Salary: ${self._salary}')
    @abstractmethod
    def get_role(self):
        pass #this method is implemented by all subclasses

class Manager(Person):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_role(self):
        return f'Manager (Team of {self.team_size})'
    
class Engineer(Person):
    def __init__(self, name, salary,specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def get_role(self):
        return f'Enginner ({self.specialty})'
    
if __name__ == "__main__":
    team = [
        Manager("Alice",95000,5),
        Engineer('Bob',80000,'Backend Development'),
        Engineer('Clara',85000,'Devops')
    ]
    for member in team:
        member.display_info()
