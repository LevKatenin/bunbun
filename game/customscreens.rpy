
## The game overlay frame

screen windowframe():
    image "gui/windowframe.png"
    zorder 100

## Inventory overlay, not modal, so allows clicking other items on the screen

screen inventory():
    style_prefix "inventory"

    image "gui/inventorybox.png" xpos 30 ypos 30 zoom 2.0
    zorder 60

    vpgrid:
        mousewheel True

        xysize (400, 750)
        
        xpos 75
        ypos 150

        cols 1
        spacing 5
        xspacing 200

        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"
        textbutton "item"

## Action menu that lets the player choose what to do

screen actionmenu():
    modal True
    style_prefix "actionmenu"

    image "gui/actionmenu.png" xpos 1480 ypos 780 zoom 2.0
    zorder 50

    grid 2 2:
        xpos 1540 ypos 840         

        textbutton _("action") action Play("sound", config.sample_sound) #this is a test button. todo: pull up a choice menu based on location
          
        textbutton _("items") xpadding 20 action ToggleScreen("inventory") ##todo: add inventory management and mouse-over info menu
        
        textbutton _("go to") ypadding 10 #this is where you add the menu that has several "jumps"
            
        textbutton _("sleep") xpadding 20 ypadding 10 #this is where you call the "advance day" function. update flags, show a dream and change date and time

