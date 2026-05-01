class RentalService:

    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def register_customer(self, customer):
        self.customers.append(customer)

    def show_avilable_vehicles(self):
        for v in self.vehicles:
            if v.is_avilable:
                v.display_info()
                print("-----")

    def rent_vehicle(self, customer_id, vehicle_id, days):
        customer = None
        vehicle = None
        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                vehicle = v
        if customer and vehicle:
            customer.rent_vehicle(vehicle)
            print("Total Cost:", vehicle.calculate_rental_cost(days))
        else:
            print("Customer or Vehicle not found")

    def return_vehicle(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                c.return_vehicle()