# Homework                          DragonQuest.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 08/17/2021

import pygame
import random
import sys
import textwrap
import time

TYPINGSPEED = 15000
    
def playMusic(track, y, x):
    if y == 1:
        if x == 1:
            try:
                pygame.mixer.init()
                #pygame.mixer.music.load(track + ".wav")
                pygame.mixer.music.play(-1)    
            except:
                print("Couldn't find sound file.")
    else:
        try:
            pygame.mixer.music.unload()
            pygame.mixer.music.stop()
        except:
            print("No sound file to stop.")
        if x == 1:
            try:
                pygame.mixer.init()
                #pygame.mixer.music.load(track + ".wav")
                pygame.mixer.music.play(-1)    
            except:
                print("Couldn't find sound file.")
                
def typeText(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / TYPINGSPEED)

def chooseContinue():
    yesContinue = input("Press 'Enter' to continue or 'Q' to quit...")
    if yesContinue == "":
        print("")
    elif yesContinue == 'q':
        exit()
    else:
        return chooseContinue()
        
def restartStory():
    yesContinue = input("Press 'Enter' to restart the story or 'Q' to quit...")
    if yesContinue == "":
        track = "You Die"
        playMusic(track, 0, 1)   
        time.sleep(1.5)     
        runMain()
    elif yesContinue.lower() == 'q':
        exit()
    else:
        return restartStory()
        
def printIntro():
    text = "\n'Here Ye! Here Ye!\n\n"
    typeText(text)
    text = "\tThe King of Anagua, the Islands of the\nGreat Sea, has proclaimed that Golan, the Great\nDragon of the Western Mountains, deserves\na slaying. He is terrorizing the countryside,\neating nobleman and stealing gold. Any man who\nfeels himself able to slay Golan should report\nto the castle this afternoon.\n\n"
    typeText(text)
    text = "\tThe King has issued a reward of 5,000\ngold pieces and to court his daughter,\nPrincess Elaine, for the killing of the Dragon\nand bringing one tooth from his jaws of death,\nthereby proving that he is dead.'\n\n"
    typeText(text)
    text = "        by decree of His Royal Majesty,\n               -King Thesium of Anagua\n\n"
    typeText(text)
    
def printIntro2():
    text = "It's a warm summer day. You, Warrick,an Elven\nWarrior of the Great Forest of Anagua, have left\nyour homeland in the trees with the other people\nto pursue this profitable announcement from the\nKing.\n\n"
    typeText(text)
    text = "You journey to the castle. As you make your way\nthrough the city, you see the other brave men\nwho are willing to accept this challenge also.\n\n"
    typeText(text)
    text = "You just hope that you will slay the Dragon\nfirst.\n"
    typeText(text)      

def printIntro3():
    text = "After waiting in line for an hour, the King's\nsquire makes the announcement that the quest is\nready to begin.\n\n"
    typeText(text)      
    text = "He suggests that you go to the peddler's and\nbuy supplies for your journey because the\nrest of the way will not be easy.\n\n"
    typeText(text)      
    
def startAdventure():
    print("Do you:")
    print("A) Go to the peddler's for supplies?")
    print("B) Continue without supplies?")
    choice = input("Which will you choose? \n(A/B/Q)> ")
    if choice.lower() == "a":
        goToPeddler()
    elif choice.lower() == "b":
        continueWithout()
    elif choice.lower() == 'q':
        exit()
    else:
        return startAdventure()
    
def goToPeddler():
    text = "\nYou've decided that it would be best to go with\nsupplies for you do not know what the wilderness\nahead will provide. This will take a little\ntime, but is is worth it.\n\n"
    typeText(text)      
    text = "At the peddler's, you decide to buy food, a\nsimple earth spellbook, some arrows for your\nbow, and some matches in case you need to start\na fire.The peddler offers you a sword, but you\nsay you already have one forged from the metal\nof a meteorite that crashed in the Western\nMountains years ago.\n\n"
    typeText(text)      
    text = "You leave for the gates heading to the forest\nand come to a path. The path forks.\n\n"
    typeText(text)      
    chooseFork()
    
def continueWithout():
    text = "\nYou decide to choose as the same as the majority of the fighters\nand go on without supplies. You again make your\nway through the city towards the gates. You can\nsee the forest of your home up ahead.\n\n"
    typeText(text)      
    text = "You enter the forest which you have known for\nso long, but there is something different about\nit. There is a strange silence in the air. No\nsigns of bird or animal life. You look around\nand realize you've been surrounded by some of\nthe men that you saw at the castle.\n"
    typeText(text)      
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "They steal from you what few possessions you\nhave and take your life. The last memory you\nhave is of the men laughing at your lifeless\nbody on the ground...\n\n"
    typeText(text)
    restartStory()

def chooseFork():
    print("Do you:")
    print("A) Take the right path?")
    print("B) Take the left path?")
    choice = input("Which will you choose? \n(A/B/Q)> ")
    if choice.lower() == "a":
        goRight()
    elif choice.lower() == "b":
        text = "\nOn the left path, you continue your quest."
        typeText(text)
        goLeft()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseFork()

def goRight():
    text = "\nYou decide to take the right path. You feel\nthat luck has helped you on what you believe\nis an excellent decision.\n\n"
    typeText(text)
    text = "As you walk along through the forest, you listen\nto the sounds of nature and think about your\nquest ahead. You keep walking and discover\nthat the path ends abruptly and the only way to\ncontinue is through the thick underbrush.\n\n"
    typeText(text)
    text = "You think about what your can do and narrow it\ndown to two choices.\n\n"
    typeText(text)
    chooseUnderbrush()

def chooseUnderbrush():
    print("Do you:")
    print("A) Go through the underbrush?")
    print("B) Walk back and take the left path?")
    choice = input("Which will you choose? \n(A/B/Q)> ")
    if choice.lower() == "a":
        goUnderbrush()
    elif choice.lower() == "b":
        goBadLeft()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseUnderbrush()
    
def goUnderbrush():
    text = "\nAfter your long, hard struggle through the\nunderbrush, you finally reach another path.\nYou think it might be the other path you could\nhave taken. You stop and take a rest to eat\nlunch, but you know...\n\n"
    typeText(text)
    text = "You must keep going."
    typeText(text)
    chooseContinue()
    goLeft()
    
def goLeft():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nNight has begun to fall and you know you must\nbe very alert because there are dangers that\nlurk in the shadows.\n\n"
    typeText(text)
    text = "You continue walking and hear very strange\nnoises. You look around quickly and realize that\nthere are three small forms following you.\n\n"
    typeText(text)
    text = "You turn quickly and make a decision."
    typeText(text)
    armSelf()
    
