﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    show cedric cocktail
    cedric.character "I'm wonderful!"

    # show joe
    joe.character "Something, something Country justice!"
    
    cedric.character normal "You know it."

    call chapter1

    return