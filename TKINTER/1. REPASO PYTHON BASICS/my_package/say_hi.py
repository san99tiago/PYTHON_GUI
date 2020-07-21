#SIMPLE CLASS TO SHOW HOW TO WORK WITH PACKAGES (look "11_test_my_package.py")
#Santiago Garcia Arango
#One of the modules to show how to create a simple package in python.

class hello:
    def __init__(self, name):
        self.name = name
    
    def say_hi_to_someone(self):
        sentence = "Hello, " + self.name + "!!!"
        return sentence 