def goBadLeft():
    text = "\nAfter you disappoint yourself with your bad\ndecision on the right path and the time you've\nwasted, you turn and head back.\n\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "After walking several steps, an unknown flying\nassailant attacks you from the trees. Dazed and\namazed, you fall subject to the appetite of a\ngiant raven!\n"
    typeText(text)
    restartStory()
    
def armSelf():
    print("Do you:")
    print("A) Draw your sword?")
    print("B) Draw your bow?")
    print("C) Run!")
    choice = input("Which will you choose? \n(A/B/C/Q) > ")
    if choice.lower() == "a":
        drawSword()
    elif choice.lower() == "b":
        drawBow()
    elif choice.lower() == "c":
        run()
    elif choice.lower() == 'q':
        exit()
    else:
        return armSelf()
    
def drawSword():
    text = "\nUnsheathing your special sword, you prepare\nyourself for an unknown attack. You find that\nthe forms are really goblin warriors!\n\n"
    typeText(text)
    text = "You, being a very skill warrior yourself, strike\nall three down with one swing. The goblins are\nquickly cut in half by your mighty sword.\n"
    typeText(text)
    chooseContinue()
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "You are very tired and decide to rest until\nmorning. After you awaken, you decide to continue\non the path.\n\n"
    typeText(text)
    continuePath()

def drawBow():
    text = "\nYou take the long wooden bow off your shoulder,\npulling three arrows from your quiver and\ntake aim. Launching all the three arrows at\nonce, you take down the three forms quickly.\n\n"
    typeText(text)
    text = "After you are sure they are dead, you go and\ninspect the bodies. You discover that they are\ngoblin warriors!\n"
    typeText(text)
    chooseContinue()
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "You find yourself very tired and decide to rest\nfor the night. After you awaken, you continue\non the path.\n\n"
    typeText(text)
    continuePath()

def run():
    text = "\nNot being sure of the strength of the forms or\nyourself, you turn cowardly and start to run.\nAs you run, the branches strike against your\nface. You don't think that you'll make it out\nalive.\n\n"
    typeText(text)
    text = "The forms prove to be very quick and catch up\nwith you easily and trip you with long pikes.\nBefore they stab down at you their pikes, you\ndiscover that they are goblin warriors!\n"
    typeText(text)
    restartStory()
    
def continuePath():
    text = "After walking for several hours on the thinning\npath, you see a small mud hut with smoke coming\nout a hole located on the top of the hut.\n\n"
    typeText(text)
    text = "You are very tired, but scared of what you might\nfind in the creepy hut.\n\n"
    typeText(text)
    chooseRest()
    
