'''
Name: Logan Heider
Semester: Spring 2026
Course: CS 1430, Section 2, Spring 2026
Purpose: RPG Choose Your Adventure
Input: Users provides input to select paths which
         lead to different branches of the program
         Users also answer math questions by providing
         integers
Output: There are 4 main branches
        Branch 1: Ends with girl and you walking away together
        Branch 2: Ends with you walking away alone
        Branch 3: Deaths | Although there are many death scenes, counting as 1 branch
        Branch 4: Go towards portal and see Mason Schneider's game
'''
# ---------------- SET UP ----------------
import time
import sys
# sys.exit() CLOSES PROGRAM
import random

def clear():
    print("\n" * 50)

def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

potions = 0
playerhealth = 100

_POTION_HEAL = 50
_SLICE = 50
_PUNCH = 25
_BEATDOWN = 50
_SLAP = 15
_WOLF_SLASH = 75
# ---------------- SET UP ----------------


# ---------------- TITLE ----------------
print("Welcome to R'ealm de Jionir!")
Start = ''
while True:
    print("Press A to continue")
    Start = input(">")
    if Start == "A":
        break
    else:
        continue
# ---------------- TITLE ----------------


# ---------------- START ----------------
def start():
    clear()
    print("You wake up, laying in snow, in the lands of Jionir...")
    time.sleep(2)
    print("You see a trail that may lead you somewhere...")
    time.sleep(2)
    print("Will you follow it?")
    time.sleep(1)
    print("1) Yes")
    time.sleep(1)
    print("2) No")
    time.sleep(1)
    print("3) Go to the mysterious portal")

    choice = input("> ")

    if choice == "1":
        clear()
        yes_path()
    elif choice == "2":
        clear()
        print("You laid there in the snow and froze to death.")
        time.sleep(2)
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    elif choice == "3":
        clear()
        print("You approach the portal and see a sign above...")
        time.sleep(2)
        print("The sign reads \"To The Tower\"")
        time.sleep(2)
        print("You try to enter but a mysterious force pushes you out...")
        time.sleep(2)
        print("You don't have enough money... you need at least $20.")
        time.sleep(2)
        print("Silly you! XD If you really want to go there that bad, play Masons Schneider's game!")
        time.sleep(4)
        start()
    else:
        print("Invalid choice.")
        clear()
        start()
# ---------------- START ----------------


# ---------------- RABBIT ENCOUNTER ----------------
def yes_path():
    print("You follow the trail and encounter a white rabbit.")
    time.sleep(2)
    print("1) Pet it.")
    time.sleep(1)
    print("2) Ignore it.")
    time.sleep(1)
    print("3) Kill it.")

    choice = input("> ")
    clear()
    if choice == "1":
        print("You started petting the rabbit but you soon realized it was a mistake...")
        time.sleep(2)
        print("The rabbit jumped at you and ate you alive.")
        time.sleep(2)
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    elif choice == "2":
        print("You choose to walk away and ignore it...")
        time.sleep(2)
        print("However, the rabbit chases you down with it's army and eats you.")
        time.sleep(2)
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    elif choice == "3":
        print("You kill the rabbit and look over towards the tree line...")
        time.sleep(2)
        print("You see an army of rabbits retreating...")
        time.sleep(2)
        print("Seems you killed their leader.")
        time.sleep(4)
        clear()
        cabin()
    else:
        clear()
        yes_path()
# ---------------- RABBIT ENCOUNTER ----------------


# ---------------- CABIN ----------------
def cabin():
    print("You continue to walk until you stumble across a cabin...")
    time.sleep(2)
    print("You try to open the door but it seems to be locked...")
    time.sleep(2)
    print("To unlock the door you must solve some math problems!")
    time.sleep(4)
    math()
# ---------------- CABIN ----------------


