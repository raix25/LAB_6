#activity7 
#importing Car class from car.py
from car import Car

def compare_car_years(car1, car2): #making a comparison 
    if car1.year < car2.year:
       return f"{car1} is older than {car2} "
    else:
        return f"{car1} is newer than {car2}"
    
#car objects
car1= Car("Toyota", "Corolla", 2020)
car2= Car("Honda", "ABC", 2025)

#diplaying the car infos
car1.display_info()
car2.display_info()

print(compare_car_years(car1,car2))