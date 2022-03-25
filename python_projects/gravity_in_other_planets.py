
menu = """
What would your weight would be in other celestian bodies
Choose a celestial body

1-Sun
2-Mercury
3-Venus
4-Mars
5-Jupiter
6-Saturn
7-Uranus
8-Neptune
9-The Moon
10- Ganymede
"""

option = int(input(menu))

class celestial_body:    
    def gravity_calculation(name,acceleration):
        mass = float(input("What is your mass?"))
        weigth = mass * acceleration
        print("Your weight on", celestial_body, "would be", weigth)


if option == 1:
    sun = celestial_body
    sun.gravity_calculation("The Sun",274)
elif option == 2:
    mercury = celestial_body
    mercury.gravity_calculation("Mercury",3.7)
elif option == 3:
    venus = celestial_body
    venus.gravity_calculation("Venus",8.87)
elif option == 4:
    mars = celestial_body
    mars.gravity_calculation("Mars",3.72)
elif option == 5:
    jupiter = celestial_body
    jupiter.gravity_calculation("Jupiter",24.79)
elif option == 6:
    saturn = celestial_body
    saturn.gravity_calculation("Saturn",10.44)
elif option == 7:
    uranus = celestial_body
    uranus.gravity_calculation("Uranus",8.87)
elif option == 8:
    neptune = celestial_body
    neptune.gravity_calculation("Neptune",11.15)
elif option == 9:
    moon = celestial_body
    moon.gravity_calculation("The moon",1.62)
elif option == 10:
    ganymede = celestial_body
    ganymede.gravity_calculation("Ganymede",1.42)
else:
    print("That is not an option")
    