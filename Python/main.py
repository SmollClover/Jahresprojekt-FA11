from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import pygame_gui
from game.tictactoe import TicTacToe
from game.bauernschach import Bauernschach
from game.game import Game
from user import User
from dbManager import DbManager


#--------[Meta]------------------------------------------
pygame.init()
#Auflösung
res = (680, 420)
screen = pygame.display.set_mode(res)
#Game Fenster
background = pygame.Surface(res)
manager = pygame_gui.UIManager(res)#, 'Themes/base.json')
clock = pygame.time.Clock()
#----------[/Meta]----------------------------------------
#----------[Funktionen]---------------------------------
def sort_scores_wins_asc(item):
    return item[3]


#Popup Windows
def open_popup(text,title,width,height):
    popup_window = pygame_gui.windows.ui_message_window.UIMessageWindow(rect=pygame.Rect((res[0]/2-200,10),(width,height)),html_message=text,manager=manager,window_title=title)

#Login
def login(username, password):
    result = db_manager.login(username, password) #result = False | User
    if result:
        User.setCurrUser(result)
        popupText = "Hallo " + result.getName() + "! Du hast dich erfolgreich eingeloggt."
        open_popup(popupText, "Login", 250, 170)
        return result.getName()
    return False

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
def set_pers_highscoretext(difficulty, user, gameid, difficultyId):
    if user:
        winloss = db_manager.getWinLossFromUser(user, gameid, difficultyId)
        if len(winloss) == 0:
            win = 0
            loss = 0
        else:
            win = winloss[0][0]
            loss = winloss[0][1]
        return "<font size=5>"+t+t+"<b>"+difficulty+"</b></font><br>Eingeloggt als:"+t+str(user.getName())+"<br><b>------------------------------</b><br>Siege: "+t+t+t+t+str(win)+"<br><br>Niederlagen:   "+t+t+str(loss)
    else:
        return "<font size=5>"+t+t+"<b>"+difficulty+"</b></font><br>Du bist nicht angemeldet.<br><b>------------------------------</b><br>Registriere dich, oder melde dich an um Statistiken speichern zu können.<br><br>"


def set_publ_highscoretext(difficulty):
    return "<font size=5>"+t+t+"<b>"+difficulty+"</b></font><br>Spieler"+t+"Siege"+t+"Niederl.<br><b>----------------------------</b>"

def fill_publ_highscores(user,wins,loses):
    spacer = 13-len(user)
    if spacer > 0:
        user += "&nbsp"*spacer
    return  "<br>"+user+str(wins)+t+t+str(loses)+"<br>"  

def loadScores(difficulty, title, pers, publ, button):
    gameid = db_manager.getGameIdFromName(title.text.split(" ")[0])
    pers.set_text(set_pers_highscoretext(button.text, User.getCurrUser(), gameid, difficulty))
    publ.set_text(set_publ_highscoretext(button.text))
    best_player = db_manager.getBestPlayer(gameid, difficulty)
    best_player.sort(key=sort_scores_wins_asc)
    for scoreValue in best_player:
        user = db_manager.getUserFromId(scoreValue[0])
        publ.set_text(publ.html_text + fill_publ_highscores(user.getName(),scoreValue[3],scoreValue[4])) 



