from pygame import Surface, draw, Rect, font
from GameObjects import *
font.init()

class Screen:
    _DEFAULT_SCREEN_SIZE:tuple[int,int] = (600,600)
    _ASPECT_RATIO:float = _DEFAULT_SCREEN_SIZE[0] / _DEFAULT_SCREEN_SIZE[1]

    def __init__(self, xPosition:int=0, yPosition:int=0, screenScalingFactor:float=1.0, backgroundColor:tuple[int,int,int]=None)->None:
        self._width:int = round(self._DEFAULT_SCREEN_SIZE[0] * screenScalingFactor)
        self._height:int = round(self._DEFAULT_SCREEN_SIZE[1] * screenScalingFactor)
        self._scalingFactor = screenScalingFactor
        self.screen:Surface = Surface((self._width, self._height))
        self.gameObjects:dict[str,Object] = {}
        self.x:int = xPosition
        self.y:int = yPosition
        self.backgroundColor:tuple[int,int,int] = backgroundColor
        if self.backgroundColor:
            self.screen.fill(self.backgroundColor)
        return

    def get_size(self)->tuple[int,int]:
        return (self._width, self._height)

    def get_width(self)->int:
        return self._width
    
    def get_height(self)->int:
        return self._height
    
    def get_scaling_factor(self)->float:
        return self._scalingFactor

    def change_position(self, newXPosistion:int, newYPosistion:int)->None:
        self.x = newXPosistion
        self.y = newYPosistion
        return

    def change_scaling_factor(self, screenScalingFactor:float)->None:
        self._width = round(self._DEFAULT_SCREEN_SIZE[0] * screenScalingFactor)
        self._height = round(self._DEFAULT_SCREEN_SIZE[1] * screenScalingFactor)
        self.screen:Surface = Surface((self._width, self._height))
        return
    
    def change_background_color(self, newBackgroundColor:tuple[int,int])->None:
        self.backgroundColor = newBackgroundColor
        self.screen.fill(self.backgroundColor)
        return
    
    def add_game_object(self, gameObjectName:str, gameObject:Object)->None:
        self.gameObjects[gameObjectName] = gameObject
        return

    def render_game_objects(self)->None:
        for _, gameObject in self.gameObjects.items():
            gameObject.render(self.screen)
        return

class MainMenuScreen(Screen):
    def __init__(self, xPosition:int=0, yPosition:int=0, screenScalingFactor:float=1.0)->None:
        super().__init__(xPosition, yPosition, screenScalingFactor, backgroundColor=(255,255,255))
        
        titleText:TextObject = TextObject(name="titleTxt", text="Connect 4",
                                             font=font.SysFont("Arial Nova", 72), fontColor=(0,0,0))
        titleText.change_position(newXPosition=round((self._width/2) - (titleText.width/2)),
                                  newYPosition=round(self._height*0.05))

        playerVSPlayerButton:TextObject = TextObject(name="pvpBtn", border=True, text="Player VS Player",
                                                     font=font.SysFont("Arial Nova", 24), fontColor=(0,0,0),
                                                     backgroundColor=(211, 211, 211))
        playerVSPlayerButton.change_position(newXPosition=round((self._width/2) - (playerVSPlayerButton.width/2)),
                                             newYPosition=round(self._height*0.25))

        self.add_game_object(titleText.name, titleText)
        self.add_game_object(playerVSPlayerButton.name, playerVSPlayerButton)
        return