# ---------------- MATH QUIZ ----------------
def math():
    global potions
    clear()
    print("Reach a score of 100% to unlock the door.")

    score = 0
    total_questions = 5

    for i in range(total_questions):
        num1 = random.randint(1, 21)
        num2 = random.randint(1, 21)
        operator = random.choice(['+', '-', '*', '//', '%'])

        if operator == '+':
            correct = num1 + num2
        elif operator == '-':
            correct = num1 - num2
        elif operator == '//':
            correct = num1 // num2
        elif operator == '%':
            correct = num1 % num2
        else:
            correct = num1 * num2

        print(f"What is {num1} {operator} {num2}?")

        try:
            answer = int(input("Your answer: "))
        except ValueError:
            print("That's not a number! Counting as incorrect.\n")
            answer = None

        if answer == correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The right answer was {correct}.\n")

    percent = (score / total_questions) * 100
    print(f"You got {score} out of {total_questions}.")
    print(f"Your score: {percent:.2f}%")
    time.sleep(3)

    if percent == 100:
        clear()
        print("Congratulations! You unlocked the door!")
        time.sleep(2)
        print("You enter the cabin and find some potions.")
        time.sleep(4)
        potions += 3
        clear()
        girl()
    else:
        clear()
        print("You failed to unlock the door...")
        time.sleep(2)
        print("You decide to move on.")
        time.sleep(4)
        clear()
        girl()
# ---------------- MATH QUIZ ----------------


# ---------------- MEET GIRL ----------------
def girl():
    print("You keep on going again and encounter a girl on the side of the road obviously in distress...")
    time.sleep(2)
    print("She asks if she can go along with you on your journies...")
    time.sleep(2)
    print("Will you take her with?")
    time.sleep(1)
    print("1) Yes")
    time.sleep(1)
    print("2) No")

    choice = input("> ")
    if choice == "1":
        clear()
        print("You decide to take her along with you...")
        time.sleep(2)
        print("She tells you her name is Anna...")
        time.sleep(2)
        print("She seems to be happy.")
        time.sleep(4)
        battle1()
    elif choice == "2":
        clear()
        print("You decide to not take her with...")
        time.sleep(2)
        print("Although she seems sad, she says she understands.")
        time.sleep(4)
        mockchoice()
    else:
        clear()
        girl()
# ---------------- MEET GIRL ----------------


# ---------------- MOCK GIRL? ----------------
def mockchoice():
    clear()
    print("Do you mock the girl?")
    time.sleep(2)
    print("1) Yes")
    time.sleep(1)
    print("2) No")

    chocie = input("> ")
    if chocie == "1":
        clear()
        print("You decide to mock the girl...")
        time.sleep(2)
        print("Ya you probably shouldn't have mocked her...")
        time.sleep(2)
        print("She killed you.")
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    elif chocie == "2":
        battle1a()

# ---------------- MOCK GIRL? ----------------

# ---------------- BATTLE 1 ----------------
def battle1():
    global girldamage
    global playerhealth
    global potions
    wolfhealth = 100
    clear()
    print("You continue the path yet again...")
    time.sleep(4)
    print("You are stopped by a wolf-like monster...")
    time.sleep(2)
    print("You must fight this beast.")
    time.sleep(4)

    while wolfhealth > 0 and playerhealth > 0:
        clear()
        print(f"Your Health: {playerhealth}")
        print(f"Wolf Health: {wolfhealth}")
        print(f"Potions: {potions}")
        print("Select your move.")
        print("1) Slice\t2) Punch\n3) Beatdown\t4) Slap\n5) Use Potion")

        choose = input("> ")
        # --- PLAYER ATTACK ---
        if choose == "1":
            clear()
            girldamage = random.randint(1, 26)
            wolfhealth -= (_SLICE + girldamage)
            print(f"You dealt {_SLICE} damage.")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "2":
            clear()
            girldamage = random.randint(1, 26)
            wolfhealth -= (_PUNCH + girldamage)
            print(f"You dealt {_PUNCH} damage.")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "3":
            clear()
            girldamage = random.randint(1, 26)
            wolfhealth -= (_BEATDOWN + girldamage)
            print(f"You dealt {_BEATDOWN} damage.")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "4":
            clear()
            girldamage = random.randint(1, 26)
            wolfhealth -= (_SLAP + girldamage)
            print(f"Wow you only dealt {_SLAP} damage...")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "5":
            if potions > 0 and playerhealth > 0 and playerhealth < 100:
                potions -= 1
                playerhealth = min(playerhealth + 50, 100)
                print(f"You used a potion! Your health is now {playerhealth}.")
                time.sleep(4)
                continue
            else:
                print("You can't use a potion right now!")
                time.sleep(4)
                continue
        else:
            print("Invalid choice.")
            time.sleep(1)
            continue

        if wolfhealth <= 0:  # Check if wolf is dead BEFORE it attacks
            break

        # --- WOLF ATTACK ---
        wolf_damage = random.randint(0, 21)
        if wolf_damage == 0:
            print("The wolf's attack missed.")
            time.sleep(4)
        else:
            playerhealth -= wolf_damage
            playerhealth = max(playerhealth, 0)  # Prevent negative HP

        if wolf_damage > 0:
            clear()
            print(f"The wolf strikes back and deals {wolf_damage} damage!")
            time.sleep(1)
            print(f"You now have {playerhealth} health left.")
            time.sleep(4)
        # --- WOLF ATTACK ---

    # --- END OF BATTLE ---
    clear()
    if playerhealth <= 0:
        print("You were defeated by the wolf...")
        time.sleep(2)
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    else:
        print("You defeated the wolf!")
        battle2()
    # --- END OF BATTLE ---
