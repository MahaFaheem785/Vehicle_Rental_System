class Customer:
    def __init__(self ,customer_id, name):
        self.customer_id = customer_id
        self.name= name
        self.rented_vehicle = None
        
    def rent_vehicle(self ,vehicle):
        
        if vehicle.is_avilable:
            vehicle.rent()
            self.rented_vehicle = vehicle
            print("vehicle rented successfully ")
        else:
            print("vehicle is not available select another")
            
    def return_vehicle(self):
        if self.rented_vehicle:
            self.rented_vehicle.return_vehicle()
            self.rented_vehicle = None
            print("Vehicel return successfully")
        else:
            print("No vehicle returned")
            
            
        
    def view_rented_vehicle(self):
        if self.rented_vehicle:
            print(self.rented_vehicle , "vehicle has rented")
            self.rented_vehicle.display_info()
        else:
            print("No vehicle rented")

'''c1 = Customer(1 ,'maha' )
##c1.rent_vehicle()
c1.return_vehicle()
c1.view_rented_vehicle()'''
    

