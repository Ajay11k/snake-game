# class Animal:
#     def __init__(self):
#         self.eyes=2
        
#     def breathe(self):
#         print("inhale,exhale")
        
# class Fish(Animal):
    
#     def __init__(self):
#         super().__init__()
        
#     def swim(self):
#         print("moving in water")
    
#     def breathe(self):
#         print("underwater")
        

# fish = Fish()
# fish.breathe()
# print(fish.eyes)
from turtle import Turtle,Screen
import random,time

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        x = random.randint(-280,280)
        y= random.randint(-280,280)
        self.goto(x,y)
    
    def random_move(self):
        x = random.randint(-280,280)
        y= random.randint(-280,280)
        self.goto(x,y)
        

        
    
        
        
        
    