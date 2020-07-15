import re
class planet():
    def __init__(self,name,diameter,no_of_moons,length_of_year):
        length_of_year = re.split(r"\s",length_of_year)
        self.name = name
        self.diameter = diameter
        self.no_of_moons = no_of_moons
        self.length_of_year = length_of_year

    def no_of_days(self):
        if len(self.length_of_year)==2:    
            return "Number of days in planet "+self.name+" is "+str(self.length_of_year[0])+" days"
        else:
            return "Number of days in planet "+self.name+" is "+str(int(self.length_of_year[0])*365.25)+" days "

    def radius(self):
        return "The radius of planet "+self.name+" is "+str(self.diameter/2)+" km"



def largest_planet(*planets):
    for planet in planets:
        if planet.diameter == maxi:
            print("The largest planet is "+planet.name)

mercury = planet("Mercury",4879,0,"88 days")
venus = planet("Venus",12100,0,"225 days")
earth = planet("Earth",12755,1,"365 days")
mars = planet("Mars",6786,2,"687 days")
jupiter = planet("Jupiter",142800,79,"12 earth years")
saturn = planet("Saturn",120537,82,"29.5 earth years")
uranus = planet("Uranus",51619,27,"84 earth years")
neptune = planet("Neptune",49529,14,"165 earth years")

maxi=max(mercury.diameter,venus.diameter,earth.diameter,mars.diameter,jupiter.diameter,saturn.diameter,uranus.diameter,neptune.diameter)

print(neptune.radius())
print(jupiter.no_of_days())
largest_planet(mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)


