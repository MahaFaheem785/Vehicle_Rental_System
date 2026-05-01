# 🚗 Vehicle Rental System (Python CLI)

A simple **Vehicle Rental Management System** built using Python and Object-Oriented Programming (OOP).
This application allows customers to rent and return vehicles through a command-line interface.

---

## 📌 Project Overview

This project simulates a real-world vehicle rental system where:

* Vehicles (Cars & Bikes) can be added
* Customers can register
* Customers can rent and return vehicles
* Rental cost is calculated based on number of days

It is designed to demonstrate **OOP concepts** like inheritance, encapsulation, and modular design.

---

## 🚀 Features

* 🚘 Add and manage vehicles (Car & Bike)
* 👤 Register customers
* 📋 View available vehicles
* 🔄 Rent a vehicle
* ✅ Return a vehicle
* 💰 Rental price calculation based on days
* 🧩 Clean modular structure

---

## 🗂️ Project Structure

```
VehicleRentalSystem/
│── main.py                # Entry point (CLI menu)
│── Vehicle.py             # Base class
│── Car.py                 # Car class (inherits Vehicle)
│── Bike.py                # Bike class (inherits Vehicle)
│── Customer.py            # Customer class
│── RentalService.py       # Core business logic
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Clone the repository:

```
git clone https://github.com/MahaFaheem785/Vehicle_Rental_System
```

3. Go to project folder:

```
cd VehicleRentalSystem
```

4. Run the application:

```
python main.py
```

---

##  How It Works

* User selects options from menu
* System shows available vehicles
* Customer enters ID and selects vehicle
* Rental is processed for given number of days
* Vehicle status updates automatically
* Customer can return vehicle anytime

---

## 🧠 OOP Concepts Used

* **Inheritance** → Car & Bike inherit from Vehicle
* **Encapsulation** → Data handled inside classes
* **Abstraction** → RentalService manages system logic
* **Modularity** → Separate files for each component

---

##  Future Improvements

* Add input validation (invalid IDs, wrong inputs)
* Add exception handling
* Store data using files or database
* Add admin panel features
* Convert CLI to GUI (Tkinter / Web App)

---

##  Learning Purpose

This project is great for learning:

* Python OOP
* Real-world system design
* CLI-based applications
* Code modularization

---

## 👨‍💻 Author

Maha faheem

---

## ⭐ Support

If you like this project, give it a  on GitHub!