# ---------------- BATTLE 1 ----------------


# ---------------- BATTLE 1a ----------------
def battle1a():
    global playerhealth
    global potions
    wolfhealth = 100
    clear()
    print("You continue the path yet again...")
    time.sleep(4)
    print("You are stopped by a wolf-like monster...")
    time.sleep(2)
    print("You must fight this beast.")
    time.sleep(4)

    while wolfhealth > 0 and playerhealth > 0:
        clear()
        print(f"Your Health: {playerhealth}")
        print(f"Wolf Health: {wolfhealth}")
        print(f"Potions: {potions}")
        print("Select your move.")
        print("1) Slice\t2) Punch\n3) Beatdown\t4) Slap\n5) Use Potion")

        choose = input("> ")
        # --- PLAYER ATTACK ---
        if choose == "1":
            clear()
            wolfhealth -= _SLICE
            print(f"You dealt {_SLICE} damage.")
            time.sleep(4)
        elif choose == "2":
            clear()
            wolfhealth -= _PUNCH
            print(f"You dealt {_PUNCH} damage.")
            time.sleep(4)
        elif choose == "3":
            clear()
            wolfhealth -= _BEATDOWN
            print(f"You dealt {_BEATDOWN} damage.")
            time.sleep(4)
        elif choose == "4":
            clear()
            wolfhealth -= _SLAP
            print(f"Wow you only dealt {_SLAP} damage...")
            time.sleep(4)
        elif choose == "5":
            if potions > 0 and playerhealth > 0 and playerhealth < 100:
                potions -= 1
                playerhealth = min(playerhealth + 50, 100)
                print(f"You used a potion! Your health is now {playerhealth}.")
                time.sleep(4)
                continue
            else:
                print("You can't use a potion right now!")
                time.sleep(4)
                continue
        else:
            print("Invalid choice.")
            time.sleep(1)
            continue

        if wolfhealth <= 0:  # Check if wolf is dead BEFORE it attacks
            break

        # --- WOLF ATTACK ---
        wolf_damage = random.randint(0, 21)
        if wolf_damage == 0:
            print("The wolf's attack missed.")
            time.sleep(4)
        else:
            playerhealth -= wolf_damage
            playerhealth = max(playerhealth, 0)  # Prevent negative HP

        clear()
        print(f"The wolf strikes back and deals {wolf_damage} damage!")
        time.sleep(1)
        print(f"You now have {playerhealth} health left.")
        time.sleep(4)
        # --- WOLF ATTACK ---

    # --- END OF BATTLE ---
    clear()
    if playerhealth <= 0:
        print("You were defeated by the wolf...")
        time.sleep(2)
        print("You Died")
        time.sleep(2)
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    else:
        print("You defeated the wolf!")
        battle2a()
    # --- END OF BATTLE ---
# ---------------- BATTLE 1a ----------------


