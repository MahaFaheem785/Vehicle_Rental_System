from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self ,vehicle_id , brand, model, rental_price_per_day,engine_capacity, bike_type):
        
        
        super().__init__(vehicle_id , brand, model, rental_price_per_day)
        

        self.engine_capacity = engine_capacity
        self.bike_type = bike_type
        
    def display_info(self):
        super().display_info()
        print("Engine Capacity", self.engine_capacity)
        print("Bike Type" , self.bike_type)
    def calculate_rental_cost(self,days):
        return self.rental_price_per_day * days
'''b1  = Bike('B101' , 'Honda' , 'CG125' , 1000, 'Aone ' , 23 )
b1.display_info()


cost = b1.calculate_rental_cost(2)
print("Total cost" , cost)'''

    
