# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define mascotfemale = Character("Delilah")

transform double_size:
    zoom 1.5

image teststreet = im.Scale("background/teststreet.png", 1920, 1080)

image intro_video = Movie(size = (1920,1080), channel="movie", play="video/IntroPortal.webm", loop=True)

# The game starts here.

label start:
    show intro_video
    #intro video virker ikke, idk why, fiks senere
    show mascotfemale at center
    mascotfemale "Welcome to the game!"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show teststreet

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show testaqua at double_size, center


    # These display lines of dialogue.

    e "Something blah."

    e "Get Cancer love"

































    # This ends the game.

    return
