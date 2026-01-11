name = input("Enter your name, adventurer: ")
print(f"\nWelcome to your adventure, {name}!" +
      "\nDo you want to begin your adventure?")

while True:
    answer = input("\nYes/No: ").lower()
    if answer == "yes":
        print("Great! Your adventure begins now.")
        print("\n "
              "You wake up and find yourself on a tropical island. "
              "\n In front of you is nothing but ocean for miles."
              "\n So you turn around and see a jungle and decide to explore."
              "\n After walking for a while, you come across a split in the road."
              "\n \n Do you want to go left or right?")
        answer = input("\nLeft/Right: ").lower()
        while answer not in ["left", "right"]:
            print("Please enter a valid option (left/right).")
            answer = input("\nLeft/Right: ").lower()

        if answer == "left":
            print("\n \n You take the path to the left. The trees grow thick and block out the sun. The air gets cold. "
                  "\n Suddenly, you stumble upon a massive stone cave entrance that looks like a Jaguar's "
                  "mouth.\n Inside, you see a faint golden glow. \n \n Do you want to enter the cave?")
            answer = input("\nYes/No: ").lower()
            while answer not in ["yes", "no"]:
                print("Please enter a valid option (yes/no).")
                answer = input("\nYes/No: ").lower()

            if answer == "yes":
                print("\n \n You bravely enter the cave. As you walk deeper, the golden glow intensifies."
                      "\n You soon find the source: a massive treasure chest overflowing with gold and jewels!"
                      "\n Beside the chest, you see a resting 7ft snake."
                      "\n Do you risk getting some treasure or leave it alone and exit the cave?")
                answer = input("\nRisk It/Leave It: ").lower()
                while answer not in ["risk it", "leave it"]:
                    print("Please enter a valid option (risk it/leave it).")
                    answer = input("\nRisk It/Leave It: ").lower()

                if answer == "risk it":
                    print("\n \n As you approach the treasure, the snake awakens."
                          "\n In one fatal strike, it attacks you. You have met a tragic end."
                          "\nGAME OVER")
                    quit()
                elif answer == "leave it":
                    print("\n \n You wisely decide to leave the treasure alone. "
                          "\n So you exit the cave safely and continue your adventure."
                          "\n After a long walk, you find a boat and sail away from the island."
                          "\nCONGRTULATIONS! You have survived the adventure!")
                    quit()
            elif answer == "no":
                print("\n \n You decide not to enter the cave and continue exploring the jungle. "
                      "\n While exploring you find a pond and have a drink of some of the water. "
                      "\n After drinking the water you feel find that you can understand"
                      "\n the animals that inhabit the jungle. Primarily, a parrot that is speaking to you."
                      "\n The parrot tells you of a way off the island and offers to guide you there."
                      "\n Do you want to follow the parrot?")
                answer = input("\nYes/No: ").lower()
                while answer not in ["yes", "no"]:
                    print("Please enter a valid option (yes/no).")
                    answer = input("\nYes/No: ").lower()
                if answer == "yes":
                    print("\n You follow the parrot through the jungle. "
                          "\n After a long trek, you find that the parrot has led you"
                          "\n to an ambush from all the animals in the jungle."
                          "\n The animals all simultaneously attack you and you meet a tragic end."
                          "\nGAME OVER")
                    quit()
                elif answer == "no":
                    print("\n You decide not to follow the parrot and continue your adventure alone."
                          "\n After walking for a while, you end up finding a radio."
                          "\n You use the radio to call for help and are soon rescued from the island."
                          "\nCONGRATULATIONS! You have survived the adventure!")
                    quit()

        elif answer == "right":
            print("\n \n You take the path to the right. The jungle opens up to a beautiful, rocky cliff overlooking the ocean. "
                  "\n Far below, you see an old, abandoned pirate ship crashed on the rocks. "
                  "\n You also see a narrow, shaky bridge leading to a small lighthouse."
                  "\n \n Do you want to explore the pirate ship or cross the bridge to the lighthouse?")
            answer = input("Lighthouse/Ship: ").lower()
            while answer not in ["lighthouse", "ship"]:
                print("Please enter a valid option (lighthouse/ship).")
                answer = input("Lighthouse/Ship: ").lower()
            if answer == "lighthouse":
                print("\n \n You carefully cross the shaky bridge to the lighthouse. "
                      "\n Inside, you find an old sailor who has been living there alone for years."
                      "\n He offers to help you get off the island if you can answer his riddle."
                      "\n He asks, 'What has keys but can't open locks?'")
                answer = input("\nYour Answer: ").lower()
                if answer == "piano":
                    print("\n Correct! The sailor is impressed and helps you signal for help."
                          "\n Soon, a passing ship spots your signal and rescues you from the island."
                          "\nCONGRATULATIONS! You have survived the adventure!")
                    quit()
                else:
                    print("\n Wrong answer! The sailor is disappointed and refuses to help you."
                          "\n You are left stranded on the island forever."
                          "\nGAME OVER")
                    quit()
            elif answer == "ship":
                print("\n \n You decide to explore the old pirate ship. "
                      "\n As you climb aboard, the ship creaks and groans under your weight."
                      "\n Suddenly, the ship starts to sink deeper into the rocks."
                      "\n You try to escape, but the ship collapses, trapping you inside."
                      "\n You have met a tragic end."
                      "\nGAME OVER")
                quit()

        else:
            print("Please print valid option.")

    elif answer == "no":
        print("Maybe next time. Goodbye!")
        quit()
    else:
        print("Please enter a valid option (yes/no).")
