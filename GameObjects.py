from pygame import Surface, image, mouse, draw, Rect
from pygame.font import Font 
import math
from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, name:str, xPosition:int=0, yPosition:int=0, width:int=0, height:int=0, velocity:float=0.0,
                 vector:tuple[float,float]=(0.0,0.0), visible:bool=True, border:bool=False,
                 borderColor:tuple[int,int,int]=(0,0,0), borderWidth:int=1)->None:
        self.name = name
        self.x:int = xPosition
        self.y:int = yPosition
        self.width:int = width
        self.height:int = height
        self.vector:tuple[float,float] = vector
        self.velocity:float = velocity
        self.movingToNewPosition:bool = False
        self.visible:bool = visible
        self.border:bool = border
        self.borderColor:tuple[int,int,int] = borderColor
        self.borderWidth:int = borderWidth
        self.boundingBox = Rect(self.x, self.y, self.width, self.height)
        self._exactX:float = float(xPosition)
        self._exactY:float = float(yPosition)
        self._newPosition:tuple[int,int] = (0,0)
        return

    def change_position(self, newXPosition:int, newYPosition:int)->None:
        self.x = newXPosition
        self.y = newYPosition
        self._exactX = float(newXPosition)
        self._exactY = float(newYPosition)
        self.boundingBox.move(self.x, self.y)
        return

    def change_velocity(self, newVelocity:float)->None:
        self.velocity = newVelocity
        return
    
    def change_vector(self, newVector:tuple[float,float])->None:
        self.vector = newVector
        return

    def activate_border(self)->None:
        self.border = True
        return

    def deactivate_border(self)->None:
        self.border = False
        return

    def change_border_color(self, newBorderColor:tuple[int,int,int])->None:
        self.borderColor = newBorderColor
        return
    
    def change_border_width(self, newBorderWidth:int)->None:
        self.borderWidth = newBorderWidth
        return

    def head_to_new_position(self, newPosition:tuple[int,int], velocity:float=1.0)->None:
        diffVector = (self.x - newPosition[0], self.y - newPosition[1])
        magnitude =  math.sqrt((diffVector[0]*diffVector[0]) + (diffVector[1]*diffVector[1]))
        normalizeVector = ((diffVector[0] / magnitude), (diffVector[1] / magnitude))
        newVector = (normalizeVector[0] * velocity, normalizeVector[1] * velocity)
        self.change_vector(newVector)
        self._newPosition = newPosition
        self.movingToNewPosition = True
        return

    def move(self)->None:
        self._exactX += self.vector[0]
        self._exactY += self.vector[1]
        self.x = round(self._exactX)
        self.y = round(self._exactY)
        self.boundingBox.move(self.x, self.y)
        if self.movingToNewPosition and self._newPosition[0] == self.x and self._newPosition[1] == self.y:
            self.change_velocity(0.0)
            self.change_vector((0.0, 0.0))
            self.movingToNewPosition = False
            self._newPosition = None
        return
    
    def mouse_hover(self)->bool:
        return self.boundingBox.collidepoint(mouse.get_pos())

    @abstractmethod
    def render(self, screen:Surface)->None:
        return        

class PictureBoxObject(Object):
    def __init__(self, name:str, xPosition:int=0, yPosition:int=0, velocity:float=0.0, vector:tuple[float,float]=(0.0,0.0),
                  visible:bool=True, border:bool=False, borderColor:tuple[int,int,int]=(0,0,0), borderWidth:int=1,
                 img:Surface=None, imgPath:str=None)->None:
        if imgPath != None:
            self.image:Surface = image.load(imgPath)
        else:
            self.image:Surface = img
        super().__init__(name, xPosition, yPosition, self.image.get_width(), self.image.get_height(),
                         velocity, vector, visible, border, borderColor, borderWidth)
        return

    def change_image(self, newImg:Surface=None, newImgPath:str=None)->None:
        if newImgPath != None:
            self.image = image.load(newImgPath)
        else:
            self.image = newImg
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        return
    
    def render(self, screen:Surface)->None:
        if not self.visible:
            return
        if self.border:
            borderRect = self.image.get_rect()
            draw.rect(self.image, self.borderColor, borderRect,  self.borderWidth)
        screen.blit(self.image, (self.x, self.y))
        return

class TextObject(Object):
    def __init__(self, name:str, xPosition:int=0, yPosition:int=0, velocity:float=0.0, vector:tuple[float,float]=(0.0,0.0),
                 visible:bool=True, border:bool=False, borderColor:tuple[int,int,int]=(0,0,0), borderWidth:int=1,
                 text:str="", font:Font=None, fontColor:tuple[int,int,int]=(255,255,255), backgroundColor:tuple[int,int,int]=None)->None:
        super().__init__(name, xPosition, yPosition, velocity, vector, visible, border, borderColor, borderWidth)
        self.text:str = text
        self.font:Font = font
        self.fontColor:tuple[int,int,int] = fontColor
        self.textSurface:Surface = font.render(self.text, 1, self.fontColor)
        self.backgroundColor:tuple[int,int,int] = backgroundColor
        self.width:int = self.textSurface.get_width()
        self.height:int = self.textSurface.get_height()
        return

    def change_text(self, newText:str)->None:
        self.text = newText
        self.textSurface = self.font.render(self.text, 1, self.fontColor)
        self.width = self.textSurface.get_width()
        self.height = self.textSurface.get_height()
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
    
    def render(self, screen:Surface)->None:
        if not self.visible:
            return
        if self.border:
            borderRect = self.textSurface.get_rect()
            draw.rect(self.textSurface, self.borderColor, borderRect,  self.borderWidth)
        screen.blit(self.textSurface, (self.x, self.y))
        return
    
