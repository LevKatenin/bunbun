

## The game overlay frame

screen windowframe():
    image "gui/windowframe.png"
    zorder 100

## Inventory overlay, not modal, so allows clicking other items on the screen

screen inventory():
    style_prefix "inventory"

    image "gui/inventorybox.png" xpos 30 ypos 30 zoom 2.0
    zorder 60

## Action menu that lets the player choose what to do

screen actionmenu():
    modal True
    style_prefix "actionmenu"

    image "gui/actionmenu.png" xpos 1480 ypos 780 zoom 2.0
    zorder 50

    grid 2 2:
        xpos 1540 ypos 840         

        textbutton _("squeak") action Play("sound", config.sample_sound)
          
        textbutton _("items") xpadding 20 action ToggleScreen("inventory")
        
        textbutton _("Button3") ypadding 10
            
        textbutton _("Button4") xpadding 20 ypadding 10

