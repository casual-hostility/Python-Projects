# How is PJ

def condition():
    has_slept = True
    ate_food = True

    if has_slept == True and ate_food == True:
        print("I am well.")

    elif ate_food == False:
        print("Hangry, leave alone!")

    elif has_slept == False:
        print("Just tired.")

    else:
        print("Distracted.")

condition()