def chooseRest():
    print("Do you:")
    print("A) Go to the hut and rest?")
    print("B) Keep walking?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        chooseHut()
    elif choice.lower() == "b":
        keepWalking()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseRest()
    
def chooseHut():
    text = "\nYou stumble over to the mud hut and knock on the small wooden door with no hinges.\nNo one answers. Suddenly, you hear a small voice from behind you. It startles\nyou at first, but then you discover that it is just a hermit, a trusted friend\nof the elf people. He invites you in to eat and sleep.\n"
    typeText(text)
    chooseContinue()
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "While you are sleeping, you have a vision about the future. You see yourself\ncarrying something in a small sack. People around you are cheering. One last\nthing you see before awaking is a woman walking, holding your hand.\n\n"
    typeText(text)
    text = "The hermit wakes you urgently and whispers a verse in your ear, \n\n'You must swing before you fire.'\n\nThen he rushes you out the door.\nYou have no clue what it means, but you think\nit could help you later.\n\n"
    typeText(text)
    chooseWrite() 
    
def keepWalking():
    text = "\nYou decide to skip the hut and keep walking on the never-ending path.\n\n"
    typeText(text)
    text = "You realize you know this part of the woods. You are near your home.\n\n"
    typeText(text)
    text = "You think of your family and your people. You don't want to fail this quest and maybe die\nbecause you do not want to lose the ones close to you.\n\n"
    typeText(text)
    text = "You finally decide that there are no such things as dragons and return home.\n"
    typeText(text)
    restartStory()  
    
def chooseWrite():
    print("Do you:")
    print("A) Stop to write it down?")
    print("B) Hurry along and write it later?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        stopToWrite()
    elif choice.lower() == "b":
        hurryAlong()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseWrite()
    
def stopToWrite():
    text = "\nYou pull out some leaves and begin sharpening\nyour bark pencil.\n\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "Then you see why the hermit was rushing you.\nYou start to run, but five men also on the quest\nspot you and take you down.\n\n"
    typeText(text)
    text = "They steal your belongings and stab you to death.\n"
    typeText(text)
    restartStory()
    
def hurryAlong():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nYou start to run, sensing a feeling of danger and\nonly look back once to see five men overtake the\nhermit's hut and kill your hermit friend.\n\n"
    typeText(text)
    chooseContinue()
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "You slip into the forest so as not to be seen and\nescape safely. You quietly thank the hermit for\nhis kindness to yourself. You will always\nremember his bravery.\n\n"
    typeText(text)
    text = "You come to the edge of the forest and see a\ngreat, broad river that seems to stretch across\nfor miles. You now know that your journey has just begun.\n"
    typeText(text)
    text = "You come across a boat and get in. You see\ntwo choices: go across the river to the scary\nswamp or go into the dangerous ocean.\n"
    typeText(text)
    chooseRiverOrBoat()
    
def chooseRiverOrBoat():
    print("Do you:")
    print("A) Choose the river?")
    print("B) Choose the ocean?")
    choice = input("Which do you choose? \n(A/B/Q) >" )
    if choice.lower() == "a":
        goRiver()
    elif choice.lower() == "b":
        text = "You head out into the ocean and come across a storm."
        typeText(text)
        goOcean()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseRiverOrBoat()
        
def goRiver():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nAfter boating for a while, you notice a school of\npiranhas! They are swimming too fast to\nout-paddle them."
    typeText(text)
    shootOrZap()
    
def shootOrZap():
    print("Do you:")
    print("A) Shoot arrows?")
    print("B) Zap them?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        shootArrows()
    elif choice.lower() == "b":
        zapThem()
    elif choice.lower() == 'q':
        exit()
    else:
        return shootOrZap()
    
def shootArrows():
    text = "\nYou try to shoot arrows at them but the\nwooden arrows float to the top instead.\nThe recoil from the bow sends you over the\nside of the boat. In your last moments,\nyou see nothing but teeth.\n"
    typeText(text)
    restartStory()
    
def zapThem():
    text = "\nThe electricity fills the water and all the\npiranhas die. You don't like piranhas but\nremember that they're good for you.\n"
    typeText(text)
    eatOrNo()
    
def eatOrNo():
    print("Do you:")
    print("A) Choose not to eat the piranhas?")
    print("B) Choose to eat the piranhas?")
    choice = input("Which do you choose? \n(A/B/q) > ")
    if choice.lower() == "a":
        dontEat()
    elif choice.lower() == "b":
        eat()
    elif choice.lower() == 'q':
        exit()
    else:
        return eatOrNo()
    
def dontEat():
    text = "\nAs you begin to paddle away again, you feel a\ntugging sensation rock the boat back and forth.\nBefore you can react, you are thrown\nfrom the boat and into the water. The fish\nhave turned into zombies! The murky\nwater turns red as the undead piranhas eat you!\n"
    typeText(text)
    restartStory()
    
def eat():
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "\nYou fill up on piranhas and are ready to go on."
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nThere are some rapids up ahead.\n"
    typeText(text)
    fordOrEvaporate()
    
def fordOrEvaporate():
    print("Do you:")
    print("A) Try to ford the rapids?")
    print("B) Try to evaporate some of the water with\nsome fireballs?")
    choice = input("Which do you choose? \n(A//B/Q) > ")
    if choice.lower() == "a":
        ford()
    elif choice.lower() == "b":
        evaporate()
    elif choice.lower() == 'q':
        exit()
    else:
        return fordOrEvaporate()
    
def ford():
    text = "\nThe rapids are two powerful! You are\ncrushed against the rocks and die!\n"
    typeText(text)
    restartStory()
    
def evaporate():
    text = "\nAfter a lot of trying, you manage to evaporate\nthe dangerous part of the water within the\nbrief allotted time. You continue to the swamp.\n\n"
    typeText(text)
    chooseContinue()
    track = "Underclocked"
    playMusic(track, 0, 1)
    text = "\nAs you enter the dark, green, shadowy swamp,\nyou notice the pungent smell of the scurrying\nrats and decaying bodies scattered around.\nYou wonder what kind of beast could have\ndone this kind of damage, but are unable\nto figure it out.\n\n"
    typeText(text)
    text = "You follow a solitary path for an estimated\nquarter mile, finding nothing of note. However,\nyou soon come to a river, and are forced to cross somehow.\n\n"
    typeText(text)
    text = "There is a mud bank to the left of you, but it is very wet and scattered with plants.\n"
    typeText(text)
    goMudOrTree()
    
def goMudOrTree():
    print("Do you:")
    print("A) Go into the mud")
    print("B) Climb the nearby tree and try to jump\nover the stream")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        goMud()
    elif choice.lower() == "b":
        climbTree()
    elif choice.lower() == 'q':
        exit()
    else:
        return goMudOrTree()
    
def goMud():
    text = "\nYou begin crawling in the mud, almost\nsmothered by the low lying bushes above\nyou...your clothes are soiled and stained, but\nyou took the easy way.\n\n"
    typeText(text)
    chooseContinue()
    text = "\nYou barely go over the stream, before you wince as\nyou feel the exhaustion and pain in your legs. Now\nwould you like to rest or journey on?\n"
    typeText(text)
    restOrJourney()
    
def climbTree():
    text = "\nYou shimmy your way up the thick trunk and\nfind yourself, once again, stuck with a left and\nright choice, this time branches."
    typeText(text)
    leftOrRightBranch()
    
def leftOrRightBranch():
    print("Do you:")
    print("A) Take the right branch?")
    print("B) Take the left branch?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        rightBranch()
    elif choice.lower() == "b":
        leftBranch()
    elif choice.lower() == 'q':
        exit()
    else:
        return leftOrRightBranch()  
    
def rightBranch():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nYou slowly creep onto the right branch, and\nquickly look down with uneasiness.\n\n"
    typeText(text)
    text = "Are you getting scared? That's no way for a\nproud elven warrior like you to go down in\nhistory!\n\n"
    typeText(text)
    text = "I can imagine: Warrick the Great Chicken!\n"
    typeText(text)
    jumpOrDown()
    
def jumpOrDown():
    print("Do you:")
    print("A) Climb back down?")
    print("B) Jump?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        text = "You fall a short way and find yourself once\nagain at the tree trunk. Great. Now what?"
        typeText(text)
        goMudOrTree()
    elif choice.lower() == "b":
        jumpDown()
    elif choice.lower() == 'q':
        exit()
    else:
        return jumpOrDown()     
    
def jumpDown():
    track = "Underclocked"
    playMusic(track, 0, 1)
    text = "You barely make it over the stream and wince as your legs absorb the shock from your fall. Now,\nwould you like to rest or journey on?"
    typeText(text)
    restOrJourney()
    
def leftBranch():
    text = "You leap with great grace, almost as if you\nare flying..."
    typeText(text)
    time.sleep(1)
    text = "...wait a minute..."
    typeText(text)
    time.sleep(2)
    text = "You aren't even in the air!\n\n"
    typeText(text)
    time.sleep(1)
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "You've landed in the snout of an\nunusually large alligator. He snaps you up\nquickly, and you are instantly killed.\n"
    typeText(text)
    restartStory()  
    
def restOrJourney():
    print("Do you:")
    print("A) Rest?")
    print("B) Journey on?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        rest()
    elif choice.lower() == "b":
        journeyOn()
    elif choice.lower() == 'q':
        exit()
    else:
        return restOrJourney()
    
def rest():
    text = "\nYou are too tired to go on, and quickly fall\nasleep to the lull of the crickets and\nbullfrogs.\n\n"
    typeText(text)
    text = "However, the next morning, snickers and\ngiggles are heard as small thieves have\nstolen all of your goods and clothes.\n\n"
    typeText(text)
    text = "As you lie in the mud, you realize it is over for\nyou, and you die days later of starvation.\n"
    typeText(text)
    restartStory()
    
def journeyOn():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nYou go on, strong as ever, and walk down a\nstraight path until you reach a small, green\nman wearing a red cloak.\n\n"
    typeText(text)
    text = "He looks somewhat threatening, while remaining still.\n"
    typeText(text)
    killOrSpeak()
    
def killOrSpeak():
    print("Do you:")
    print("A) Try to kill him?")
    print("B) Try to speak to him?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        kill()
    elif choice.lower() == "b":
        speak()
    elif choice.lower() == 'q':
        exit()
    else:
        return killOrSpeak()
    
def kill():
    text = "\nYou lunge at him with your dagger drawn,\nbut are quickly killed as he spins and rakes\nyour eyes out."
    typeText(text)
    restartStory()  
    
def speak():
    text = "\nHe speak your language, but only mutters\nthe words, 'Friend...foe...\n"
    typeText(text)
    friendOrFoe()
    
def friendOrFoe():
    print("A) Friend?")
    print("B) Foe!")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        chooseFriend()
    elif choice.lower() == "b":
        text = "You shout, 'Foe!' before moving forward to attack.\n\n"
        typeText(text)
        kill()
    elif choice.lower() == 'q':
        exit()
    else:
        return friendOrFoe()
    
def chooseFriend():  
    text = "\nYou replay, 'Friend.'.\n\n"
    typeText(text)
    text = "The two of you strike up a conversation,\nquickly becoming friends, but soon the sun\nsets, leaving you with another choice.\n"
    typeText(text)
    talkOrStay()
    
def talkOrStay():
    print("Do you:")
    print("A) Tell him to talk to you later?")
    print("B) Stay with him?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        talk()
    elif choice.lower() == "b":
        stay()
    elif choice.lower() == 'q':
        exit()
    else:
        return killOrSpeak()

def talk():
    text = "\nYou say, 'I'm terribly sorry, but I must go.\nHopefully I will speak to you again soon!\n\n"
    typeText(text)
    text = "He replies, 'Yes...dear traveler...\ncome back...soon.\n\n"
    typeText(text)
    text = "As you leave, you come to a three-way path.\n"
    typeText(text)
    goRightCenterLeft()
    
def stay():
    text = "\nYou say, 'Pardon my intrusion, but may I stay\nwith you for the night? I hope it isn't too much\ntrouble, for I am very weary!\n\n"
    typeText(text)
    text = "He answers, 'Oh...sure! Stay...as long as you like.\nYou...are my good friend!\n\n"
    typeText(text)
    text = "You go to his house and find his children, all 35\nof them! You sleep very little, as the kids are\ntalking to you all night. However, in the\nmorning, you quickly steal away while the\npeople are sleeping and return to your\nadventures.\n\n"
    typeText(text)
    text = "You come to a three-way path.\n"
    typeText(text)
    goRightCenterLeft()
    
def goRightCenterLeft():
    print("Which way do you take?")
    print("A) Right path")
    print("B) Center path")
    print("C) Left path")
    choice = input("Which do you choose? \n(A/B/C/Q) > ")
    if choice.lower() == "a":
        goRightOrCenterPath()
    elif choice.lower() == "b":
        goRightOrCenterPath()
    elif choice.lower() == "c":
        goLeftPath()
    elif choice.lower() == 'q':
        exit()
    else:
        return goRightCenterLeft()    
    
def goRightOrCenterPath():
    text = "\nYou get lost, but are found by the swamp\ncreature's family. They quickly save you from\nyour predicament and lead lead you safely to the\nedge of the swamp.\n\n"
    typeText(text)
    text = "Suddenly, though, a sacred being comes down\nfrom above and rewards you with the following words:\n\n"
    typeText(text)
    text = "'Let the altitude keep climbing higher...'\n"
    typeText(text)
    chooseContinue()
    continuePlains()

def goLeftPath():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nYou take a single step and quickly fall into\nthe mud, sinking as you go...soon the mud\nhas dried and you are unable to move\nfrom the chest up.\n\n"
    typeText(text)
    text = "You soon die of dehydration.\n"
    typeText(text)
    restartStory()
    
    
def goOcean():
    print("Do you:")
    print("A) Brave the Storm?")
    print("B) Turn back to shore?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        islandAttack()
    elif choice.lower() == "b":
        backShore()
    elif choice.lower() == 'q':
        exit()
    else:
        return goOcean()
    
def islandAttack():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nYou sail through the storm and come\nupon an island. As you sail toward it,\na group of native hurl spears at you.\n"
    typeText(text)
    retreatFightThrow()
    
def retreatFightThrow():
    print("Do you:")
    print("A) Retreat?")
    print("B) Fight back with jolts of electricity?")
    print("C) Throw fireballs?")
    choice = input("Which do you choose? \n(A/B/C/Q) > ")
    if choice.lower() == "a":
        backShore()
    elif choice.lower() == "b":
        fight()
    elif choice.lower() == "c":
        throwFireballs()
    elif choice.lower() == "q":
        exit()
    else:
        return retreatFightThrow()
    
def fight():
    text = "\nThere are too many spears! You die!"
    typeText(text)
    restartStory()
    
def throwFireballs():
    text = "\nYou set spears on fire, one by one. Some fallen\nspears hit other spears and ignite them. The\nnatives retreat to another island.\n"
    typeText(text)
    followBack()
    
def followBack():
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "\nYou get to the island and are greeted by\nanother tribe. They won't let you leave. You\nlive happily ever after with them.\n"
    typeText(text)
    restartStory()
    
def backShore():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\nOn your way back to shore, you come upon\nthe Vhwortyzaxisnghkepqublcfdjm! One head\nalways lies and the other always tells the truth.\n\n"
    typeText(text)
    text = "'One path leads to certain death, the other\n leads to freedom,' the heads intone.\n"
    typeText(text)
    text = "You can only ask one question to determine the path\nto take.\n"
    typeText(text)
    heads()
    paths()
    
def heads():
    print("Do you:")
    print("A) Ask the first head a question?")
    print("B) Ask the second head a question?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        head(1)
    elif choice.lower() == "b":
        head(2)
    elif choice.lower() == "q":
        exit()
    else:
        return goOcean()    
    
def head(x):
    print("A) Which path do I take?")
    print("B) Which path would your other head say to take?")
    print("C) Do you lie or tell the truth?")
    if x == 1:
        choice = input("What do you ask the first head? \n(A/B/C/Q) > ")
    else:
        choice = input("What do you ask the second head? \n(A/B/C/Q) > ")
    if choice.lower() == "a":
        if x == 1:
            text = "Take the second path."
            typeText(text)
        else:
            text = "Take the first path."
            typeText(text)
    elif choice.lower() == "b":
        if x == 1:  
            text = "The head says, 'My counterpart would say to take the first path."
            typeText(text)
        else:
            text = "The head says, 'My counterpart would say to take the second path."
            typeText(text)
    elif choice.lower() == "c":
        text = "The head replies, 'I only speak the truth.'"
        typeText(text)
    elif choice.lower() == "q":
        exit()
    else:
        return head()
    
def paths():
    print("Do you:")
    print("A) Choose the first path?")
    print("B) Choose the second path?")
    choice = input("Which do you choose? \n(A/B\Q) > ")
    if choice.lower() == "a":
        pathOne()
    elif choice.lower() == "b":
        pathTwo()
    elif choice.lower() == "q":
        exit()
    else:
        return paths()
    
def pathOne():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n'You chose the wrong path!' ,the Vhwortyzaxisnghkepqublcfdjm screams.\nAnd you die. Just like that."
    typeText(text)
    restartStory()
    
def pathTwo():
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "\n'You choose the correct path.'\n\n"
    typeText(text)
    text = "As you land on the shore, you see that you have passed the swamp and are going to\nenter the plains. However, a bottle that has washed ashore catches your eye.\nYou pick it up and notice that a rolled up paper is inside of it. You manage to get the\npaper out and open it. It has a message written on it that says...\n\n"
    typeText(text)
    text = "'Let the altitude keep climbing higher'\n\n"
    typeText(text)
    text = "You continue on to the plains.\n"
    typeText(text)
    continuePlains()
    
def continuePlains():
    text = "\nAs you enter the wide open plains you feel a\nsudden gust of wind as you realize just how\nfar you have to go before you reach your final\ndestination.\n\n"
    typeText(text)
    text = "The grass is slightly higher than your waist\nand is so thick you can hardly see your feet.\n\n"
    typeText(text)
    text = "Knowing you have limited time, you try to\nlogically think out the course you should take.\n"
    typeText(text)
    trailOrPath()
    
def trailOrPath():
    print("Do you:")
    print("A) Choose the old, weed-covered trail to the\nleft over the grassy knoll?")
    print("B) Choose the dirt path to the right. The\npath seems to have small footprints of an\nunknown origin.")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        trail()
    elif choice.lower() == "b":
        dirtPath()
    elif choice.lower() == "q":
        exit()
    else:
        return trailOrPath()    
        
def trail():
    text = "\nYou decide to take the less beaten path to the\nleft. As you start walking, the grass is\nbecoming too tall for your short body so you\ntake your sword from its sheath and begin to\nslash down the weeds in your path.\n\n"
    typeText(text)
    text = "You're hoping to have found a shortcut, but\ninstead it only leads into a small creek that\nwinds and bends through dense weeds.\n"
    typeText(text)
    creekOrShortcut()
    
def dirtPath():
    text = "\nThe dirt path appeals to you despite the fear that the\nfootprints may lead to something you may not like.\nEverything is going fine until you hear faint screeching\ncoming closer and closer through the surrounding\nbrush.\n\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "You pull out your spellbook and try to cast a\nprotective spell before whatever is making the sound\nis upon you. Minutes turn into seconds and the\nsounds are so close you can hear the footsteps. The\n spell is almost complete, but before you can finish it,\nsmall, green wretched-looking monsters leap out of the\nbush. They are even more hideous than you could\never have imagined. Their mouths are seeping\noozing saliva and they are staring at you with red,\ndevil-like eyes.\n"
    typeText(text)
    speakOrBanish()
    
def speakOrBanish():
    print("Do you:")
    print("A) Speak with them and try to become friends?")
    print("B) Try to banish them to another time and\nplace with a fast activating spell, and be on your\nway?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        speakFriend()
    elif choice.lower() == "b":
        banish()
    elif choice.lower() == "q":
        exit()
    else:
        return speakOrBanish() 
        
def speakFriend():
    text = "\nYou try to reason with yourself on what to do, and you\ndecide to try to talk to the monsters. You think they might\nknow a shortcut, considering that they live on the plains.\nYou pick out the largest creature and being to talk to it in\nevery language you know. As you grow tired of trying,\nthe whole band of animals start to chirp in a high-pitched\nsound. You become alarmed and begin to slowly ease\nyour way to the safety of a nearby tree just large enought to\nsupport your weight.\n\n"
    typeText(text)
    text = "Then comes the screeching from behind you as you bump into a\n slimy, grotesque-looking monster! You are now so frightened that you forget all logic and take off running.\nYou soon find out how bad of an idea running is as the screeching\nbecomes louder and encircle you completely. Monsters from\n all sides leap onto you with teeth bared.\n"
    typeText(text)
    restartStory()
    
def banish():
    text = "\nYou are fed up with things stopping you from reaching your\nfinal destination, so you decide to banish the wretched\ncreeatures standing before you to another time and another\nplace with a spell. You pull out your spellbook very slowly as\n the monsters stare at you with a cross-eyed look. Page by\npage you turn until you find the spell you want. Wasting no\ntime you begin chanting the words of the spell out loud.\n"
    typeText(text)
    text = "The monsters seem amused at first, but they stop chirping\nand begin to screech. They start to leap at you just as\nyou are mid-sentence of your last chant. Instinctively you\ngrab for your sword and lash out at the first one you see. The\n monsters are somehow stopped by the powerful blows and as a\nresult, several are now lying around you in a morbid mess of\nblood and decapitated limbs.\n"
    typeText(text)
    chooseContinue()
    text = "You initial success appears to anger the remaining creatures\nand they increase the intensity of their attacks. Soon\nyou are no match for them as you fall victim to their\nsuperior numbers. You slowly and painfully die as you are devoured\nwhole.\n"
    typeText(text)
    restartStory()
    
def creekOrShortcut():
    print("Do you:")
    print("A) Follow the creek so that if you come upon\nthe desert you'll have water before entering?")
    print("B) Follow the shortcut branching off of the\ncreek to the desert?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        creek()
    elif choice.lower() == "b":
        shortcut()
    elif choice.lower() == "q":
        exit()
    else:
        return creekOrShortcut()    
    
def shortcut():
    text = "\nYou decide to save a tremendous amount of much-needed\ntime and take the shortcut. It makes more sense to take the\nshortcut, because it's so much easier to walk through the\nshorter grass than to continue through the long grass.\n"
    typeText(text)
    chooseContinue()
    text = "\nYou walk."
    typeText(text)
    chooseContinue()
    text = "And walk..."
    typeText(text)
    chooseContinue()
    text = "And walk..."
    typeText(text)
    chooseContinue()
    text = "It becomes so tiresome that you cannot continue any longer and you\nhave to stop.\n\n"
    typeText(text)
    text = "You reach for your pouch for a drink of water, but instead of\nwater there is only air. You throw the pouch down in disgust,\nand as you throw it down you notice a hole in the bottom.\nYou become angered that you didn't notice that when you\nput the water in the pouch.\n"
    typeText(text)
    digOrGiveUp()
    
def digOrGiveUp():
    print("Do you:")
    print("A) Try to dig for life-saving water and then one you find it\nyou can continue?")
    print("B) Give up because you know you will die even if you find\nwater?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        dig()
    elif choice.lower() == "b":
        giveUp()
    elif choice.lower() == "q":
        exit()
    else:
        return digOrGiveUp()
    
def dig():
    text = "\nYou decide that you would rather try to preserve\nyour life as long as possible, so you dig for water.\nYou choose a place right under the closest tree\nand begin to dig as fast as humanly possible.\nYour decision to dig has paid off because you\nfound an underground stream!\n\n"
    typeText(text)
    text = "You drink the water in huge gulps, barely\nstopping for air. After you have your fill of the ice-cold\nwater, you lie down to rest.\n\n"
    typeText(text)
    text = "Your sleep is interrupted by an indescribably\npain in your stomach. It feels as though a knife is\ntearing through your entire body. As you lose\nconsciousness, you figure out that the cause of\nyour pain is the bad water. Thinking only of your\nmistake, you let death come.\n"
    typeText(text)
    restartStory()
    
def giveUp():
    text = "\nYou decide not to even attempt to find water\nbecause you know you will die anyway.\n\n"
    typeText(text)
    text = "As you drift away into unconsciousness, you\nthink of everything you will be leaving behind\nyou. It all depresses you very much, but at least\nyou die in peace and without suffering.\n"
    typeText(text)
    restartStory() 
    
def creek():
    text = "\nYou fill your small rawhide pouch with the creek water,\nand then continue alongside the small creek. It is\ntaking a long time to walk to the desert. You begin to\nwonder if the other choice had been a better one, but\nsoon dismiss the thought as the tall grass stops. You\ncan see the desert once more, and you still have your\npouch full. After you take a small drink of water and\nsit down slowly to rest, you notice the ten-foot wide\ngap in front of you. You curse out at yourself for not\nseeing it earlier, because now you have one more\nproblem to add to your ever-increasing list of troubles.\n"
    typeText(text)
    jumpOrMagic()
    
def jumpOrMagic():
    print("Do you:")
    print("A) Get up and try to jump across the gap, and\nprove to yourself you don't always need the aid of magic?")
    print("B) Use your magic to float across the gap and\nsave some of the energy you may need along your trek?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        jump()
    elif choice.lower() == "b":
        magic()
    elif choice.lower() == "q":
        exit()
    else:
        return digOrGiveUp()  
    
def magic():
    text = "\nYou think using your magic is the better choice, so you\ncarefully take out the old spellbook and begin to cast the\nspell. As you start, a whirling wind seems to form out of\nnowhere and beings to slowly pick you up off of the sandy\nground. It has a calming effect on you, so you close your\neyes and just let the spell carry you over the gap.\n\n"
    typeText(text)
    text = "As you are floating, you notice that it is taking forever to get\nacross a mere ten feet. Cautiously you open your eyes.\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "All you see around you are dirt walls that are quickly\nspeeding by.\n\n"  
    typeText(text)
    text = "You suddenly panic and look down to see your fate.\nTwenty giant spikes are awaiting you at the bottom of the\npit. In seconds you will be impaled by at least three spikes.\nYour life flashes before your eyes and you know you have\nfailed. You die a death of dishonor.\n"
    typeText(text)
    restartStory()
    
def jump():
    text = "\nYou choose to try and jump across the ten feet of space by\nyourself. In preparation, you judge the distance and the\namount of strides you will need to take in order to make it.\nYou are ready after a long and fearful preparation. Once\nmore you look down at the sandy and worn-looking ground and\nsay an old elven prayer your mother once told you for good luck.\nThen you know it's time.\n\n"
    typeText(text)
    text = "You take off as fast as your tiny legs can take you. You\napproach the edge thinking only of making it, and then you finally jump.\n"
    typeText(text)
    chooseContinue()
    text = "It seems to take forever for something to happen. Suddenly\nyou open your eyes to see that you might not make it. You kick\nyour legs in one last desperate attempt to make it and, to\n your surprise, you do.\n\n"
    typeText(text)
    text = "The shock makes your legs give way and you fall, but you\ndon't notice because you're kissing the ground and looking back\nat how far you actually jumped. You rest once more and then\ntry to decide what to do.\n"
    typeText(text)
    summonOrWalk()

def summonOrWalk():
    print("Do you:")
    print("A) Try to summon a beast to carry you to the desert?")
    print("B) Try to walk the 5+ miles on foot without aid?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        summon()
    elif choice.lower() == "b":
        walk()
    elif choice.lower() == "q":
        exit()
    else:
        return summonOrWalk()    
        
def walk():
    text = "\nYou evaluate the amount of strength you have\nleft and you decide to on by yourself.\n\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "You have not walked more than a mile when\nthe sky turns a deathly black, the clouds swirl in\n a threatening wind, and the grass of the plains\ngrab hold of you with its long, waving blades.\n\n"
    typeText(text)
    text = "You shiver in fear as the brilliant yellow flash of\nlightning consumes your body, rendering you helpless under its power, and finally as the\nlightning is gone you fall limp and die.\n"
    typeText(text)
    restartStory()
    
def summon():
    text = "\nYou once again decide to take the easy way and\nsummon a beast to carry you the rest of the\nway to the desert. Before you can even attempt\nto summon anything you need to collect certain\nmaterials, all of which can be easily obtained from the area around you.\n\n"
    typeText(text)
    text = "You first pick up a handful of sand, then mix it\nwith some water from the earth, and finally you\nbegin to mix that concoction together with\n your very own blood from a cut your make with\nyour sword. As the ingredients mix together, a beast starts to appear\nbefore you. It has a dark brown, shaggy coat like a buffalo,\nbeady eyes like a rat, and a massive body like an elephant.\n"
    typeText(text)
    chooseContinue()
    text = "You're a little intimidated at first, as the animal\nonly stares at you and snorts, but you soon\ncome to realize it's a gentle creature and you\nclimb on its back.\n\n"
    typeText(text)
    text = "It lurches forward at a blinding speed, and in a\nmatter of a few seconds you are at the edge\nof the desert. You blink and slowly dismount the\ngiant beast. As you do, the animal slowly disappears\ninto the air around you.\n\n"
    typeText(text)
    text = "As the beast fades, a raspy voice, barely audible\ntells you, 'That which falls upon his head.'\n\n"
    typeText(text)
    text = "You take your first step on the blistering hot\nsand of the desert, try to breathe through the\nheat, and begin perhaps the most grueling walk\nyou have ever attempted.\n"
    typeText(text)
    desert()
    
def desert():
    track = ""
    playMusic(track, 0, 1)
    text = "\nYou enter the Moseekan Desert on the island of\nAnagua. The temperatures in the desert are\nextremely hot. The temperatures sometimes\nreach 125 degrees. Beware! Many strange\ncreatures live in the Moseekan.\n\n"
    typeText(text)
    text = "You initially take a westerly course. You soon\ncome to an enormous rock in the middle of your\npath. It has a distinctive column of rock\nthat juts straight up into the air. You\ngo around the rock and continue on your way.\n\n"
    typeText(text)
    chooseContinue()
    text = "\nAfter about two miles, you come upon a giant\nsand dune that disrupts your path.\n"
    typeText(text)
    northwestWestSouthwest()
    
def northwestWestSouthwest():
    print("Do you:")
    print("A) Go northwest around the dune?")
    print("B) Continue west over the dune?")
    print("C) Travel southwest around the dune?")
    choice = input("Which do you choose? \n(A/B/C/Q) > ")
    if choice.lower() == "a":
        northwest()
    elif choice.lower() == "b":
        west()
    elif choice.lower() == "c":
        southwest()
    elif choice.lower() == "q":
        exit()
    else:
        return northwestWestSouthwest()    

def west():
    text = "\nYou start the long climb up the giant sand dune.\nYour climb up the dune is easy at first but soon\ngets steeper. Your easy climb is now very\ndifficult.\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nAll of a sudden you slip and grab onto a vine.\nThe vine turns out to be a snake! It bites you\nand injects its deadly venom.\n\n"
    typeText(text)
    text = "He then eats you for dinner.\n"
    typeText(text)
    restartStory()
    
def northwest():
    text = "\nYou continue your treacherous walk around the\nnorth side of the dune.\n\n"
    typeText(text)
    text = "As you go, your mouth begins to feel like\nsandpaper. Each step you take makes it worse.\n"
    typeText(text)
    turnEndure()
    
def turnEndure():
    print("Do you:")
    print("A) Turn back?")
    print("B) Endure the heat and continue in the hope\nof finding water?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        turnBack()
    elif choice.lower() == "b":
        endure()
    elif choice.lower() == "q":
        exit()
    else:
        return turnEndure()
    
def turnBack():
    text = "\nYou decide to turn back and try to get back to\nthe rock.\n\n"
    typeText(text)
    text = "You see a row of cacti and decide to follow along\nthe row. You come to a break in the row.\n"
    typeText(text)
    straightRight()
    
def straightRight():
    print("Do you:")
    print("A) Keep going straight?")
    print("B) Turn to the right?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        keepStraight()
    elif choice.lower() == "b":
        turnRight()
    elif choice.lower() == "q":
        exit()
    else:
        return straightRight()     
    
def keepStraight():
    text = "\nYou keep going along the cactus row. Eventually\nit ends.\n\n"
    typeText(text)
    text = "By now you are really lost and can't find your\nway back.\n\n"
    typeText(text)
    text = "You soon become thirsty and die slowly in the\nhot heat of the desert.\n"
    typeText(text)
    restartStory()
    
def turnRight():
    text = "\nTurning right, you wander in the extreme heat\ntrying to find a familiar object. You soon see the\ndistinctive rock in front of you.\n\n"
    typeText(text)
    text = "You continue toward the rock and are at the spot\nfrom which you started. You go around the rock\nand continue on your way.\n\n"
    typeText(text)
    text = "After about two miles, you come upon the giant sand dune that disrupts your path.\n"
    typeText(text)
    northwestWestSouthwest()
    
def endure():
    print("Do you:")
    print("A) Turn back?")
    print("B) Endure the heat and continue in the hope\nof finding water?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        turnBack()
    elif choice.lower() == "b":
        hope()
    elif choice.lower() == "q":
        exit()
    else:
        return endure()         
    
def hope():
    text = "\nYou are walking aimlessly in the scorching\ndesert. You are becoming very thirsty.\n\n"
    typeText(text)
    text = "You come upon a large cactus.\n"
    typeText(text)
    cactus()
    
def cactus():
    print("Do you:")
    print("A) Try to get water from the cactus?")
    print("B) Leave it alone and continue?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        getWater()
    elif choice.lower() == "b":
        leaveAlone()
    elif choice.lower() == "q":
        exit()
    else:
        return cactus()  
    
def getWater():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\nYou are intelligent enough to know there was a\nrefreshing liquid in the cactus.\n\n"
    typeText(text)
    text = "You pull out your trusty sword and slice off a\npiece. You hold it over your mouth and let\nthe liquid drip into your mouth.\n\n"
    typeText(text)
    text = "What you didn't know was that some cactus juice\nis poisonous.\n"
    typeText(text)
    restartStory()  
    
def leaveAlone():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\nYou leave the cactus alone. You continue on your\npath through the desert.\n\n"
    typeText(text)
    text = "You see an oasis and go towards it in search of\nwater.\n"
    typeText(text)
    oasis()
    
def southwest():
    text = "\nYou choose to go southwest around the giant\nsand dune.\n\n"
    typeText(text)
    text = "When you round the southern tip of the dune,\nyou come upon a sandworm. It is thirty\nfeet long and has rough brown skin.\n"
    typeText(text)
    runOrFight()
    
def runOrFight():
    print("Do you:")
    print("A) Run back?")
    print("B) Stay and fight it with your sword?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        northwestWestSouthwest()
    elif choice.lower() == "b":
        worm()
    elif choice.lower() == "q":
        exit()
    else:
        return runOrFight()
    
def worm():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\nYou choose to stay and fight the sandworm. You\n pull out your sword. It glimmers in the bright sun.\n"
    typeText(text)
    heartOrHead()
    
def heartOrHead():
    print("Do you:")
    print("A) Stab at the heart?")
    print("B) Swipe at the head?")
    choice = input("Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        stabHeart()
    elif choice.lower() == "b":
        swipeHead()
    elif choice.lower() == "q":
        exit()
    else:
        return heartOrHead()   
    
def swipeHead():
    text = "\nYou swipe at the sandworm's head. He ducks\nand you wiff.\n\n"
    typeText(text)
    text = "It is furious and is slithering directly at\nyou as fast as a speeding train.\n\n"
    typeText(text)
    text = "You close your eyes. Goodbye!\n"
    typeText(text)
    restartStory()
    
def stabHeart():
    text = "\nYour stab at the sandworm's heart and\nthe sharp blade of your sword pierces it.\nThe creature falls down, dying in great pain.\n\n"
    typeText(text)
    text = "You see an oasis and you decide to walk\ntowards it.\n"
    typeText(text)
    oasis()
    
def oasis():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\nYou walk into the green oasis. You haven't seen\nthis color for a long time. You sit down on the\nedge of the pond. You take a long refreshing\ndrink. Feeling tired, you fall asleep in the shade\nof a palm tree.\n\n"
    typeText(text)
    text = "In the middle of your long nap you feel a blow to\nyour head. On the ground at your side is a coconut.\nYou pick it up and it breaks in two. Inside you find a\nmysterious piece of paper stating,\n'Will strike him down, forever dead\n\n"
    typeText(text)
    text = "Rubbing your head, you look up to see the\nmountains before you. You know they hold the\nlair of the dragon and the end of your quest...\nbut hopefully not the end of you.\n\n"
    typeText(text)
    text = "Gathering your supplies, you move on.\n"
    typeText(text)
    mountains()
    
def mountains():
    text = "\nYou finally make it out of the barren desert.\nYou look before you and see the vast\nmountain lair of the Great Dragon. You make\nthe hike up and enter the twisted caves.\n\n"
    typeText(text)
    text = "You hear the sound of dripping water\nthroughout the cavern and a stingy mist is in the air. All of a sudden you hear it. Heavy\nbreathing coming from one of the paths. You\nfollow the sound to a large cavernous room.\n\n"
    typeText(text)
    text = "THE LAIR OF THE DRAGON!\n"
    typeText(text)
    theLair()
    
def theLair():
    text = "\nYou look around quickly and see huge piles of gold...his\nhoard.\n\n"
    typeText(text)
    text = "Sitting between piles is a huge dark form. A loud echoing\nroar erupts from behind the piles.\n\n"
    typeText(text)
    text = "You move closer to investigae. Seeing all the gold, you\nare tempted to take some and flee.\n\n"
    typeText(text)
    text = "You reach forward, and just before you grab some of the\ngold, you are suddenly face-to-face with Golan..."
    typeText(text)
    theFight()
    
def theFight():
    track = "Dungeon Boss"
    playMusic(track, 0, 1)
    text = "\nYou quickly jump aside before being roasted with an enormous gout of fire. Thinking back,\nyou remember the poem. 'This must be the secret,' you think, but you don't quite\nunderstand it. Now it's time for you to make your final decision. What will you use to fight\nthe dragon?\n\n"
    typeText(text)
    text = "'I can use anything around me,' you think as you notice spears, swords, and battleaxes amongst the\nmassive piles of gold. You also have everything you currently carry.\n"
    typeText(text)
    recitePoem()
    
def recitePoem():
    text = "\n   You must swing before you fire"
    typeText(text)
    text = "\nLet the altitude keep climbing higher"
    typeText(text)
    text = "\n   That which falls upon his head"
    typeText(text)
    text = "\n Will strike him down, forever dead\n"
    typeText(text)
    text = "\n 1) Use your sword            \t 2) Use your bow      \t 3) Use your spellbook   \t 4) Use a mace   \t 5) Use a dagger"
    typeText(text)
    text = "\n 6) Say the poem aloud        \t 7) Use a rock        \t 8) Use a handful of dirt\t 9) Sing a song \t10) Fight with your fists"
    typeText(text)
    text = "\n11) Use a torch              \t12) Use your own blood\t13) Use an axe          \t14) Use a whip  \t15) Use a feather"
    typeText(text)
    text = "\n16) Use water from your pouch\t17) Use a sling       \t18) Use a club          \t19) Use a mirror\t20) Use a large diamond"
    typeText(text)
    choice = input("\n\nWhat shalt thou use to slay the fearsome beast? \n( 1/ 2/ 3/ 4/ 5)\n( 6/ 7/ 8/ 9/10)\n(11/12/13/14/15)\n(16/17/18/19/20) > ")
    if int(choice) == 17:
        youWin()
    elif int(choice) <= 16 or int(choice) >= 18:  
        youLose()
    else:
        return recitePoem()
    
def youLose():
    text = "\nYou have made your choice.\n\n"
    typeText(text)
    text = "It has no effect on Golan other than to give him a\nslight chuckle at your foolish and worthless\nattempt to slay him.\n\n"
    typeText(text)
    text = "You frantically try to remember the poem more\nclearly. What hidden meaning did it hold? What\nhave you missed?\n\n"
    typeText(text)
    text = "Unfortunately, Golan does not miss the opportunity\nas he releases another blast of fire."
    typeText(text)
    restartStory()
    
def youWin():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\nYou think back to the lines of the poem you have received throughout your quest. As you\npull your sling from your holster resting on your belt. You are hoping this was the best\nchoice. You run behind a vast pile of gold and take careful aim. Round and round you\nswing the sling until..."
    typeText(text)
    chooseContinue()
    text = "WOOOOOOSH!!!!!!!!!\n"
    typeText(text)
    chooseContinue()
    text = "\nThe small round stone punctures the are right between the dragon's eyes! The stunned\nbeast falls hard to the ground, shaking the whole cavern. Could it be true the Great Golan\nhas been slain?\n"
    typeText(text)
    chooseContinue()
    text = "Yes! You finally recall it after studying the motionless dragon. You remember the\nsquire's words from the beginning of your quest. You walk calmly over to the dragon and\npry one of his blade-like teeth from his jaws of death. Now that the hard part is over, you\nmust return to the castle with the good word!\n"
    typeText(text)
    toTheCastle()
    
def toTheCastle():
    track = "[You win]"
    playMusic(track, 0, 1)
    text = "\nThe King is sitting in his throne room when you walk into\nHis presence. You speak up nervously of your news\nand hold up the dragon tooth. The King slowly looks up\nwith a broad smile on his face. He congratulates you\nand announces a celebration in your honor and of\nyour upcoming wedding with his fair daughter. For the\nfirst time on your long and grueling quest, you feel a sense of joy. You go right to the town tailor with your\n gold and buy his finest cloak. Your quest is finally\nover!\n\n"
    typeText(text)
    text = "You marry the princess in a romantic ceremony held on the\nshore beside the King's castle. At the end of the\nceremony, the King places a large golden crown on\nyour head as the large crowd yells and screams your\nname in great excitement.\n\n"
    typeText(text)
    chooseContinue()
    text = "\nYou are the new prince of Anagua.\n\n"
    typeText(text)
    text = "Warrick the Elf!\n"
    typeText(text)
    restartStory()
    
def runMain():
    track = "Itty Bitty"
    playMusic(track, 1, 1)
    printIntro()
    chooseContinue()
    printIntro2()
    chooseContinue()
    printIntro3()
    startAdventure()
    
if __name__ == '__main__':    
    runMain()