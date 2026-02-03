# 1. Define the super class Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# 2. Define the subclass Automobile which inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Initialize the super class (Vehicle)
        super().__init__(vehicle_type)
        # Initialize attributes specific to Automobile
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# 3. Main function to run the app
def main():
    print("Please enter the details for your car.")
    
    # Hardcode the vehicle type as "car" per the instructions
    vehicle_type = "car"
    
    # Get user input for the remaining attributes
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    
    # Create an instance of the Automobile class with the data
    my_car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Output the data in the readable format
    print("\n" + "="*20)
    print(f"Vehicle type: {my_car.vehicle_type}")
    print(f"Year: {my_car.year}")
    print(f"Make: {my_car.make}")
    print(f"Model: {my_car.model}")
    print(f"Number of doors: {my_car.doors}")
    print(f"Type of roof: {my_car.roof}")

# Run the app
if __name__ == "__main__":
    main()