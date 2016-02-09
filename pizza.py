# def make_pizza(*toppings):
#     print("")
#     # Print the list of toppings that have been requested.
#     print(toppings)
#     # Summarize the pizza we are about to make.
#     print("Making a pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza("pepperoni")
# make_pizza("mushroom", "green peppers", "extra cheese")


def make_pizza(size, *toppings):
    # Summarize the pizza we are about to make.
    print("")
    print("Making a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
