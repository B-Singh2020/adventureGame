'''
Text adventure game 
'''
print("Welcome to Aventura!\n")
print("Prepare for the journey...")
health = 10
infected = False

name = input("What is your name? ")

print("\n" + name + "? Not that it matters now, prisoner 147\n")

age = int(input("What is your age? "))

#print("Test: Hello", name, "you are", age, "years old\n")

ageCheck = age - 18
if(ageCheck < 0):
    print("You are not old enough for this adventure!\n")
    
else:
    print("You are ready for this adventure!\n")
    wants_to_play = input("Are you ready to begin your journey? (yes/no) ")
    if(wants_to_play == "yes"):
        print("Let us begin!!\n")

