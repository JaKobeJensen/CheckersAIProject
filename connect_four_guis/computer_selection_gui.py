import pygame
from pygame import Surface, display
from pygame.event import Event
from pygame.font import SysFont
from pygame.time import Clock

from codes import Codes
from connect_four import ConnectFour
from connect_four_guis.const import *
from gui_components import ButtonObject, Screen, TextObject


class ComputerSelectionGui:
    def __init__(self, scaling_factor: float = 1.0) -> None:
        self.display: Surface = display.set_mode(
            (
                round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
                round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
            )
        )
        self.screen: Screen = Screen(
            width=DEFAULT_DISPLAY_SIZE[0],
            height=DEFAULT_DISPLAY_SIZE[1],
            screen_scaling_factor=scaling_factor,
        )
        self.clock: Clock = Clock()
        
        self.screen.add_new_group("text")
        self.screen.add_new_group("buttons")
        
        """COMPUTER SELECTION TEXT"""
        computer_selection_text = TextObject(
            name="computerSelectionTxt",
            text="Computer Selection",
            text_font=SysFont(DEFAULT_FONT_TYPE, 84),
            scaling_factor=scaling_factor,
        )
        computer_selection_text.position = (
            round(self.screen.width / 2 - computer_selection_text.width / 2),
            round(self.screen.height * 0.05),
        )
        self.screen.add_new_sprite(computer_selection_text, computer_selection_text.name, "text", True)
        
        """EASY COMPUTER BUTTON"""
        easy_computer_button = ButtonObject(
            name="easyBtn",
            width=400,
            height=50,
            text="Easy",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                32,
            ),
            scaling_factor=scaling_factor,
        )
        easy_computer_button.position = (
            round(self.screen.width / 2 - easy_computer_button.width / 2),
            round(self.screen.height * 0.30),
        )
        self.screen.add_new_sprite(easy_computer_button, easy_computer_button.name, "buttons", True)
        
        """NORMAL COMPUTER BUTTON"""
        normal_computer_button = ButtonObject(
            name="normalBtn",
            width=400,
            height=50,
            text="Normal",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                32,
            ),
            scaling_factor=scaling_factor,
        )
        normal_computer_button.position = (
            round(self.screen.width / 2 - normal_computer_button.width / 2),
            round(self.screen.height * 0.40),
        )
        self.screen.add_new_sprite(normal_computer_button, normal_computer_button.name, "buttons", True)
        
        """HARD COMPUTER BUTTON"""
        hard_computer_button = ButtonObject(
            name="hardBtn",
            width=400,
            height=50,
            text="Hard",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                32,
            ),
            scaling_factor=scaling_factor,
        )
        hard_computer_button.position = (
            round(self.screen.width / 2 - hard_computer_button.width / 2),
            round(self.screen.height * 0.50),
        )
        self.screen.add_new_sprite(hard_computer_button, hard_computer_button.name, "buttons", True)
        
        """MASTER COMPUTER BUTTON"""
        master_computer_button = ButtonObject(
            name="masterBtn",
            width=400,
            height=50,
            text="Master",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                32,
            ),
            scaling_factor=scaling_factor,
        )
        master_computer_button.position = (
            round(self.screen.width / 2 - master_computer_button.width / 2),
            round(self.screen.height * 0.60),
        )
        self.screen.add_new_sprite(master_computer_button, master_computer_button.name, "buttons", True)
        
        """LOAD COMPUTER BUTTON"""
        laod_computer_button = ButtonObject(
            name="loadBtn",
            width=400,
            height=50,
            text="Load Computer",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                32,
            ),
            scaling_factor=scaling_factor,
        )
        laod_computer_button.position = (
            round(self.screen.width / 2 - laod_computer_button.width / 2),
            round(self.screen.height * 0.70),
        )
        self.screen.add_new_sprite(laod_computer_button, laod_computer_button.name, "buttons", True)
        
        """BACK BUTTON"""
        back_button = ButtonObject(
            name="backBtn",
            width=400,
            height=50,
            text="Back",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                32,
            ),
            scaling_factor=scaling_factor,
        )
        back_button.position = (
            round(self.screen.width / 2 - back_button.width / 2),
            round(self.screen.height * 0.80),
        )
        self.screen.add_new_sprite(back_button, back_button.name, "buttons", True)
        
        return
    
    def _event_check(self, event: Event) -> Codes:
        if event.type == pygame.QUIT:
            return Codes.QUIT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.screen.get_sprites_from_group("buttons"):
                if type(button) is not ButtonObject: continue
                if button.move_hover() and button.name == "easyBtn":
                    return Codes.EASY_MODE
                if button.move_hover() and button.name == "normalBtn":
                    return Codes.NORMAL_MODE
                if button.move_hover() and button.name == "hardBtn":
                    return Codes.HARD_MODE
                if button.move_hover() and button.name == "masterBtn":
                    return Codes.MASTER_MODE
                if button.move_hover() and button.name == "loadBtn":
                    return Codes.LOAD_COMPUTER
                if button.move_hover() and button.name == "backBtn":
                    return Codes.BACK
        return Codes.RUNNING

    def start(self) -> Codes:
        code = Codes.RUNNING
        while code is Codes.RUNNING:
            for event in pygame.event.get():
                code = self._event_check(event)
            self.screen.update()
            self.display.blit(
                self.screen.screen,
                (self.screen.x, self.screen.y),
            )
            display.update()
            self.clock.tick(DEFAULT_FRAMERATE)
        return code