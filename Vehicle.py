class Vehicle:
    total_vehicle =0
    def __init__(self ,vehicle_id , brand, model, rental_price_per_day):
        self.vehicle_id = vehicle_id 
        self.brand= brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_avilable = True
        
     
    def display_info(self):
        
        print("Vehicle ID : ",self.vehicle_id )
        print("Brand : ", self.brand)
        print("Model: ", self.model)
        
        
        
    def rent(self):
        if self.is_avilable:
            self.is_avilable = False
            print(self.vehicle_id ,self.brand , "is rented")
        else:
            print(f"Sorry" , self.vehicle_id ,"is not avialble" )
       
        
    def return_vehicle(self):
        self.is_avilable = True
        print(self.vehicle_id , "is return")
    def calculate_rental_cost(self , days):
        return self.rental_price_per_day * days


'''b1  = Vehicle('B101' , 'Honda' , 'CG125' , 1000 )
b1.display_info()
b1.rent()
b1.return_vehicle()
cost = b1.calculate_rental_cost(2)
print("Total cost" , cost)
c1  = Vehicle('C201' , 'Toyota' , 'Corolla' , 4000 )
c1.display_info()
#c1.rent()
ac1  = Vehicle('C301' , 'Honda' , 'Civic' , 6000 )
ac1.display_info()
#ac1.rent()'''

        