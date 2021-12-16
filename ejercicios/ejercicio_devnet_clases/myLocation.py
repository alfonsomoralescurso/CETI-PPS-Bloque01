class Location:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " 
               + self.country + ".")


# Crea objeto de la clase Location
loc = Location("Raquel Esteve", "Italia")
loc2 = Location("Ángeles Tor", "Francia")
loc3 = Location("Fermín Bueno", "Marruecos")

loc.myLocation()
loc2.myLocation()
loc3.myLocation()

# print(loc.name)
# print(loc.country)

# print(type(loc))
