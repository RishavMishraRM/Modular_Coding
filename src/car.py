from src.person import Person

class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    
    def display(self):
        print(f" This car is {self.name} and model is {self.model}")