#-----------[/Funktionen]----------------------------------
#-----------[Langtexte]---------------------------------
game1_rule = "Bauernschach ist eine simple Variante des Schachs, die nur mit Bauern gespielt wird. In der Ausgansstellung stehen dabei die weißen bzw. schwarze Spielfiguren (Bauern) auf der jeweiligen Grundlinie. Die Spieler machen abwechselnd einen Zug, wobei Weiß beginnt. Es gibt zwei erlaubte Sorten von Zügen: Ziehen oder Schlagen. Ziehen kann ein Bauer, indem er ein Feld in Richtung der gegnerischen Grundlinie (das sind die Felder, auf denen anfangs die gegnerischen Bauern stehen) geht, aber nur sofern dieses Feld frei ist (also nicht von einem eigenen oder gegnerischen Bauern besetzt ist). Schlagen kann ein Bauer in Richtung der gegnerischen Grundlinie durch diagonales Ziehen in Richtung der gegnerischen Grundlinie, aber nur auf ein Feld, auf dem ein gegnerischer Bauer steht. Ziel des Spieles ist es, einen Bauern auf die generische Grundlinie zu platzieren; wenn das gelingt, ist das Spiel sofort zu Ende und die Farbe, die das erreicht hat, hat gewonnen. Wenn ein Spieler nicht mehr ziehen kann, oder überhaupt keine Figuren mehr hat, ist das Spiel für ihn als verloren. Ein unentschieden ist nicht möglich."
game2_rule = "Bei der Dame werden zu Beginn für beide Spieler die Spielsteine auf den schwarzen Feldern der ersten zwei Reihen des Spielfeldes verteilt. Gespielt wird nur auf den dunklen Feldern. Die Steine ziehen jeweils ein Feld vorwärts in diagonaler Richtung. Es herrscht generell Schlagzwang, gegnerische Steine müssen entsprechend übersprungen und dadurch geschlagen werden, sofern das direkt angrenzende dahinter liegende Feld frei ist. Der schlagende Stein wird auf dieses freie Feld gezogen und wenn das Zielfeld eines Sprungs auf ein Feld führt, von dem aus ein weiterer Stein übersprungen werden kann, wird der Sprung fortgesetzt. Alle übersprungenen Steine werden nach dem Zug vom Brett genommen. Es darf dabei nicht über eigene Spielsteine gesprungen werden. Das Spiel ist gewonnen, wenn ein Spieler einen Spielstein auf der gegnerischen Grundlinie platzieren kann. Wenn ein Spieler nicht mehr ziehen kann, oder keine Spielsteine mehr hat, ist das Spiel für ihn verloren. Ein unentschieden ist nicht möglich."
game3_rule = "Beide Spieler setzen abwechselnd ihre Spielsteine auf ein freies Feld. Der Spieler, der als Erster vier seiner Spielsteine in eine Zeile, Spalte oder Diagonale setzen kann, gewinnt. Das Spiel ist unentschieden, wenn alle Felder belegt sind, ohne dass ein Spieler die erforderlichen Spielsteine in einer Reihe, Spalte oder Diagonalen setzen konnte."
#-----------[/Langtexte]--------------------------------
#--------------------[Main Menu-Screen]-----------------------------------