# ---------------- BATTLE 2 ----------------
def battle2():
    global girldamage
    global playerhealth
    global potions
    rockhealth = 750
    print("After defeating the wolf you learn a new skill...")
    time.sleep(2)
    print("New Skill Learned: Wolf Slash!")
    time.sleep(2)
    print("Automatically replacing with worst attack you currently have.")
    time.sleep(4)
    clear()
    print("You feel a shake in the ground...")
    time.sleep(4)
    print("You look out in the horizon and see a dark shadow...")
    time.sleep(2)
    print("It looks like a Rock Giant...")
    time.sleep(4)

    while rockhealth > 0 and playerhealth > 0:
        clear()
        print(f"Your Health: {playerhealth}")
        print(f"Rock Giant Health: {rockhealth}")
        print(f"Potions: {potions}")
        print("Select your move.")
        print("1) Slice\t2) Punch\n3) Beatdown\t4) Wolf Slash\n5) Use Potion")

        choose = input("> ")
        # --- PLAYER ATTACK ---
        if choose == "1":
            clear()
            girldamage = random.randint(1, 26)
            rockhealth -= (_SLICE + girldamage)
            print(f"You dealt {_SLICE} damage.")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "2":
            clear()
            girldamage = random.randint(1, 26)
            rockhealth -= (_PUNCH + girldamage)
            print(f"You dealt {_PUNCH} damage.")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "3":
            clear()
            girldamage = random.randint(1, 26)
            rockhealth -= (_BEATDOWN + girldamage)
            print(f"You dealt {_BEATDOWN} damage.")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "4":
            clear()
            girldamage = random.randint(1, 26)
            rockhealth -= (_WOLF_SLASH + girldamage)
            print(f"You dealt {_WOLF_SLASH} damage...")
            time.sleep(1)
            print(f"Anna dealt {girldamage} damage also!")
            time.sleep(4)
        elif choose == "5":
            if potions > 0 and playerhealth > 0 and playerhealth < 100:
                potions -= 1
                playerhealth = min(playerhealth + 50, 100)
                print(f"You used a potion! Your health is now {playerhealth}.")
                time.sleep(4)
                continue
            else:
                print("You can't use a potion right now!")
                time.sleep(2)
                continue
        else:
            print("Invalid choice.")
            time.sleep(4)
            continue

        if rockhealth <= 0:  # Check if wolf is dead BEFORE it attacks
            break

        # --- ROCK GIANT ATTACK ---
        rock_damage = random.randint(1, 51)
        if rock_damage == 0:
            print("The Rock Giant's attack missed.")
            time.sleep(4)
        else:
            playerhealth -= rock_damage
            playerhealth = max(playerhealth, 0)  # Prevent negative HP

        if rock_damage > 0:
            clear()
            print(f"The Rock Giant strikes back and deals {rock_damage} damage!")
            time.sleep(1)
            print(f"You now have {playerhealth} health left.")
            time.sleep(4)
        # --- ROCK GIANT ATTACK ---

    # --- END OF BATTLE ---
    clear()
    if playerhealth <= 0:
        print("You were defeated by the Rock Giant...")
        time.sleep(2)
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    else:
        end()
    # --- END OF BATTLE ---
# ---------------- BATTLE 2 ----------------


