from pygame import display, Surface, draw, Rect
from GameObjects import *

class Screen:
    def __init__(self, screenSize:tuple[int,int]=(0,0), backgroundColor:tuple[int,int,int]=None)->None:
        self.screen:Surface = display.set_mode(screenSize)
        self.gameObjects:dict[str:Object] = {}
        self.backgroundColor:tuple[int,int,int] = backgroundColor
        draw.rect(self.screen, self.backgroundColor, Rect(0, 0, self.screen.get_width(), self.screen.get_height()))
        return
    
    def get_width(self)->int:
        return self.screen.get_width()
    
    def get_height(self)->int:
        return self.screen.get_height()
    
    def change_screen_size(self, newScreenSize:tuple[int,int])->None:
        self.screen:Surface = display.set_mode(newScreenSize)
        return
    
    def change_background_color(self, newBackgroundColor:tuple[int,int])->None:
        self.backgroundColor = newBackgroundColor
        self.screen.fill(self.backgroundColor)
        return
    
    def add_game_object(self, gameObjectName:str, gameObject:Object)->None:
        self.gameObjects[gameObjectName] = gameObject
        return

    def render_game_objects(self)->None:
        for gameObjectName, gameObject in self.gameObjects.items():
            self.screen.blit()
        return

class MainMenuScreen(Screen):
    def __init__(self, screenSize:tuple[int,int]=(0,0), backgroundColor:tuple[int,int,int]=None)->None:
        super().__init__(screenSize, backgroundColor)
        return