def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "\'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")
describe_pet(animal_type="hamster", pet_name="harry")


def describe_pet(pet_name, animal_type="dog"):
    # Display information about a pet.
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "\'s name is " + pet_name.title() + ".")

describe_pet(pet_name="willie")
describe_pet(pet_name="harry", animal_type="hamster")
