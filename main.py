from Vehicle import Vehicle
from Car import Car
from Bike import Bike
from Customer import Customer
from RentalService import RentalService

def main():
    service = RentalService()

    v1 = Bike("B101", "Honda", "CG125", 1000, "125cc", "Standard")
    v2 = Car("C201", "Toyota", "Corolla", 4000, 4, "Petrol")
    v3 = Car("C301", "Honda", "Civic", 6000, 4, "Diesel")

    service.add_vehicle(v1)
    service.add_vehicle(v2)
    service.add_vehicle(v3)

    c1 = Customer("U1", "Ali")
    c2 = Customer("U2", "Maha")
    service.register_customer(c1)
    service.register_customer(c2)

    while True:
        print("\n1. Show Vehicles")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            service.show_avilable_vehicles()

        elif choice == "2":
            cid = input("Enter Customer ID: ")
            vid = input("Enter Vehicle ID: ")
            days = int(input("Enter days: "))
            service.rent_vehicle(cid, vid, days)

        elif choice == "3":
            cid = input("Enter Customer ID: ")
            service.return_vehicle(cid)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()