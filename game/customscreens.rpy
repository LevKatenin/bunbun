## The game overlay frame

screen windowframe():
    image "gui/windowframe.png"
    zorder 100
    
## Action menu that lets the player choose what to do

screen actionmenu():
    style_prefix "actionmenu"

    image "gui/actionmenu.png" xpos 1480 ypos 780 zoom 2.0
    zorder 50

    grid 2 2:
        xpos 1540 ypos 840         

        textbutton _("Button1") 
          
        textbutton _("Button2") xpadding 20 
        
        textbutton _("Button3") ypadding 10
            
        textbutton _("Button4") xpadding 20 ypadding 10 