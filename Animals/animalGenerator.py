import Animals

print("Welcome to the animal generator")
print("This program creates Animal Objects")

def main():
    # Get animal data
    animal_list = []
    find_info = True
    while(find_info):
        _animal_type = input("\nWhat type of animal would you like to create? ")
        __name = input("What is the animals name? ")
        more_animals = input("would you like to add more animals (y/n)? ")
        if (more_animals != "y"):
            find_info = False

        # Create
        animal_list.append(Animals.Animal(_animal_type, __name))

    animal = Animals.Animal(_animal_type, __name)

    # Display the data

    print("\nAnimal List:\n")
    for animal in animal_list:
        print("" + animal.get_animal_type() + " " + "the" + " " + animal.get_name() + " " + "is" + " " + animal.check_mood() + "\n")
main()
