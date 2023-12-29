import pygame
from pygame import Surface, display
from pygame.event import Event
from pygame.font import SysFont
from pygame.time import Clock

from codes import Codes
from connect_four_guis.const import *
from gui_components import ButtonObject, Screen, TextObject


class MainMenuGui:
    TITLE_TEXT_SIZE = 72
    BUTTON_SIZE = (300, 40)
    BUTTON_TEXT_SIZE = 24

    def __init__(self, scaling_factor: float = 1.0) -> None:
        self.display: Surface = display.set_mode(
            (
                round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
                round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
            )
        )
        self.screen: Screen = Screen(
            width=round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
            height=round(DEFAULT_DISPLAY_SIZE[1] * scaling_factor),
        )
        self.game_object_id: dict[str, int] = {}
        self.scaling_factor = scaling_factor
        self.clock = Clock()

        """TITLE TEXT"""
        title_text = TextObject(
            name="titleTxt",
            text="Connect Four",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                round(self.TITLE_TEXT_SIZE * scaling_factor),
                True,
            ),
        )
        title_text.position = (
            int(self.screen.width / 2 - title_text.width / 2),
            int(self.screen.height * 0.05),
        )
        self.game_object_id[title_text.name] = len(self.screen.game_objects)
        self.screen.game_objects.add(title_text)

        """PLAYER VS PLAYER BUTTON"""
        player_vs_player_button = ButtonObject(
            name="pvpBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Player VS Player",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                round(self.BUTTON_TEXT_SIZE * scaling_factor),
            ),
        )
        player_vs_player_button.position = (
            int(self.screen.width / 2 - player_vs_player_button.width / 2),
            int(self.screen.height * 0.25),
        )
        self.game_object_id[player_vs_player_button.name] = len(
            self.screen.game_objects
        )
        self.screen.game_objects.add(player_vs_player_button)

        """PLAYER VS COMPUTER BUTTON"""
        player_vs_computer_button = ButtonObject(
            name="pvcBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Player VS Computer",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                round(self.BUTTON_TEXT_SIZE * scaling_factor),
            ),
        )
        player_vs_computer_button.position = (
            int(self.screen.width / 2 - player_vs_computer_button.width / 2),
            int(self.screen.height * 0.40),
        )
        self.game_object_id[player_vs_computer_button.name] = len(
            self.screen.game_objects
        )
        self.screen.game_objects.add(player_vs_computer_button)

        """COMPUTER VS COMPUTER BUTTON"""
        computer_vs_computer_button = ButtonObject(
            name="cvcBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Computer VS Computer",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                round(self.BUTTON_TEXT_SIZE * scaling_factor),
            ),
        )
        computer_vs_computer_button.position = (
            int(self.screen.width / 2 - computer_vs_computer_button.width / 2),
            int(self.screen.height * 0.55),
        )
        self.game_object_id[computer_vs_computer_button.name] = len(
            self.screen.game_objects
        )
        self.screen.game_objects.add(computer_vs_computer_button)

        """TRAIN COMPUTER BUTTON"""
        train_computer_button = ButtonObject(
            name="trainBtn",
            width=self.BUTTON_SIZE[0],
            height=self.BUTTON_SIZE[1],
            text="Train Computer",
            text_font=SysFont(
                DEFAULT_FONT_TYPE,
                round(self.BUTTON_TEXT_SIZE * scaling_factor),
            ),
        )
        train_computer_button.position = (
            int(self.screen.width / 2 - train_computer_button.width / 2),
            int(self.screen.height * 0.70),
        )
        self.game_object_id[train_computer_button.name] = len(self.screen.game_objects)
        self.screen.game_objects.add(train_computer_button)

        return

    def _event_check(self, event: Event) -> Codes:
        if event.type == pygame.QUIT:
            return Codes.QUIT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for game_object in self.screen.game_objects:
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
