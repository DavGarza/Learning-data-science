import statistics
from unicodedata import name

# Creating an empty list
numbers = []

# Accesing to the file ./data_set1 and using the reading opening mode
def main():
    with open("./file_to_operate/data_set1", "r") as x:
        for line in x:
            #Bringing the data from the file to the empty list
            numbers.append(int(line))
    #Using the added data to the list, and calculating the mean of the data
    print(statistics.mean(numbers))

#Accesing to the file ./name_set1 and overwriting it
def overwriting():
    #list to be added
    countries = ["France", "Southafrica", "Urugay", "Turkey", "New Zealand"]
    with open("./file_to_operate/name_set1", "w") as y:
        #Creating the cicle in order to add each country
        for countries in countries:
            #Adding each country
            y.write(countries)
            y.write("\n")

overwriting()

if __name__ == "__main__":
    main()