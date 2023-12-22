from pygame import Surface, draw, Rect, font
from GameObjects import *
font.init()

class Screen:
    def __init__(self, xPosition:int=0, yPosition:int=0, screenSize:tuple[int,int]=(0,0), backgroundColor:tuple[int,int,int]=None)->None:
        self.screen:Surface = Surface(screenSize)
        self.gameObjects:dict[str,Object] = {}
        self.x:int = xPosition
        self.y:int = yPosition
        self.backgroundColor:tuple[int,int,int] = backgroundColor
        if self.backgroundColor:
            self.screen.fill(self.backgroundColor)
        return

    def get_width(self)->int:
        return self.screen.get_width()
    
    def get_height(self)->int:
        return self.screen.get_height()
    
    def change_position(self, newXPosistion:int, newYPosistion:int)->None:
        self.x = newXPosistion
        self.y = newYPosistion
        return

    def change_screen_size(self, newScreenSize:tuple[int,int])->None:
        self.screen = Surface(newScreenSize)
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
            gameObject.render(self.screen)
        return

class MainMenuScreen(Screen):
    def __init__(self, xPosition:int=0, yPosition:int=0, screenSize:tuple[int,int]=(0,0))->None:
        backgroundColor = (255,255,255)
        super().__init__(xPosition, yPosition, screenSize, backgroundColor)
        
        titleText:TextObject = TextObject(name="titleTxt", text="Connect 4",
                                             font=font.SysFont("Arial Nova", 72), fontColor=(0,0,0))
        titleText.change_position(newXPosition=round((self.get_width()/2) - (titleText.width/2)),
                                  newYPosition=round(self.get_height()*0.05))

        playerVSPlayerButton:TextObject = TextObject(name="pvpBtn", border=True, text="Player VS Player",
                                                     font=font.SysFont("Arial Nova", 24), fontColor=(0,0,0),
                                                     backgroundColor=(211, 211, 211))
        playerVSPlayerButton.change_position(newXPosition=round((self.get_width()/2) - (playerVSPlayerButton.width/2)),
                                             newYPosition=round(self.get_height()*0.25))

        self.add_game_object(titleText.name, titleText)
        self.add_game_object(playerVSPlayerButton.name, playerVSPlayerButton)
        return