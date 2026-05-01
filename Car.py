from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self ,vehicle_id , brand, model, rental_price_per_day,num_doors, feul_type):
        
        
        super().__init__(vehicle_id , brand, model, rental_price_per_day)
        
        self.num_doors = num_doors
        self.feul_type = feul_type

        
    def display_info(self):
        super().display_info()
        print("Doors", self.num_doors)
        print("Feul Type" , self.feul_type)
    def calculate_rental_cost(self,days):
        return self.rental_price_per_day * days
        
'''c1 = Car('C201' , 'Toyota' , 'Corolla' , 4000,4 , "Petrol" )
c1.display_info()
cost = c1.calculate_rental_cost(3)
print("total cost" , cost'''