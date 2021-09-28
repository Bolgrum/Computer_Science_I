import time
from DragonQuest import typeText
def countDown(count):
    if count == 0:
        time.sleep(1)
        print('Go!')
    else:
        time.sleep(1)
        print(count)
        countDown(count-1)

text = "\n   You must swing before you fire"
typeText(text)
text = "\nLet the altitude keep climbing higher"
typeText(text)
text = "\n   That which falls upon his head"
typeText(text)
text = "\n Will strike him down, forever dead"
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