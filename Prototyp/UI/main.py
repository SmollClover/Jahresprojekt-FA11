import pygame
import pygame_gui




#--------[Meta]------------------------------------------
pygame.init()
#Auflösung
res = (680, 420)
screen = pygame.display.set_mode(res)
#Game Fenster
background = pygame.Surface(res)
manager = pygame_gui.UIManager(res, 'Themes/base.json')
manager.get_theme().load_theme('Themes/label.json')
manager.get_theme().load_theme('Themes/button.json')
clock = pygame.time.Clock()
#----------[/Meta]----------------------------------------
#----------[Funktionen]---------------------------------

#-----------[/Funktionen]----------------------------------

#--------------------[Main Menu-Screen]-----------------------------------
def main_menu():
   
    
    
    #Hintergrundfarbe
    background.fill(pygame.Color('#9c9c9c'))
    
    #--------------------Elemente------------------------
    #Label
    menu_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((res[0]/2-50, 20), (100, 50)), text="Main Menu", manager=manager)
    
    #Buttons
    
    
    user_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (50, 50)),
                                             text='Test', manager=manager)
    
    gamebutton_offset = -125
    rulesbutton_offset = 125
    scorebutton_offset = 175
    #Game1 Buttons
    game1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+gamebutton_offset, 100), (250, 50)),
                                             text='Game1', manager=manager)
    
    game1_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+rulesbutton_offset, 100), (50, 50)),
                                             text='Game1_rules', manager=manager)
    
    game1_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+scorebutton_offset, 100), (50, 50)),
                                             text='Game1_score', manager=manager)

    #Game2 Buttons
    game2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+gamebutton_offset, 175), (250, 50)),
                                             text='Game2', manager=manager)
    
    game2_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+rulesbutton_offset, 175), (50, 50)),
                                             text='Game2_rules', manager=manager)
    
    game2_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+scorebutton_offset, 175), (50, 50)),
                                             text='Game2_score', manager=manager)
    #Game3 Buttons
    
    game3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+gamebutton_offset, 250), (250, 50)),
                                             text='Game3', manager=manager)
    
    game3_rules_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+rulesbutton_offset, 250), (50, 50)),
                                             text='Game3_rules', manager=manager)
    
    game3_score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2+scorebutton_offset, 250), (50, 50)),
                                             text='Game3_score', manager=manager)
    

    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2-200, 325), (250, 50)),
                                               text="Quit", manager=manager)
    
    #-----------------------------------------------------
    is_running = True
    while is_running:
        
        #Fenster Titel
        pygame.display.set_caption('Main Menu')
        
        #Show Elemente
        menu_text.show()
        quit_button.show()
        
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            #Buttons Funktionen
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                #Game1
                if event.ui_element == game1_button:
                    print('Game1_clicked')
                    
                if event.ui_element == game1_rules_button:
                    print('Game1_rules_clicked')
                    
                if event.ui_element == game1_score_button:
                    print('Game1_score_clicked')
                    
                 #Game2
                if event.ui_element == game2_button:
                    print('Game2_clicked')
                    
                if event.ui_element == game2_rules_button:
                    print('Game2_rules_clicked')
                    
                if event.ui_element == game2_score_button:
                    print('Game2_score_clicked')
                      
                 #Game3
                if event.ui_element == game3_button:
                    print('Game3_clicked')
                    
                if event.ui_element == game3_rules_button:
                    print('Game3_rules_clicked')
                    
                if event.ui_element == game3_score_button:
                    print('Game3_score_clicked')
    
                    
                    #Hide Elemente
                    
                if event.ui_element == quit_button:
                    print('Quit!')
                    is_running = False
               
            manager.process_events(event)
            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.update()
    pygame.quit()
#-----------------[/Main Menu-Screen]-----------------------------------------------------    
#-----------------[Settings-Screen]-----------------------------------------
def settings():
    

    #Hintergrundfarbe
    background.fill(pygame.Color('#9c9c9c'))
    
    #--------------------Elemente---------------------
    #Label
    settings_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20, 20), (100, 50)), text="Settings", manager=manager)

    #Buttons
    resolution_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2-100, 115), (200, 50)),
                                             text='Resolution', manager=manager)

    theme_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2-100, 175), (200, 50)),
                                               text="Theme", manager=manager)

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((res[0]/2-100, 235), (200, 50)),
                                               text="Back", manager=manager)
    
    #---------------------------------------------------
    is_running = True
    while is_running:
        
        #Fenster Titel
        pygame.display.set_caption('Settings')
    
        #Show Elemente
        settings_text.show()
        resolution_button.show()
        theme_button.show()
        back_button.show()
        
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            #Buttons Funktionen
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == resolution_button:
                    print('Resolution!')
                      
                if event.ui_element == theme_button:
                    print('Theme!')
                    
                if event.ui_element == back_button:
                    print('Back!')
                    
                    #Hide Elemente
                    settings_text.hide()
                    resolution_button.hide()
                    theme_button.hide()
                    back_button.hide()
                    
                    is_running = False
               
            manager.process_events(event)
            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.update()

#---------------------[/Settings-Screen]----------------------------------
#--------------------------------Main-------------------------------------
main_menu()
    
