import pygame
from pygame import Surface, display
from pygame.event import Event
from pygame.font import SysFont
from pygame.time import Clock

from codes import Codes
from connect_four_guis.const import *
from gui_components import ButtonObject, Screen, TextObject


class MainMenuGui:
    TITLE_TEXT_SIZE = 108
    BUTTON_SIZE = (400, 50)
    BUTTON_TEXT_SIZE = 32

    def __init__(self, scaling_factor: float = 1.0) -> None:
        self.display: Surface = display.set_mode(
            (
                round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
                round(DEFAULT_DISPLAY_SIZE[1] * scaling_factor),
            )
        )
        self.screen: Screen = Screen(
            width=DEFAULT_DISPLAY_SIZE[0],
            height=DEFAULT_DISPLAY_SIZE[1],
            screen_scaling_factor=scaling_factor,
        )
        self.scaling_factor = scaling_factor
        self.clock = Clock()
        self.screen.add_new_group("static_objects")

        """TITLE TEXT"""
        title_text = TextObject(
            name="titleTxt",
            text="Connect Four",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                self.TITLE_TEXT_SIZE,
            ),
            scaling_factor=scaling_factor,
        )
        title_text.position = (
            round(self.screen.width / 2 - title_text.width / 2),
            round(self.screen.height * 0.05),
        )
        self.screen.groups["static_objects"].add(title_text)

        """PLAYER VS PLAYER BUTTON"""
        player_vs_player_button = ButtonObject(
            name="pvpBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Player VS Player",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                self.BUTTON_TEXT_SIZE,
            ),
            scaling_factor=scaling_factor,
        )
        player_vs_player_button.position = (
            round(self.screen.width / 2 - player_vs_player_button.width / 2),
            round(self.screen.height * 0.25),
        )
        self.screen.groups["static_objects"].add(player_vs_player_button)

        """PLAYER VS COMPUTER BUTTON"""
        player_vs_computer_button = ButtonObject(
            name="pvcBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Player VS Computer",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                self.BUTTON_TEXT_SIZE,
            ),
            scaling_factor=scaling_factor,
        )
        player_vs_computer_button.position = (
            round(self.screen.width / 2 - player_vs_player_button.width / 2),
            round(self.screen.height * 0.40),
        )
        self.screen.groups["static_objects"].add(player_vs_computer_button)

        """COMPUTER VS COMPUTER BUTTON"""
        computer_vs_computer_button = ButtonObject(
            name="cvcBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Computer VS Computer",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                self.BUTTON_TEXT_SIZE,
            ),
            scaling_factor=scaling_factor,
        )
        computer_vs_computer_button.position = (
            round(self.screen.width / 2 - player_vs_player_button.width / 2),
            round(self.screen.height * 0.55),
        )
        self.screen.groups["static_objects"].add(computer_vs_computer_button)

        """TRAIN COMPUTER BUTTON"""
        train_computer_button = ButtonObject(
            name="trainBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Train Computer",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                self.BUTTON_TEXT_SIZE,
            ),
            scaling_factor=scaling_factor,
        )
        train_computer_button.position = (
            round(self.screen.width / 2 - player_vs_player_button.width / 2),
            round(self.screen.height * 0.70),
        )
        self.screen.groups["static_objects"].add(train_computer_button)

        return

    def _event_check(self, event: Event) -> Codes:
        if event.type == pygame.QUIT:
            return Codes.QUIT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for game_object in self.screen.groups["static_objects"]:
                if type(game_object) is not ButtonObject:
                    continue
                if game_object.move_hover() and game_object.name == "pvpBtn":
                    return Codes.PLAYER_VS_PLAYER
                if game_object.move_hover() and game_object.name == "pvcBtn":
                    return Codes.PLAYER_VS_COMPUTER
                if game_object.move_hover() and game_object.name == "cvcBtn":
                    return Codes.COMPUTER_VS_COMPUTER
                if game_object.move_hover() and game_object.name == "trainBtn":
                    return Codes.TRAIN_COMPUTER
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
