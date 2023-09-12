class Planet:
    def __init__(self, name, moons, radius_km, distance_from_sun_km, mass_kg):
        self.name = name
        self.moons = moons
        self.radius_km = radius_km
        self.distance_from_sun_km = distance_from_sun_km
        self.mass_kg = mass_kg
        
        

    def print_attributes(self):
        print(f"Name: {self.name}")
        print(f"Has Moons: {self.moons}")
        print(f"Radius (km): {self.radius_km}")
        print(f"Distance from Sun (km): {self.distance_from_sun_km}")
        print(f"Mass (kg): {self.mass_kg}")
        print()

def save_palnets_file(planets, file_path):
    with open(file_path, 'w') as file:
        for planet in planets:
            file.write(f"Name: {planet.name}\n")
            file.write(f"Has Moons: {planet.moons}\n")
            file.write(f"Radius (km): {planet.radius_km}\n")
            file.write(f"Distance from Sun (km): {planet.distance_from_sun_km}\n")
            file.write(f"Mass (kg): {planet.mass_kg}\n")
            file.write("\n")

def float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def yes_no_question(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ('yes', 'no'):
            return value
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")            

def main():
    planets = []

    print("⋆｡ﾟ⭐🌙🪐✨🔭☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆")
    print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ⭐🌙🪐✨🔭☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆")
    print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⭐🌙🪐✨🔭⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆")
    print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆")
    print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ⭐🌙🪐✨🔭☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⭐🌙🪐✨🔭⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆")

    while True:
        print("Create a new planet:")
        name = input("Name: ")
        moons = yes_no_question("Has Moons (yes/no): ") == 'yes'
        radius_km = float_input("Radius (km): ")
        distance_from_sun_km = float_input("Distance from Sun (km): ")
        mass_kg = float_input("Mass (kg): ")
        
        planet = Planet(name, moons, radius_km, distance_from_sun_km, mass_kg)
        planets.append(planet)
        
        save_to_file = yes_no_question("Do you want to save this planet's information to a file? (yes/no): ")
        if save_to_file == 'yes':
            file_path = input("Enter the file path: ")
            save_palnets_file(planets, file_path)
        
        another_planet = yes_no_question("Do you want to create another planet? (yes/no): ")
        if another_planet != 'yes':
            break

    print("\nInformation for all created planets:")
    for planet in planets:
        planet.print_attributes()


main()