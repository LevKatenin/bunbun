# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("bunbun")

define n = Character("")

image bunbun test:
    "bunbun test1.png"
    0.5
    "bunbun test2.png"
    0.5
    repeat
     
# The game starts here.

label start:

    stop music

    scene bg empty

    show screen actionmenu

    show screen windowframe

    n "And so it begins"

    show bunbun test

    b "The quick brown fox jumps over the lazy dog."

    b "Съешь ещё этих мягких французских булок, да выпей же чаю."

    b "Translate this too please."

    b "I am just a test sprite. You will likely never see me again! I am just a test sprite. You will likely never see me again! I am just a test sprite. You will likely never see me again! I am just a test sprite. You will likely never see me again!"

    return
