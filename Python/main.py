from asyncio.windows_events import NULL
import pygame
import pygame_gui

from dbManager import DbManager


#--------[Meta]------------------------------------------
pygame.init()
#Auflösung
res = (680, 420)
screen = pygame.display.set_mode(res)
#Game Fenster
background = pygame.Surface(res)
manager = pygame_gui.UIManager(res, 'Themes/base.json')
#manager.get_theme().load_theme('Themes/label.json')
#manager.get_theme().load_theme('Themes/button.json')
clock = pygame.time.Clock()
#----------[/Meta]----------------------------------------
#----------[Funktionen]---------------------------------
#Rules Windows
def open_popup(text,title,width,height):
    rules_window = pygame_gui.windows.ui_message_window.UIMessageWindow(rect=pygame.Rect((res[0]/2-200,10),(width,height)),html_message=text,manager=manager,window_title=title)
    
#-----------[/Funktionen]----------------------------------
#-----------[Langtexte]---------------------------------
game1_rule = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
game2_rule = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
game3_rule = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."


#-----------[/Langtexte]--------------------------------
#--------------------[Main Menu-Screen]-----------------------------------

def main_menu():

    manager.clear_and_reset()
    pygame.init()

    #Hintergrundfarbe
    background.fill(pygame.Color("#3c3c3c"))
    
    #--------------------Elemente------------------------
    #Label
    menu_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((res[0]/2-150, 20), (300, 50)), text="Hauptbildschirm", manager=manager)
   
    #User Menu
    user_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (70, 50)), text='User', manager=manager)
    dd_menu = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (200, 205)),starting_layer_height=0, manager=manager,visible=0)
    signin_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 100), (190, 50)), text="Anmelden", manager=manager,visible=0,starting_height=3)
    signup_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 150), (190, 50)), text="Registrieren", manager=manager,visible=0,starting_height=3)
    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 200), (190, 50)), text="Quit", manager=manager,visible=0,starting_height=3)

    ##Anmelden & Registrieren ----
    loginWindow = 0  # 0 = both closed | 1 = login opened | 2 = registration opened
    user_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, 50), (190, 30)), text="Angemeldet als:", manager=manager,visible=0)
    username_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, 70), (190, 30)), text="Gast/Username", manager=manager,visible=0)
    id_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, 150), (190, 30)), text="Benutzername:", manager=manager,visible=0)
    id_txtentry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((5, 180), (190, 30)), manager=manager,visible=0)
    pw_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, 210), (190, 30)), text="Passwort:", manager=manager,visible=0)
    pw_txtentry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((5, 235), (190, 30)), manager=manager,visible=0)
    ok_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 270), (95, 30)), text="Ok", manager=manager,visible=0)
    ##-------------
    
    
    #Main Buttons Dimension
    button_height = 75
    big_button_width = 300
    small_button_width = 75
    button_vert_gap = 10
    button_hori_gap = 10
    button_vert_startposition = 100
    button_hori_startposition = 100
    gamebutton_offset = (button_hori_startposition)
    rulesbutton_offset = button_hori_startposition+big_button_width+button_hori_gap
    scorebutton_offset = button_hori_startposition+big_button_width+(2*button_hori_gap)+small_button_width
   
   #Game1 Buttons
    game1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, button_vert_startposition), (big_button_width, button_height)),
                                             text='Game1', manager=manager,starting_height=-2)
    game1_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((rulesbutton_offset, button_vert_startposition), (small_button_width, button_height)),
                                             text='?', manager=manager,starting_height=-2)
    game1_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, button_vert_startposition), (small_button_width, button_height)),
                                             text='Score', manager=manager,starting_height=-2)

    #Game1 Difficulty Buttons
    game1_buttonl = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, button_vert_startposition), (big_button_width/3+4, button_height)),
                                             text='Leicht', manager=manager, visible=0, starting_height=-1)
    game1_buttonm = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((gamebutton_offset+(big_button_width/3)), button_vert_startposition), (big_button_width/3+4, button_height)),
                                             text='Mittel', manager=manager, visible=0, starting_height=-1)
    game1_buttons = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset+(big_button_width/3*2), button_vert_startposition), (big_button_width/3, button_height)),
                                             text='Schwer', manager=manager, visible=0, starting_height=-1)    

    #Game2 Buttons
    game2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (big_button_width, button_height)),
                                             text='Game2', manager=manager,starting_height=-2)
    game2_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((rulesbutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (small_button_width, button_height)),
                                             text='?', manager=manager,starting_height=-2)
    game2_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (small_button_width, button_height)),
                                             text='Score', manager=manager,starting_height=-2)
    
    #Game2 Difficulty Buttons
    game2_buttonl = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (big_button_width/3+4, button_height)),
                                             text='Leicht', manager=manager, visible=0, starting_height=-1)
    game2_buttonm = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((gamebutton_offset+(big_button_width/3)), (button_vert_startposition + button_height + button_vert_gap)), (big_button_width/3+4, button_height)),
                                             text='Mittel', manager=manager, visible=0, starting_height=-1)
    game2_buttons = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset+(big_button_width/3*2), (button_vert_startposition + button_height + button_vert_gap)), (big_button_width/3, button_height)),
                                             text='Schwer', manager=manager, visible=0, starting_height=-1)
    
    #Game3 Buttons
    
    game3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width, button_height)),
                                             text='Game3', manager=manager,starting_height=-2)  
    game3_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((rulesbutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (small_button_width, button_height)),
                                             text='?', manager=manager,starting_height=-2) 
    game3_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (small_button_width, button_height)),
                                             text='Score', manager=manager,starting_height=-2)
    
    #Game3 Difficulty Buttons
    game3_buttonl = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width/3+4, button_height)),
                                             text='Leicht', manager=manager, visible=0, starting_height=-1)
    game3_buttonm = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((gamebutton_offset+(big_button_width/3)), (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width/3+4, button_height)),
                                             text='Mittel', manager=manager, visible=0, starting_height=-1)
    game3_buttons = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset+(big_button_width/3*2), (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width/3, button_height)),
                                             text='Schwer', manager=manager, visible=0, starting_height=-1)
    
    #-----------------------------------------------------
    is_running = True
    while is_running:
        
            
        #Fenster Titel
        pygame.display.set_caption('Spiele')
        
        #Show Elemente
        
        
        time_delta = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            #Buttons Funktionen
                
            if event.type == pygame_gui.UI_BUTTON_PRESSED:   
                #User menu
                if event.ui_element == user_button:
                    if dd_menu.visible == 0:
                        dd_menu.visible = 1
                        quit_button.show()
                        signin_button.show()
                        signup_button.show()
                        user_lbl.show()
                        username_lbl.show()
                        
                        game1_buttonl.hide()
                        game1_buttonm.hide()
                        game1_buttons.hide()
                    
                        game2_buttonl.hide()
                        game2_buttonm.hide()
                        game2_buttons.hide()
                    
                        game3_buttonl.hide()
                        game3_buttonm.hide()
                        game3_buttons.hide()
                        
                        game1_button.show()
                        game2_button.show()
                        game3_button.show()
                    else:
                        dd_menu.visible = 0
                        quit_button.hide()
                        signin_button.hide()
                        signup_button.hide()
                        user_lbl.hide()
                        username_lbl.hide()
                        id_lbl.hide()
                        pw_lbl.hide()
                        id_txtentry.hide()
                        pw_txtentry.hide()
                        ok_button.hide()
                        dd_menu.set_dimensions((200, 205))
                        signup_button.set_position((5,150))
                        quit_button.set_position((5,200))
                        
                if event.ui_element == quit_button:
                    print('Quit!')
                    is_running = False
                    
                if event.ui_element == signin_button:
                    if ok_button.visible == 0 or loginWindow == 2:
                        id_lbl.show()
                        pw_lbl.show()
                        id_txtentry.show()
                        pw_txtentry.show()
                        ok_button.show()
                        id_lbl.set_position((5,150))
                        pw_lbl.set_position((5,210))
                        id_txtentry.set_position((5,180))
                        pw_txtentry.set_position((5,235))
                        ok_button.set_position((5,270))
                        dd_menu.set_dimensions((200, 355))
                        signup_button.set_position((5,300))
                        quit_button.set_position((5,350))
                        loginWindow = 1
                    else:
                        id_lbl.hide()
                        pw_lbl.hide()
                        id_txtentry.hide()
                        pw_txtentry.hide()
                        ok_button.hide()
                        dd_menu.set_dimensions((200, 205))
                        signup_button.set_position((5,150))
                        quit_button.set_position((5,200))
                        loginWindow = 0

                if event.ui_element == signup_button:
                    if ok_button.visible == 0 or loginWindow == 1:
                        id_lbl.show()
                        pw_lbl.show()
                        id_txtentry.show()
                        pw_txtentry.show()
                        ok_button.show()
                        id_lbl.set_position((5,200))
                        pw_lbl.set_position((5,260))
                        id_txtentry.set_position((5,230))
                        pw_txtentry.set_position((5,285))
                        ok_button.set_position((5,320))
                        dd_menu.set_dimensions((200, 355))
                        signup_button.set_position((5,150))
                        quit_button.set_position((5,350))
                        loginWindow = 2
                    else:
                        id_lbl.hide()
                        pw_lbl.hide()
                        id_txtentry.hide()
                        pw_txtentry.hide()
                        ok_button.hide()
                        dd_menu.set_dimensions((200, 205))
                        signup_button.set_position((5,150))
                        quit_button.set_position((5,200))
                        loginWindow = 0

                if event.ui_element == ok_button:
                    open_popup("Das war erfolgreich!", "title", 150, 20)
                    open_popup("Du Opfer!", "title", 150, 20)
                    username = id_txtentry.get_text()
                    password = pw_txtentry.get_text()
                    if len(username) != 0 and len(password) != 0:
                        if loginWindow == 1: # login is active
                            db_manager.login(username, password)
                        elif loginWindow == 2: # registration is active
                            successful = db_manager.register(username, password)                   
                            if successful:
                                open_popup("Das war erfolgreich!", "title", 150, 50)
                            else:
                                open_popup("Du Opfer!", "title", 150, 50)

                
            
                        
                #Game1
                if event.ui_element == game1_button:
                    print('Game1_clicked')

                    gameid = 1

                    game1_button.hide()
                    game2_button.show()
                    game3_button.show()
                    
                    game1_buttonl.show()
                    game1_buttonm.show()
                    game1_buttons.show()
                    
                    game2_buttonl.hide()
                    game2_buttonm.hide()
                    game2_buttons.hide()
                    
                    game3_buttonl.hide()
                    game3_buttonm.hide()
                    game3_buttons.hide()
               
                    dd_menu.visible = 0
                    quit_button.hide()
                    signin_button.hide()
                    signup_button.hide()
                    user_lbl.hide()
                    username_lbl.hide()
                    id_lbl.hide()
                    pw_lbl.hide()
                    id_txtentry.hide()
                    pw_txtentry.hide()
                    ok_button.hide()
                    dd_menu.set_dimensions((200, 205))
                    signup_button.set_position((5,150))
                    quit_button.set_position((5,200))
                    
                if event.ui_element == game1_rules_button:
                    open_popup(game1_rule, "Game1 Regeln", 400, 400)
                    print('Game1_rules_clicked')
                    
                if event.ui_element == game1_score_button:
                    print('Game1_score_clicked')

                if event.ui_element == game1_buttonl:
                    gameframe("Game1",1,"Leicht")
                
                if event.ui_element == game1_buttonm:
                    gameframe("Game1",1,"Mittel")

                if event.ui_element == game1_buttons:
                    gameframe("Game1",1,"Schwer")

                #Game2
                if event.ui_element == game2_button:
                    print('Game2_clicked')

                    gameid = 2

                    game2_button.hide()
                    game1_button.show()
                    game3_button.show()
                    
                    game2_buttonl.show()
                    game2_buttonm.show()
                    game2_buttons.show()
                    
                    game1_buttonl.hide()
                    game1_buttonm.hide()
                    game1_buttons.hide()
                    
                    game3_buttonl.hide()
                    game3_buttonm.hide()
                    game3_buttons.hide()
                    
                    dd_menu.visible = 0
                    quit_button.hide()
                    signin_button.hide()
                    signup_button.hide()
                    user_lbl.hide()
                    username_lbl.hide()
                    id_lbl.hide()
                    pw_lbl.hide()
                    id_txtentry.hide()
                    pw_txtentry.hide()
                    ok_button.hide()
                    dd_menu.set_dimensions((200, 205))
                    signup_button.set_position((5,150))
                    quit_button.set_position((5,200))
                    
                if event.ui_element == game2_rules_button:
                    open_popup(game2_rule , "Game2 Regeln", 400, 400)
                    print('Game2_rules_clicked')
                    
                if event.ui_element == game2_score_button:
                    print('Game2_score_clicked')

                if event.ui_element == game2_buttonl:
                    gameframe("Game2",2,"Leicht")
                
                if event.ui_element == game2_buttonm:
                    gameframe("Game2",2,"Mittel")

                if event.ui_element == game2_buttons:
                    gameframe("Game2",2,"Schwer")

                 #Game3
                if event.ui_element == game3_button:
                    print('Game3_clicked')

                    gameid = 3

                    game3_button.hide()
                    game1_button.show()
                    game2_button.show()
                    
                    game3_buttonl.show()
                    game3_buttonm.show()
                    game3_buttons.show()
                    
                    game1_buttonl.hide()
                    game1_buttonm.hide()
                    game1_buttons.hide()
                    
                    game2_buttonl.hide()
                    game2_buttonm.hide()
                    game2_buttons.hide()
                    
                    dd_menu.visible = 0
                    quit_button.hide()
                    signin_button.hide()
                    signup_button.hide()
                    user_lbl.hide()
                    username_lbl.hide()
                    id_lbl.hide()
                    pw_lbl.hide()
                    id_txtentry.hide()
                    pw_txtentry.hide()
                    ok_button.hide()
                    dd_menu.set_dimensions((200, 205))
                    signup_button.set_position((5,150))
                    quit_button.set_position((5,200))
                    
                if event.ui_element == game3_rules_button:
                    open_popup(game3_rule , "Game3 Regeln", 400, 400)
                    print('Game3_rules_clicked')
                    
                if event.ui_element == game3_score_button:
                    print('Game3_score_clicked')
                    
                if event.ui_element == game3_buttonl:
                    gameframe("Game3",3,"Leicht")
                
                if event.ui_element == game3_buttonm:
                    gameframe("Game3",3,"Mittel")

                if event.ui_element == game3_buttons:
                    gameframe("Game3",3,"Schwer")
                    
                if event.ui_element == quit_button:
                    print('Quit!')
                    is_running = False
                    #pygame.quit()
                    
                             
            manager.process_events(event)
            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.update()
    pygame.quit()
