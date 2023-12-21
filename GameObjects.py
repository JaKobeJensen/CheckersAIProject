from pygame import Surface, image, mouse
from pygame.font import Font 
import math

class Object:
    def __init__(self, name:str="", xPosition:int=0, yPosition:int=0, velocity:float=0.0, vector:tuple[float,float]=(0.0,0.0),
                 visible:bool=True)->None:
        self.objectName = name
        self.x:int = xPosition
        self.y:int = yPosition
        self.vector:tuple[float,float] = vector
        self.velocity:float = velocity
        self.movingToNewPosition:bool = False
        self.visible:bool = visible
        self._exactX:float = float(xPosition)
        self._exactY:float = float(yPosition)
        self._newPosition:tuple[int,int] = (0,0)
        return

    def change_position(self, newXPosition:int, newYPosition:int)->None:
        self.x = newXPosition
        self.y = newYPosition
        self._exactX = float(newXPosition)
        self._exactY = float(newYPosition)
        return

    def change_velocity(self, newVelocity:float)->None:
        self.velocity = newVelocity
        return
    
    def change_vector(self, newVector:tuple[float,float])->None:
        self.vector = newVector
        return

    def head_to_new_position(self, newPosition:tuple[int,int], velocity:float=1.0)->None:
        diffVector = (self.x - newPosition[0], self.y - newPosition[1])
        magnitude =  math.sqrt((diffVector[0]*diffVector[0]) + (diffVector[1]*diffVector[1]))
        normalizeVector = ((diffVector[0] / magnitude), (diffVector[1] / magnitude))
        self.change_vector((normalizeVector[0] * velocity, normalizeVector[1] * velocity))
        self._newPosition = newPosition
        self.movingToNewPosition = True
        return

    def move(self)->None:
        self._exactX += self.vector[0]
        self._exactY += self.vector[1]
        self.x = round(self._exactX)
        self.y = round(self._exactY)
        if self.movingToNewPosition and self._newPosition[0] == self.x and self._newPosition[1] == self.y:
            self.velocity = 0.0
            self.vector = (0.0, 0.0)
            self.movingToNewPosition = False
        return          

class PictureBoxObject(Object):
    def __init__(self, img:Surface=None, imgPath:str=None, name:str="", xPosition:int=0, yPosition:int=0,
                 velocity:float=0.0, vector:tuple[float,float]=(0.0,0.0), visible:bool=True)->None:
        super().__init__(name, xPosition, yPosition, velocity, vector, visible)
        if imgPath != None:
            self.image:Surface = image.load(imgPath)
        else:
            self.image:Surface = img
        self.width:int = self.image.get_width()
        self.height:int = self.image.get_height()
        return

    def change_image(self, newImg:Surface=None, newImgPath:str=None)->None:
        if newImgPath != None:
            self.image = image.load(newImgPath)
        else:
            self.image = newImg
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        return
    
    def mouse_hover(self)->bool:
        mousePosition = mouse.get_pos()
        if mousePosition[0] > self.x and mousePosition[0] < self.x + self.width and \
           mousePosition[1] > self.y and mousePosition[1] < self.y + self.height:
            return True
        return False

class TextObject(Object):
    def __init__(self, text:str="", font:Font=None, fontColor:tuple[int,int,int]=(255,255,255), backgroundColor:tuple[int,int,int]=None,
                 name:str="", xPosition:int=0, yPosition:int=0, velocity:float=0.0, vector:tuple[float,float]=(0.0,0.0),
                 visible:bool=True)->None:
        super().__init__(name, xPosition, yPosition, velocity, vector, visible)
        self.text:str = text
        self.font:Font = font
        self.fontColor:tuple[int,int,int] = fontColor
        self.textSurface:Surface = font.render(self.text, 1, self.fontColor)
        self.backgroundColor = backgroundColor
        self.width = self.textSurface.get_width()
        self.height = self.textSurface.get_height()
        return

    def change_text(self, newText:str)->None:
        self.text = newText
        self.textSurface = self.font.render(self.text, 1, self.fontColor)
        return
    
    def change_font(self, newFont:Font)->None:
        self.font = newFont
        self.textSurface = self.font.render(self.text, 1, self.fontColor)
        return
    
    def change_font_color(self, newFontColor:tuple[int,int,int])->None:
        self.fontColor = newFontColor
        self.textSurface = self.font.render(self.text, 1, self.fontColor)
        return
    
    def change_background_color(self, newBackgroundColor:tuple[int,int,int])->None:
        self.backgroundColor = newBackgroundColor
        return
    
    def mouse_hover(self)->bool:
        mousePosition = mouse.get_pos()
        if mousePosition[0] > self.x and mousePosition[0] < self.x + self.width and \
           mousePosition[1] > self.y and mousePosition[1] < self.y + self.height:
            return True
        return False
