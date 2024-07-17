def band_name_generator():
    print("Welcome to the Band Name Generator.")
    city = input("What's name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    print("Your band name could be {city} {pet}.".format(city=city, pet= pet)) 

if __name__ == "__main__":
    band_name_generator()