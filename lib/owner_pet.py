# lib/owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        
        # Add this instance to the class variable `all`
        Pet.all.append(self)

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # List to store owned pets

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        # Check if the pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        
        self._pets.append(pet)
        pet.owner = self  # Set the owner for the pet

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name={self.name})"
