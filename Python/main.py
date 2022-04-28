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
#Popup Windows
def open_popup(text,title,width,height):
    popup_window = pygame_gui.windows.ui_message_window.UIMessageWindow(rect=pygame.Rect((res[0]/2-200,10),(width,height)),html_message=text,manager=manager,window_title=title)

#Login
def login(username, password):
    result = db_manager.login(username, password) #result = False | User
    if result:
        popupText = "Hallo " + result.getName() + "! Du hast dich erfolgreich eingeloggt."
        open_popup(popupText, "Login", 250, 170)
        return result.getName()

#Register
def register(username, password):
    successful = db_manager.register(username, password)                    
    if successful:
        open_popup("Du hast dich erfolgreich registriert!", "Registrierung", 250, 170)
    else:
        open_popup("Der Benutzername ist bereits vergeben.", "Registrierung", 250, 170)

# def open_confirm(text,title,width,height):
#     confirm_window = pygame_gui.windows.ui_message_window.UIConfirmationDialog(rect=pygame.Rect((res[0]/2-200,10),(width,height)),html_message=text,manager=manager,window_title=title)
t = "&nbsp;&nbsp;&nbsp;&nbsp;"
def set_pers_highscoretext(difficulty,highscore,wins,loses,ties):
    return "<font size=5>"+t+t+"<b>"+difficulty+"</b></font><br>Höchste Punktezahl:"+t+str(highscore)+"<br><b>------------------------------</b><br>Siege: "+t+t+t+t+str(wins)+"<br><br>Niederlagen:   "+t+t+str(loses)+"<br><br>Unentschieden: "+t+t+str(ties)


def set_publ_highscoretext(difficulty):
    return "<font size=5>"+t+t+"<b>"+difficulty+"</b></font><br>Spieler"+t+"Siege"+t+"Niederl.<br><b>----------------------------</b>"

def fill_publ_highscores(user,wins,loses):
    return  "<br>"+user+t+str(wins)+t+t+str(loses)+"<br>"  


#-----------[/Funktionen]----------------------------------
#-----------[Langtexte]---------------------------------
game1_rule = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
game2_rule = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
game3_rule = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

