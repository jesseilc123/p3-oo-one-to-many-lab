class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if pet_type not in Pet.PET_TYPES:
            raise Exception

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self

    def sort_pets_by_name(self):
        if self.name != self:
            raise Exception
        return sorted(Pet.all, key=lambda x: x.name) 
  
    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda x: x.name)