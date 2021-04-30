import random
# challenge: Animal Class

class Animal:
    def __init__(self, name, typeAna):
        self._name = name
        self.mood = self.__mood()
        self._animal_type = typeAna

    def _amimal_type(self, typeAna):
        self._animal_type = typeAna

    def __mood(self):
        random_number = random.randint(1, 3)
        if random_number == 1:
            return "happy"
                
        elif random_number == 2:
            return "sleepy"
            
        else:
            return "hungry"

    def get_animal_type(self):
        return self._animal_type

    def get_name(self):
        return self._name


    def check_mood(self):
        return self.mood

        

