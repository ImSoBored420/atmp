import time

#My first attempt at implementing classes - be nice to meeeeeeeeeee ;3 (someone kill me)
class Terry:
    def __init__(self, morality, skillz, speed, fortitude):
        self.morality = morality
        self.skillz = skillz
        self.speed = speed
        self.fortitude = fortitude

#STATTTTTTTTTTTTS
NormalTerry = Terry(3, 7, 9, 15)

TSBDeluxePackage = Terry(2, 10, 11, 14)

#this was a test to see if I did the class thing right
while (True): #I'm gonna preserve this test thing and try to make it inaccessable to the people running this (A maximum of 3 people will ever run this code in the world)
    break
    print(f"Normal Terry morality is {NormalTerry.morality}")
    print(f"T S-B Deluxe Package morality is {TSBDeluxePackage.morality}")

def normality(): #terry: normal edition
    chooseAbility = input("what stats do you want to look at on Normal Terry? (morality, skillz, speed, fortitude): ")
    if chooseAbility == "morality":
        print(f"Normal Terry morality stat is {NormalTerry.morality}.")
    elif chooseAbility == "skillz" or chooseAbility == "skills":
        print(f"Normal Terry epic skillz stat is {NormalTerry.skillz}.")
    elif chooseAbility == "speed":
        print(f"Normal Terry speed stat is {NormalTerry.speed}.")
    elif chooseAbility == "fortitude":
        print(f"Normal Terry fortitude stat is {NormalTerry.fortitude}.")
    else: 
        while (True):
            print("That stat doesn't exist in this context. pick one. (morality, skillz, speed, fortitude) ")
            chooseAbility = input("what stats do you want to look at on Normal Terry? (morality, skillz, speed, fortitude): ")
            if chooseAbility == "morality":
                print(f"Normal Terry morality stat is {NormalTerry.morality}.")
                break
            elif chooseAbility == "skillz" or chooseAbility == "skills":
                print(f"Normal Terry epic skillz stat is {NormalTerry.skillz}.")
                break
            elif chooseAbility == "speed":
                print(f"Normal Terry speed stat is {NormalTerry.speed}.")
                break
            elif chooseAbility == "fortitude":
                print(f"Normal Terry fortitude stat is {NormalTerry.fortitude}.")
                break

def DELUXO(): #terry using a mere %1 of his power (I can't understand the code I make after I make it and look at it again)
    chooseAbility = input("what stats do you want to look at on DELUXE Terry? (morality, skillz, speed, fortitude): ")
    if chooseAbility == "morality":
        print(f"DELUXE Terry morality stat is {TSBDeluxePackage.morality}.")
    elif chooseAbility == "skillz" or chooseAbility == "skills":
        print(f"DELUXE Terry epic skillz stat is {TSBDeluxePackage.skillz}.")
    elif chooseAbility == "speed":
        print(f"DELUXE Terry speed stat is {TSBDeluxePackage.speed}.")
    elif chooseAbility == "fortitude":
        print(f"DELUXE Terry fortitude stat is {TSBDeluxePackage.fortitude}.")
    else: 
        while (True):
            print("That stat doesn't exist in this context. pick one. (morality, skillz, speed, fortitude) ")
            chooseAbility = input("what stats do you want to look at on TSBDeluxePackage Terry? (morality, skillz, speed, fortitude): ")
            if chooseAbility == "morality":
                print(f"TSBDeluxePackage Terry morality stat is {TSBDeluxePackage.morality}.")
                break
            elif chooseAbility == "skillz" or chooseAbility == "skills":
                print(f"DELUXE Terry epic skillz stat is {TSBDeluxePackage.skillz}.")
                break
            elif chooseAbility == "speed":
                print(f"DELUXE Terry speed stat is {TSBDeluxePackage.speed}.")
                break
            elif chooseAbility == "fortitude":
                print(f"DELUXE Terry fortitude stat is {TSBDeluxePackage.fortitude}.")
                break

def selecTOR():
    nt_or_deluxe = input("\nnormal terry, or TSBDeluxePackage?: ")
    if nt_or_deluxe == "normal terry" or nt_or_deluxe == "normal":
        normality()
    elif nt_or_deluxe == "TSBDeluxePackage" or nt_or_deluxe == "deluxe":
        DELUXO()
    else: 
        print("That's not a thing in this context, bro. You gotta type either 'normal terry' or 'normal' for normal terry, and for TSB: Deluxe Package, type either 'TSBDeluxePackage' or 'deluxe'")
        print("We'll try this again, okay?")
        while (True):
            nt_or_deluxe = input("\nnormal terry, or TSBDeluxePackage?: ")
            if nt_or_deluxe == "normal terry" or nt_or_deluxe == "normal":
                normality()
                break
            elif nt_or_deluxe == "TSBDeluxePackage" or nt_or_deluxe == "deluxe":
                DELUXO()
                break
            else:
                pass #I just put this comment here because it gets rid of a sonarlint error about this being empty
selecTOR() #I put this in the wrong place last time, eventing in the code asking me if I needed anything else indefinitely until I said yes
while (True):
    anythingMore = input("\nanything else?: ")
    if anythingMore == "yes" or anythingMore == "y":
        selecTOR()
    elif anythingMore == "no" or anythingMore == "n":
        print("Alright then.")
        break
      
time.sleep(3)
while (True):
    time.sleep(0.1)
    print("\nGREAT JOB!") #femtanyl reference