def main_menu():

    manager.clear_and_reset()
    pygame.init()
    pygame.display.set_caption('Spielekollektion')

    #Hintergrundfarbe
    background.fill(pygame.Color("#3c3c3c"))

    #--------------------Elemente------------------------
    #Label
    font = pygame.font.SysFont(None, 72)
    text = font.render("Spielekollektion", True, (255, 255, 255))
    background.blit(text, (res[0] / 2 - text.get_width() / 2, 20))

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
    user = User.getCurrUser()
    if user:
        users_name =  user.getName()
    else:
        users_name = "Gast"
    user_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (70, 50)), text=users_name, manager=manager, starting_height=21)
    dd_menu = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (200, 205)),starting_layer_height=20, manager=manager, visible=0)
    signin_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 100), (190, 50)), text="Anmelden", manager=manager, visible=0, starting_height=21)
    signup_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 150), (190, 50)), text="Registrieren", manager=manager, visible=0, starting_height=21)
    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 200), (190, 50)), text="Quit", manager=manager, visible=0, starting_height=21)
    ##---------------------------

    ##Anmelden & Registrieren ----
    loginWindow = 0  # 0 = both closed | 1 = login opened | 2 = registration opened
    user_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (190, 30)), text="Angemeldet als:", manager=manager, visible=0,container=dd_menu)
    username_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 20), (190, 30)), text=users_name, manager=manager, visible=0, container=dd_menu)
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
                                             text='Regeln', manager=manager,starting_height=1)
    game1_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, button_vert_startposition), (small_button_width, button_height)),
                                             text='Scores', manager=manager,starting_height=1)


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
                                             text='Regeln', manager=manager,starting_height=1)
    game2_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, (button_vert_startposition + button_height + button_vert_gap)), (small_button_width, button_height)),
                                             text='Scores', manager=manager,starting_height=1)
    
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
                                             text='Regeln', manager=manager,starting_height=1) 
    game3_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((scorebutton_offset, (button_vert_startposition + (2*button_height) + (2*button_vert_gap))), (small_button_width, button_height)),
                                             text='Scores', manager=manager,starting_height=1)
    
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
                    loadScores(1,hs_title_lbl, data_pers_highscore_txt, data_publ_highscore_txt, hs_data_l_button)
                if event.ui_element == hs_data_m_button:
                    loadScores(2,hs_title_lbl, data_pers_highscore_txt, data_publ_highscore_txt, hs_data_m_button)

                if event.ui_element == hs_data_s_button:
                    loadScores(3,hs_title_lbl, data_pers_highscore_txt, data_publ_highscore_txt, hs_data_s_button)

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
                                user_button.set_text(result)
                            else:
                                popupText = "Das Benutzername oder Passwort ist falsch."
                                open_popup(popupText, "Login", 250, 170)
                        elif loginWindow == 2: # registration is active
                            register(username, password)
                        
                #Game1
                if event.ui_element == game1_button:
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
                    open_popup(game1_rule, gamesList[0][1]+" Regeln", 400, 400)
                    
                if event.ui_element == game1_score_button:
                    hs_title_lbl.set_text(game1_button.text + " Highscores")
                    highscore_panel.show()    
                    loadScores(1,hs_title_lbl, data_pers_highscore_txt, data_publ_highscore_txt, hs_data_l_button)

                if event.ui_element == game1_buttonl:
                    game_state = (game1_button.text,1,1)
                    
                
                if event.ui_element == game1_buttonm:
                    game_state = (game1_button.text,1,2)

                if event.ui_element == game1_buttons:
                    game_state = (game1_button.text,1,3)

                #Game2
                if event.ui_element == game2_button:
                    popupText = "Das DLC 'Dame' wurde nicht erworben!"
                    open_popup(popupText, "Dame", 250, 170)

                    # game2_button.hide()
                    # game1_button.show()
                    # game3_button.show()
                    
                    # game2_buttonl.show()
                    # game2_buttonm.show()
                    # game2_buttons.show()
                    
                    # game1_buttonl.hide()
                    # game1_buttonm.hide()
                    # game1_buttons.hide()
                    
                    # game3_buttonl.hide()
                    # game3_buttonm.hide()
                    # game3_buttons.hide()
                    
                    # dd_menu.visible = 0
                    # quit_button.hide()
                    # signin_button.hide()
                    # signup_button.hide()
                    # user_lbl.hide()
                    # username_lbl.hide()
                    # id_lbl.hide()
                    # pw_lbl.hide()
                    # id_txtentry.hide()
                    # pw_txtentry.hide()
                    # ok_button.hide()
                    # dd_menu.set_dimensions((200, 205))
                    # signup_button.set_position((5,150))
                    # quit_button.set_position((5,200))
                    
                if event.ui_element == game2_rules_button:
                    open_popup(game2_rule , gamesList[1][1]+" Regeln", 400, 400)

                if event.ui_element == game2_score_button:
                    hs_title_lbl.set_text(game2_button.text + " Highscores")
                    highscore_panel.show()
                    loadScores(1,hs_title_lbl, data_pers_highscore_txt, data_publ_highscore_txt, hs_data_l_button)

                # if event.ui_element == game2_buttonl:
                #     game_state = (game2_button.text,2,1)
                
                # if event.ui_element == game2_buttonm:
                #     game_state = (game2_button.text,2,2)

                # if event.ui_element == game2_buttons:
                #     game_state = (game2_button.text,2,3)

                 #Game3
                if event.ui_element == game3_button:
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
                    open_popup(game3_rule , gamesList[2][1]+" Regeln", 400, 400)
                    
                if event.ui_element == game3_score_button:
                    hs_title_lbl.set_text(game3_button.text + " Highscores")
                    highscore_panel.show()
                    loadScores(1,hs_title_lbl, data_pers_highscore_txt, data_publ_highscore_txt, hs_data_l_button)
                    
                if event.ui_element == game3_buttonl:
                    game_state = (game3_button.text,3,1)
                
                if event.ui_element == game3_buttonm:
                    game_state = (game3_button.text,3,2)

                if event.ui_element == game3_buttons:
                    game_state = (game3_button.text,3,3)
                    
                if event.ui_element == quit_button:
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

