from pygame import display
from Screens import *

if __name__ == '__main__':
    window = display.set_mode((600,600))
    mainMenu = MainMenuScreen(screenSize=(window.get_width(),window.get_height()))
    mainMenu.render_game_objects()
    window.blit(mainMenu.screen, (mainMenu.x,mainMenu.y))
    display.update()
    quit()