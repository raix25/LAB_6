class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model #activity3 private attribute
        self.year = year
        pass

#activity2
    def display_info (self): #public display of the car's detail
        print("Make: {}\nModel: {}\nYear: {}".format(self.make, self.__model, self.year))
        pass
    
    def __update_model(self, new_model): #private method of changing car's model
        self.model= new_model

#activity4 
    def __str__(self):
        return (f"{self.year} {self.make} {self.__model}")



#car object 
car2 = Car("Honda", "ABC", 2025)
car2.display_info() 

