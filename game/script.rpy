# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#Aqua the mascot character images and info
image mascot = "characters/mascot/mascotfemale.png"
image mascot2 = "characters/mascot/aqua2.png"
image mascot confused = "characters/mascot/aquaconfused.png"
image mascot happy point = "characters/mascot/aquahappypoint.png"
image mascot pointing = "characters/mascot/aquapointing.png"
image mascot dance = "characters/mascot/aquadance.png"
define mascotfemale = Character("Aqua the Mascot", color="#c8c8ff")



#Characters transforms
transform double_size:
    zoom 2

transform half_size:
    zoom 0.5

transform halfdouble_size:
    zoom 1.5

transform fixedmascot_size:
    zoom 1.2

transform upsidedown_character:
    yzoom -1
    yalign -0.3
    xalign 0.5

#Money and inventory system
init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        def __init__(self, money=0):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False



# The game starts here.
label start:
    python:
        inventory = Inventory()
        BigMac = Item("Big Mac", 1)

    screen money_display:
        frame:
            style "money_box"
            text "$[inventory.money]" color "#3e9c35" size 24

    style money_box:
        xpadding 10
        ypadding 5
        background Frame("gui/frame.png")

    show screen money_display

    $ current_money = inventory.money

    image intro_video = Movie(size=(1920, 1080), channel="movie", play="images/video/IntroPortal.webm", loop=True)
    show intro_video
    pause 1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show mascot at fixedmascot_size, center

    # These display lines of dialogue.

    mascotfemale "Hello, i am Aqua"

    mascotfemale "Legal copyright btw"

    mascotfemale "Welcome to the game!"

    hide mascot
    show mascot confused at fixedmascot_size, center

    mascotfemale "Are you over the age of 18?"


    menu:
        "Yes":
            hide mascot confused
            jump mainstorytutorial
        "No":
            mascotfemale "I'm sorry, but you need to be over the age of 18 to play this game."
            hide mascot confused
            return
        "I want to die":
            hide mascot confused
            jump game_over

    # This ends the game.
    return

label game_over:
    image gameover = im.Scale("mainmenuWeSeeYou.png", 1920, 1080)
    show gameover

    show mascot at upsidedown_character

    mascotfemale "Unlucky, better luck next time!"
    $ renpy.quit()

    return

label mainstorytutorial:
    image teststreet = im.Scale("background/streets/teststreet.png", 1920, 1080)
    show teststreet

    show mascot2 at fixedmascot_size, center

    mascotfemale "Perfect! Let's get started."

    mascotfemale "This is a short tutorial to get you started."

    mascotfemale "Do you want to skip the tutorial?"

    menu:
        "It is recommended for new players to play the tutorial."
        "Yes (Skip tutorial)":
            hide mascot2
            jump mainstory
        "No":
            hide mascot2
            jump tutorial

    return

label tutorial:
        


    jump mainstory

    return


label mainstory:
    image teststreet = im.Scale("background/streets/teststreet.png", 1920, 1080)
    show teststreet

    show mascot dance at center

    mascotfemale "Let's get started!"

    mascotfemale "Seems like you're a bit poor"
    mascotfemale "You have $[inventory.money] currently"
    mascotfemale "Let me give you 20 dollars to start off with."

    $ inventory.earn(20)

    "You now have $[inventory.money] dollars"



    

    return