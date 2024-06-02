#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    pass
    def __init__(self, name = "Simba", breed="French Bulldog"):
        self.name = name
        self.breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if(type(name) == str) and (1<=len(name)<=25):
            # print(f"Setting name to {name}.")
            self._name = name
        
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)


    def get_breed(self):
        return self._breed
 
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)


beast = Dog(name = "Beast", breed = "Beagle")
beast.name
beast.breed

beauty = Dog(name = "123")
beauty.name
beauty.name = "Lassie"
beauty.name
beauty.breed = "Pug"
beauty.breed

bosco = Dog(name = 456, breed = "Alsatian")
bosco.name = [3, 5, "hello"]

rufus = Dog(name = False)

scar = Dog(breed = "Pitbull")
