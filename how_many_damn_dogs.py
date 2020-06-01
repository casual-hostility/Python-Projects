# How many damn dogs are in my yard today?

def the_yard():
    dogs = []

    while True:

        dog = input("What dogs do you see? Type 'Done' when finished inputting dogs: " )
        dogs.append(dog)

        if 'Sam' in dogs:
            print("Sam doesn't count.")
            dogs.remove('Sam')
            continue

        if ' ' in dogs:
            print("Please type the name of a dog.")
            dogs.remove('')

        if 'Done' in dogs:
            dogs.remove('Done')
            break

    if len(dogs) > 2:
        print("Too damn many.")
        for i in dogs:
            print(i)

the_yard()