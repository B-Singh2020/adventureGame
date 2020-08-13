'''
Text adventure game 
'''
print("Welcome to Aventura!\n")

health = 10
infected = False

name = input("What is your name? ")

print("\n" + name + "? Not that it matters now, prisoner 147\n")

age = int(input("What is your age, prisoner? "))

#print("Test: Hello", name, "you are", age, "years old\n")

ageCheck = age - 18
if(ageCheck < 0):
    print("You are too weak and unfit to survive!\n")
    
else:
    print("You look strong, too bad you will waste away in here", name, "\n")
    wants_to_play = input("(Are you ready to begin your journey?) (yes/no) ").lower()
    if(wants_to_play == "yes"):
        print("Let us begin!!\n\n")
        print("You've been surrounded by four aged stone walls for weeks, there was nothing else to do but stare at them. To look at the cracks that had started to form as time passed, or gouged by other prisoners - anything to pass time, slowly going mad trying to find the meaning behind your imprisonment.\n\n")

        print("You regret ever stopping in North Umberton. Why had you insisted on stopping by a local inn? Companionship? A warm meal? Whatever reason, it didnt matter once the kings guard accused of being sone else.... something else...\n\n")

        print(" \" They are here. No more running. It happened closer sooner than we could ever expect, take this flee as far as you can, your highness. I will buy you some time.  \" \n\n")

        print(" Before you realized it, your door cell opens and closes. Your life wasnt much different, expect for the fact there was a frail old man with a crown on his head right in front of you.\n\n")

        print(" \" And who might you be? Haah, they told me this passage would be empty. The fates have a strange way of bringing people together.  \" the old man said. He whispered \" Aventura\" near the far wall and a passage opened up. \n\n")

        print(" \" Im not the best company but its only a short walk to your freedom\" You instantly jolted up and begin your walk with the king into the deep unknown\n\n ")


    else:
        print("Thats a shame...\n")

