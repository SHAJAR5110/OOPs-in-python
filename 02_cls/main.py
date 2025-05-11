class car:
    
    count=0
    
    def __init__(self,name,color,year):
        self.name=name
        self.color=color
        self.year=year
        car.count+=1
        
    #call this method when you want to print car information
    def car_info(self):
        print(f"Car Name: {self.name}\nCar Color: {self.color}\nCar Year: {self.year}")    
    
    @classmethod
    def car_count(cls):
        print(f"Total Cars: {cls.count}")    
    
#Count print 0(Zero) here because we are not creating any object yet
print("Count Before Creating Object")
car.car_count()    

#Here we are creating 3 objects 
car1=car("BMW","Black",2020)
car2=car("Audi","Red",2021)
car3=car("Mercedes","White",2022)       


#Count print 3(Three) here because we are creating 3 objects
print("Count After Creating Object")
car.car_count()