def gameframe(gamename, gameid, difficulty):
    difficulty = str(difficulty)
    time = ""
    temp = "None"
    manager.clear_and_reset()
    #Hintergrundfarbe
    background.fill(pygame.Color("#3c3c3c"))
    
    #--------------------Elemente---------------------
    #User Menu
    user = User.getCurrUser()
    if user:
        users_name =  user.getName()
    else:
        users_name = "Gast"
    user_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (70, 50)), text=users_name, manager=manager)
    dd_menu = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (200, 155)), starting_layer_height=9, manager=manager, visible=0)
    restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 100), (190, 50)), text="Neustart", manager=manager, visible=0, starting_height=10)
    menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 150), (190, 50)), text="Hauptmenü", manager=manager, visible=0, starting_height=10)
    user_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (200, 30)), text="Angemeldet als:", manager=manager, visible=0, container=dd_menu)
    username_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 20), (200, 30)), text=users_name, manager=manager, visible=0, container=dd_menu)

    #Label
    if difficulty == "1": difficulty_as_str = "Leicht"
    if difficulty == "2": difficulty_as_str = "Mittel"
    if difficulty == "3": difficulty_as_str = "Schwer"
    difficulty_head_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20,res[1]/2-50), ((res[0]-res[1])/2,50)), text="Schwierigkeit:", manager=manager)
    difficulty_lbl = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20,res[1]/2-25), ((res[0]-res[1])/2,50)), text=difficulty_as_str, manager=manager)
    
    bauernschach_formation = " "+t+t
    dame_formation = " "+t+t+t
    tictactoe_formation = "  "+t+t
    if gameid == 1: formation = bauernschach_formation
    if gameid == 2: formation = dame_formation
    if gameid == 3: formation = tictactoe_formation

    title_lbl = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((res[0]*0.25,0), ((res[1]-80),40)), html_text="<font size=5>"+formation+"<b><i>"+gamename+"</i></b>", manager=manager)
    message_lbl = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((res[0]*0.25,res[1]-40), ((res[1]-80),40)), html_text="", manager=manager)


    #Buttons
    rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,res[1]-40), (40, 40)),
                                             text='?', manager=manager,starting_height=-2)

    #Debug Output
    debug_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]-40,res[1]-40), (40, 40)),
                                             text='...', manager=manager,starting_height=-2)
    debug_panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((res[0]*0.75,0), (res[0]*0.25, res[1]-40)),starting_layer_height=0, manager=manager,visible=0)
    debug_output_txt = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((-3,-3), ((res[0]*0.25), res[1]-40)),html_text="<font size=1>Debug", manager=manager,container=debug_panel)


    #---------------------------------------------------
    is_running = True
    back_to_main_menu = False
    restart = False
    is_game_over = False

    if gameid == 1:
        game = Game(db_manager, background, 6, 6, Bauernschach(6, 6), difficulty)
    elif gameid == 2:

        back_to_main_menu = True
        # game = Game(background, 6, 6, Dame(4, 6, 6), difficulty)
    elif gameid == 3:
        game = Game(db_manager, background, 6, 6, TicTacToe(4, 6, 6), difficulty)

    while is_running and not back_to_main_menu and not restart:
       
        #Fenster Titel
        pygame.display.set_caption('Spieloberfläche')
    
        #Show Elemente 
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame.time: 
                count += 1


            if event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0]<(res[0]*0.75):
                if game.getDebugInfo() == temp:
                    temp = game.getDebugInfo()
                    debug_output_txt.set_text(debug_output_txt.html_text)
                else:
                    temp = game.getDebugInfo()
                    debug_output_txt.set_text(debug_output_txt.html_text +"<br>"+str(clock.get_time)+"<br>" + str(game.getDebugInfo()))

            #Buttons Funktionen
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == debug_button:
                    if debug_panel.visible == 0:
                        debug_panel.show()
                    else:
                        debug_panel.hide()

                if event.ui_element == user_button:
                    if dd_menu.visible == 0:
                        dd_menu.visible = 1
                        restart_button.show()
                        menu_button.show()
                        user_lbl.show()
                        username_lbl.show()
                    else:
                        dd_menu.visible = 0
                        restart_button.hide()
                        menu_button.hide()
                        user_lbl.hide()
                        username_lbl.hide()
                elif event.ui_element == menu_button:
                    back_to_main_menu = True    
                elif event.ui_element == rules_button:
                    if gameid == 1:
                        open_popup(game1_rule , gamename +" Regeln", 400, 400)
                    elif gameid == 2:
                        open_popup(game2_rule , gamename +" Regeln", 400, 400)
                    elif gameid == 3:
                        open_popup(game3_rule , gamename +" Regeln", 400, 400)
                elif event.ui_element == restart_button:
                    restart = True

            if not is_game_over:
                game_result = game.tick(event)
                if game_result[0] == 0: # still playing
                    if game_result[1] == -1: # ai is moving
                        message_lbl.set_text("Zug wird berechnet.")
                    else: # player is moving
                        message_lbl.set_text("Du bist dran.")
                else: # game is over
                    is_game_over = True
                    if game_result[1] == game.gameStateEnum["PLAYER"]:
                        message_lbl.set_text("Du hast gewonnen!")
                        user = User.getCurrUser()
                        if user:
                            db_manager.updateScore(user.getId(), gameid, difficulty, True)
                    if game_result[1] == game.gameStateEnum["KI"]:
                        message_lbl.set_text("Du hast verloren.")
                        user = User.getCurrUser()
                        if user:
                            db_manager.updateScore(user.getId(), gameid, difficulty, False)
                    if game_result[1] == game.gameStateEnum["DRAW"]:
                        message_lbl.set_text("Unentschieden.")
            
            
            
            
            manager.process_events(event)
            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.update()
    if back_to_main_menu:
        main_menu()
    elif restart:
        gameframe(gamename, gameid, difficulty)
    else:
        pygame.quit()
#-----------------[/GameFrame Screen]---------------------------------------------------
#--------------------------------Main-------------------------------------

db_manager = DbManager()
gamesList = db_manager.getGames()
main_menu()
