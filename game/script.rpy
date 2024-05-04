# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
image mascot = "characters/mascotfemale.png"
define mascotfemale = Character("Aqua the Mascot", color="#c8c8ff")


#Image transforms are used to change the size of images. The zoom argument
transform double_size:
    zoom 2

transform half_size:
    zoom 0.5

transform halfdouble_size:
    zoom 1.5

transform fixedmascot_size:
    zoom 1.2


image intro_video = Movie(size = (1920,1080), channel="movie", play="video/IntroPortal.webm", loop=True)

# The game starts here.

label start:
    #show intro_video
    #intro video virker ikke, idk why, fiks senere
    show mascot at fixedmascot_size, center

    mascotfemale "Welcome to the game!"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    hide mascot

    image teststreet = im.Scale("background/streets/teststreet.png", 1920, 1080)
    show teststreet

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mascot at fixedmascot_size, center


    # These display lines of dialogue.

    mascotfemale "Something blah."

    mascotfemale "Get Cancer love8"

    hide mascot

    image cafe start = im.Scale("background/buildings/cafe1.png", 1920, 1080)
    show cafe start

    show mascot at fixedmascot_size, right


    mascotfemale "I'm going to the cafe."




    # This ends the game.

    return