# ---------------- BATTLE 2a ----------------
def battle2a():
    global playerhealth
    global potions
    rockhealth = 750
    clear()
    print("After defeating the wolf you learn a new skill...")
    time.sleep(2)
    print("New Skill Learned: Wolf Slash!")
    time.sleep(2)
    print("Automatically replacing with worst attack you currently have.")
    time.sleep(4)
    clear()
    print("You feel a shake in the ground...")
    time.sleep(4)
    print("You look out in the horizon and see a dark shadow...")
    time.sleep(2)
    print("It looks like a Rock Giant...")
    time.sleep(4)

    while rockhealth > 0 and playerhealth > 0:
        clear()
        print(f"Your Health: {playerhealth}")
        print(f"Wolf Health: {rockhealth}")
        print(f"Potions: {potions}")
        print("Select your move.")
        print("1) Slice\t2) Punch\n3) Beatdown\t4) Wolf Slash\n5) Use Potion")

        choose = input("> ")
        # --- PLAYER ATTACK ---
        if choose == "1":
            clear()
            rockhealth -= _SLICE
            print(f"You dealt {_SLICE} damage.")
            time.sleep(4)
        elif choose == "2":
            clear()
            rockhealth -= _PUNCH
            print(f"You dealt {_PUNCH} damage.")
            time.sleep(4)
        elif choose == "3":
            clear()
            rockhealth -= _BEATDOWN
            print(f"You dealt {_BEATDOWN} damage.")
            time.sleep(4)
        elif choose == "4":
            clear()
            rockhealth -= _WOLF_SLASH
            print(f"You dealt {_WOLF_SLASH} damage...")
            time.sleep(4)
        elif choose == "5":
            if potions > 0 and playerhealth > 0 and playerhealth < 100:
                potions -= 1
                playerhealth = min(playerhealth + 50, 100)
                print(f"You used a potion! Your health is now {playerhealth}.")
                time.sleep(4)
                continue
            else:
                print("You can't use a potion right now!")
                time.sleep(4)
                continue
        else:
            print("Invalid choice.")
            time.sleep(4)
            continue

        if rockhealth <= 0:  # Check if wolf is dead BEFORE it attacks
            break

        # --- ROCK GIANT ATTACK ---
        rock_damage = random.randint(1, 51)
        if rock_damage == 0:
            print("The Rock Giant's attack missed.")
            time.sleep(4)
        else:
            playerhealth -= rock_damage
            playerhealth = max(playerhealth, 0)  # Prevent negative HP

        if rock_damage > 0:
            clear()
            print(f"The Rock Giant strikes back and deals {rock_damage} damage!")
            time.sleep(1)
            print(f"You now have {playerhealth} health left.")
            time.sleep(4)
        # --- WOLF ATTACK ---

    # --- END OF BATTLE ---
    clear()
    if playerhealth <= 0:
        print("You were defeated by the Rock Giant...")
        time.sleep(2)
        print("You Died")
        time.sleep(2)
        print("Would you like to restart?")
        time.sleep(1)
        print("1) Yes")
        time.sleep(1)
        print("2) No")
        choose = input("> ")
        if choose == "1":
            start()
        elif choose == "2":
            sys.exit()
    else:
        enda()
    # --- END OF BATTLE ---
# ---------------- BATTLE 2a ----------------


# ---------------- END ----------------
def end():
    clear()
    print("Congratulations on beating the Rock Giant!")
    time.sleep(2)
    print("You and Anna gather your things and start to go on your ways...")
    time.sleep(2)
    print("She pulls you aside and thanks you for taking her with you...")
    time.sleep(2)
    print("You two will spend your lives together exploring this world.")
    time.sleep(4)
    secret()
# ---------------- END ----------------


# ---------------- END(a) ----------------
def enda():
    clear()
    print("Congratulations on beating the Rock Giant!")
    time.sleep(2)
    print("You continue your journey to the horizon...")
    time.sleep(2)
    print("Seeing what else this world has to offer.")
    time.sleep(4)
    secret()
# ---------------- END(a) ----------------


# ---------------- SECRET ----------------
def secret():
    clear()
    while True:
        secret = input("> ")
        if secret == "J10N!R":
            break
        else:
            continue
    clear()
    print("Wow you got the secret code...")
    time.sleep(2)
    print("Idk what you expect but theres nothing here...")
    time.sleep(8)
    print("I said there's nothing here...")
    time.sleep(10)
    print("You can leave now...")
    time.sleep(10)
    print("Fine... here's something I guess...")
    time.sleep(2)
    a= r"""
                  ____----------- _____
\~~~~~~~~~~/~_--~~~------~~~~~     \
 `---`\  _-~      |                   \
   _-~  <_         |                     \[]
 / ___     ~~--[""] |      ________-------'_
> /~` \    |-.   `\~~.~~~~~                _ ~ - _
 ~|  ||\%  |       |    ~  ._                ~ _   ~ ._
   `_//|_%  \      |          ~  .              ~-_   /\
          `--__     |    _-____  /\               ~-_ \/.
               ~--_ /  ,/ -~-_ \ \/          _______---~/
                   ~~-/._<   \ \`~~~~~~~~~~~~~     ##--~/
                         \    ) |`------##---~~~~-~  ) )
                          ~-_/_/                  ~~ ~~    
    """
    print(a)
# ---------------- SECRET ----------------
start()