#pers_highscore_data = "<font size=5><b>"+difficulty+"</b></font><br>Siege: <br><br>Niederlagen:  <br><br>Unentschieden: "
#publ_highscore_data = "<font size=5><b>Leicht</b></font><br>Siege: <br><br>Niederlagen:  <br><br>Unentschieden: "
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
   
    ##Highscore Screen---------------------
    #Panel
    highscore_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(((res[0]/2)-((res[1]*1.25)/2),0), (res[1]*1.25, res[1])),starting_layer_height=3, manager=manager,visible=0)
    hs_head_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (res[1]*1.25-6, 40)),starting_layer_height=3, manager=manager,container=highscore_panel)
    publ_highscore_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0,70), ((res[1]*1.25)/2, res[1]-76)),starting_layer_height=3, manager=manager,container=highscore_panel)
    data_publ_highscore_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((-3,30), ((res[1]*1.25)/2, res[1]-109)),starting_layer_height=3, manager=manager,container=publ_highscore_panel)
    pers_highscore_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(((res[0]/2)-((res[1]*0.2)-1),70), ((res[1]*1.25)/2, res[1]-76)),starting_layer_height=3, manager=manager,container=highscore_panel)
    data_pers_highscore_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((-3,30), ((res[1]*1.25)/2, res[1]-109)),starting_layer_height=4, manager=manager,container=pers_highscore_panel)
    close_hs_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[1]*1.25-46, 0), (40, 40)), text='X',starting_height = 4, manager=manager, container=highscore_panel)
   
    #Label
    hs_title_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (res[1]*1.25-6, 30)), text="Highscores", manager=manager, container=hs_head_panel)
    publ_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), ((res[1]*1.25)/2, 30)), text="Öffentliche Highscores", manager=manager, container=publ_highscore_panel)
    pers_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), ((res[1]*1.25)/2, 30)), text="Persönliche Statistik", manager=manager, container=pers_highscore_panel)
   
    #Buttons
    hs_data_l_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 35), ((res[1]*1.25/3)+1, 40)), text='Leicht',starting_height = 4, manager=manager, container=highscore_panel)
    hs_data_m_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((res[1]*1.25/3)-3, 35), ((res[1]*1.25/3)+1, 40)), text='Mittel',starting_height = 4, manager=manager, container=highscore_panel)
    hs_data_s_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((res[1]*1.25/3)*2-6, 35), ((res[1]*1.25/3), 40)), text='Schwer',starting_height = 4, manager=manager, container=highscore_panel)

    #Textboxen
    data_publ_highscore_txt = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((-3,-3), ((res[1]*1.25)/2, res[1]-109)),html_text="", manager=manager,container=data_publ_highscore_panel)
    data_pers_highscore_txt = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((-3,-3), ((res[1]*1.25)/2, res[1]-109)),html_text="", manager=manager,container=data_pers_highscore_panel)

    ##--------------------------------------

    ##User Menu -----------------
    user_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (70, 50)), text='User', manager=manager, starting_height=21)
    dd_menu = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (200, 205)),starting_layer_height=20, manager=manager, visible=0)
    signin_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 100), (190, 50)), text="Anmelden", manager=manager, visible=0, starting_height=21)
    signup_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 150), (190, 50)), text="Registrieren", manager=manager, visible=0, starting_height=21)
    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 200), (190, 50)), text="Quit", manager=manager, visible=0, starting_height=21)
    ##---------------------------

    ##Anmelden & Registrieren ----
    loginWindow = 0  # 0 = both closed | 1 = login opened | 2 = registration opened
    user_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (190, 30)), text="Angemeldet als:", manager=manager, visible=0,container=dd_menu)
    username_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 20), (190, 30)), text="Gast/Username", manager=manager, visible=0, container=dd_menu)
    id_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 70), (190, 30)), text="Benutzername:", manager=manager, visible=0, container=dd_menu)
    id_txtentry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((5, 150), (190, 30)), manager=manager, visible=0, container=dd_menu)
    pw_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 180), (190, 30)), text="Passwort:", manager=manager, visible=0, container=dd_menu)
    pw_txtentry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0, 210), (190, 30)), manager=manager, visible=0, container=dd_menu)
    ok_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 235), (95, 30)), text="Ok", manager=manager, visible=0, container=dd_menu)
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
   
    game_state = ("",0,0) # (Name, GameID, Difficulty) | IDs are equal to DB-IDs, while 0 is 'no game' | Difficulty: 0 -> Leicht, 1 -> Mittel, 2 -> Hard

    #Game1 Buttons
    game1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, button_vert_startposition), (big_button_width, button_height)),
                                             text=gamesList[0][1], manager=manager,starting_height=1)
    game1_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((rulesbutton_offset, button_vert_startposition), (small_button_width, button_height)),
                                             text='?', manager=manager,starting_height=1)
    game1_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, button_vert_startposition), (small_button_width, button_height)),
                                             text='Score', manager=manager,starting_height=1)


    #Game1 Difficulty Buttons
    game1_buttonl = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, button_vert_startposition), (big_button_width/3+4, button_height)),
                                             text='Leicht', manager=manager, visible=0, starting_height=2)
    game1_buttonm = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((gamebutton_offset+(big_button_width/3)), button_vert_startposition), (big_button_width/3+4, button_height)),
                                             text='Mittel', manager=manager, visible=0, starting_height=2)
    game1_buttons = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset+(big_button_width/3*2), button_vert_startposition), (big_button_width/3, button_height)),
                                             text='Schwer', manager=manager, visible=0, starting_height=2)    

    #Game2 Buttons
    game2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (big_button_width, button_height)),
                                             text=gamesList[1][1], manager=manager,starting_height=1)
    game2_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((rulesbutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (small_button_width, button_height)),
                                             text='?', manager=manager,starting_height=1)
    game2_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (small_button_width, button_height)),
                                             text='Score', manager=manager,starting_height=1)
    
    #Game2 Difficulty Buttons
    game2_buttonl = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (big_button_width/3+4, button_height)),
                                             text='Leicht', manager=manager, visible=0, starting_height=2)
    game2_buttonm = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((gamebutton_offset+(big_button_width/3)), (button_vert_startposition + button_height + button_vert_gap)), (big_button_width/3+4, button_height)),
                                             text='Mittel', manager=manager, visible=0, starting_height=2)
    game2_buttons = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset+(big_button_width/3*2), (button_vert_startposition + button_height + button_vert_gap)), (big_button_width/3, button_height)),
                                             text='Schwer', manager=manager, visible=0, starting_height=2)
    
    #Game3 Buttons
    
    game3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width, button_height)),
                                             text=gamesList[2][1], manager=manager,starting_height=1)  
    game3_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((rulesbutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (small_button_width, button_height)),
                                             text='?', manager=manager,starting_height=1) 
    game3_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (small_button_width, button_height)),
                                             text='Score', manager=manager,starting_height=1)
    
    #Game3 Difficulty Buttons
    game3_buttonl = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width/3+4, button_height)),
                                             text='Leicht', manager=manager, visible=0, starting_height=2)
    game3_buttonm = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((gamebutton_offset+(big_button_width/3)), (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width/3+4, button_height)),
                                             text='Mittel', manager=manager, visible=0, starting_height=2)
    game3_buttons = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gamebutton_offset+(big_button_width/3*2), (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (big_button_width/3, button_height)),
                                             text='Schwer', manager=manager, visible=0, starting_height=2)
    
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

                #Highscore screen
                if event.ui_element == close_hs_button:
                    highscore_panel.hide()

                if event.ui_element == hs_data_l_button:
                    data_pers_highscore_txt.set_text(set_pers_highscoretext(hs_data_l_button.text,9999,4,2,1))
                    #user scores mit schleife ausgeben
                    data_publ_highscore_txt.set_text(set_publ_highscoretext(hs_data_l_button.text))
                    data_publ_highscore_txt.set_text(data_publ_highscore_txt.html_text + fill_publ_highscores("Spieler2",95,0))
                    data_publ_highscore_txt.set_text(data_publ_highscore_txt.html_text + fill_publ_highscores("Spieler3",54,21))
                    data_publ_highscore_txt.set_text(data_publ_highscore_txt.html_text + fill_publ_highscores("Spieler4",32,5))
                    data_publ_highscore_txt.set_text(data_publ_highscore_txt.html_text + fill_publ_highscores("Spieler5",20,4))
                    data_publ_highscore_txt.set_text(data_publ_highscore_txt.html_text + fill_publ_highscores("Spieler6",16,34))
                    data_publ_highscore_txt.set_text(data_publ_highscore_txt.html_text + fill_publ_highscores("Spieler7",14,8))

                if event.ui_element == hs_data_m_button:
                    data_pers_highscore_txt.set_text(set_pers_highscoretext(hs_data_m_button.text,5000,3,3,3))
                    data_publ_highscore_txt.set_text(set_publ_highscoretext(hs_data_m_button.text))

                if event.ui_element == hs_data_s_button:
                    data_pers_highscore_txt.set_text(set_pers_highscoretext(hs_data_s_button.text,420,2,4,0))
                    data_publ_highscore_txt.set_text(set_publ_highscoretext(hs_data_s_button.text))

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
                    username = id_txtentry.get_text()
                    password = pw_txtentry.get_text()
                    if len(username) != 0 and len(password) != 0:
                        if loginWindow == 1: # login is active
                            result = login(username, password)
                            if result:
                                username_lbl.set_text(result)
                        elif loginWindow == 2: # registration is active
                            register(username, password)
                        
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
                    hs_title_lbl.set_text(game1_button.text + " Highscores")
                    highscore_panel.show()
                   

                if event.ui_element == game1_buttonl:
                    game_state = (game1_button.text,1,1)
                    
                
                if event.ui_element == game1_buttonm:
                    game_state = (game1_button.text,1,2)

                if event.ui_element == game1_buttons:
                    game_state = (game1_button.text,1,3)

                #Game2
                if event.ui_element == game2_button:
                    print('Game2_clicked')

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
                    hs_title_lbl.set_text(game2_button.text + " Highscores")
                    highscore_panel.show()

                if event.ui_element == game2_buttonl:
                    game_state = (game2_button.text,2,1)
                
                if event.ui_element == game2_buttonm:
                    game_state = (game2_button.text,2,2)

                if event.ui_element == game2_buttons:
                    game_state = (game2_button.text,2,3)

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
                    hs_title_lbl.set_text(game3_button.text + " Highscores")
                    highscore_panel.show()
                    
                if event.ui_element == game3_buttonl:
                    game_state = (game3_button.text,3,1)
                
                if event.ui_element == game3_buttonm:
                    game_state = (game3_button.text,3,2)

                if event.ui_element == game3_buttons:
                    game_state = (game3_button.text,3,3)
                    
                if event.ui_element == quit_button:
                    print('Quit!')
                    is_running = False
                    #pygame.quit()                    
                             
            manager.process_events(event)
            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.update()

            if game_state != ("",0,0):
                is_running = False

    if game_state == ("",0,0):
        pygame.quit()
        exit()
    else:
        gameframe(game_state[0], game_state[1], game_state[2])
#-----------------[/Main Menu-Screen]-----------------------------------------------------
#-----------------[GameFrame Screen]----------------------------------------------------

def gameframe(game, gameid, difficulty):
    difficulty = str(difficulty)
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
    back_to_main_menu = False
    while is_running and not back_to_main_menu:
       
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
                    back_to_main_menu = True
                    
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
    if back_to_main_menu:
        main_menu()
    else:
        pygame.quit()
#-----------------[/GameFrame Screen]---------------------------------------------------
#--------------------------------Main-------------------------------------

db_manager = DbManager()
gamesList = db_manager.getGames()
main_menu()
#gameframe()

