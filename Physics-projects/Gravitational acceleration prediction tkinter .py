import tkinter as tk
from tkinter import messagebox


class Inputs_Numbers:
    def __init__(self, root):
        self.root = root
        self.root.title("Gravitational Calculator")

        # Create and place widgets
        tk.Label(root, text="Planet Name:").grid(row=0, column=0)
        self.planet_name_entry = tk.Entry(root)
        self.planet_name_entry.grid(row=0, column=1)

        tk.Label(root, text="Mass (kg):").grid(row=1, column=0)
        self.mass_entry = tk.Entry(root)
        self.mass_entry.grid(row=1, column=1)

        tk.Label(root, text="Radius (meters):").grid(row=2, column=0)
        self.radius_entry = tk.Entry(root)
        self.radius_entry.grid(row=2, column=1)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_gravity)
        self.calculate_button.grid(row=3, columnspan=2)

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.grid(row=4, columnspan=2)

    def gravitational_acceleration(self, mass, radius):
        G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
        return G * mass / radius**2

    def calculate_gravity(self):
        planet_name = self.planet_name_entry.get()
        try:
            mass_of_planet = float(self.mass_entry.get())
            radius_of_planet = float(self.radius_entry.get())
            g = self.gravitational_acceleration(mass_of_planet, radius_of_planet)
            self.result_label.config(text=f"The gravitational acceleration on {planet_name} is {g:.2f} m/s^2")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numerical values for mass and radius.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Inputs_Numbers(root)
    root.mainloop()
