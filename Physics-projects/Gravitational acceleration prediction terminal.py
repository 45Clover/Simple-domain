# ok so Val flexed on me so i must flex right back .
# this code should based on my text to her ,use math to calculate the gravity of a planet given the mass and radius in SI units 

import math 

class Inputs_Numbers:
    def __init__(self):
        self.used_numbers = set()

    def gravitational_acceleration(self, mass, radius):
        G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
        return G * mass / radius**2

    def calculate_gravity(self):
        while True :
            planet_name = input("Enter the name of the planet (or type 'quit' to exit): ")
            if planet_name.lower() == 'quit':
                print("Exiting the program.")
                break
            try:
                mass_of_planet = float(input(f"Enter the mass of {planet_name} in kg: "))
                radius_of_planet = float(input(f"Enter the radius of {planet_name} in meters: "))
                g = self.gravitational_acceleration(mass_of_planet, radius_of_planet)
                print(f"The gravitational acceleration on {planet_name} is {g:.2} m/s^2")
            except ValueError:
                print("Invalid input. Please enter numerical values for mass and radius.")
 
if __name__ == "__main__":
    simulator = Inputs_Numbers()
    simulator.calculate_gravity()
   