#-----------------[/Main Menu-Screen]-----------------------------------------------------
#-----------------[GameFrame Screen]----------------------------------------------------

def gameframe(game, gameid, difficulty):
    
    #count = 0
    time = ""
    manager.clear_and_reset()
    pygame.init()
    #Hintergrundfarbe
    background.fill(pygame.Color("#3c3c3c"))
    
    #--------------------Elemente---------------------
    #User Menu
    user_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (70, 50)), text='User', manager=manager)
    dd_menu = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (200, 205)),starting_layer_height=0, manager=manager,visible=0)
    restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 100), (190, 50)), text="Neustart", manager=manager,visible=0,starting_height=3)
    menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 150), (190, 50)), text="Hauptmenü", manager=manager,visible=0,starting_height=3)
    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 200), (190, 50)), text="!Keine Funktion!", manager=manager,visible=0,starting_height=3)
    user_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, 50), (190, 30)), text="Angemeldet als:", manager=manager,visible=0)
    username_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, 70), (190, 30)), text="Gast/Username", manager=manager,visible=0)

    #Label
    game_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((res[0]- ((res[0]-res[1])/2),0), ((res[0]-res[1])/2,50)), text=game, manager=manager)
    difficulty_head_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((res[0]- ((res[0]-res[1])/2),50), ((res[0]-res[1])/2,50)), text="Schwierigkeit:", manager=manager)
    difficulty_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((res[0]- ((res[0]-res[1])/2),75), ((res[0]-res[1])/2,50)), text=difficulty, manager=manager)
    timer_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((res[0]- ((res[0]-res[1])/2),150), ((res[0]-res[1])/2,50)), text=time, manager=manager)

    #Panel
    game_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(((res[0]/2)-(res[1]/2),0), (res[1], res[1])),starting_layer_height=-1, manager=manager,visible=1)

    #Buttons
    rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,res[1]-40), (40, 40)),
                                             text='?', manager=manager,starting_height=-2)
    
    #---------------------------------------------------
    is_running = True
    while is_running:
       
        #Fenster Titel
        pygame.display.set_caption('Spieloberfläche')
    
        #Show Elemente
       
        
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame.time: 
                count += 1
                

            #Buttons Funktionen
            if event.type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == quit_button:
                    print('Quit!')
                    #is_running = False
                    #pygame.quit()

                if event.ui_element == user_button:
                    if dd_menu.visible == 0:
                        dd_menu.visible = 1
                        quit_button.show()
                        restart_button.show()
                        menu_button.show()
                        user_lbl.show()
                        username_lbl.show()
                    else:
                        dd_menu.visible = 0
                        quit_button.hide()
                        restart_button.hide()
                        menu_button.hide()
                        user_lbl.hide()
                        username_lbl.hide()
                
                if event.ui_element == menu_button:
                    main_menu()
                    is_running2 = False
                    
                    
                if event.ui_element == rules_button:
                    print('rules_clicked')
                    if gameid == 1:
                        open_popup(game1_rule , "Game1 Regeln", 400, 400)

                    elif gameid == 2:
                        open_popup(game2_rule , "Game2 Regeln", 400, 400)

                    elif gameid == 3:
                        open_popup(game3_rule , "Game3 Regeln", 400, 400)
                    

            manager.process_events(event)
            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.update()
    pygame.quit()
#-----------------[/GameFrame Screen]---------------------------------------------------
#--------------------------------Main-------------------------------------

db_manager = DbManager()
main_menu()
#gameframe()

