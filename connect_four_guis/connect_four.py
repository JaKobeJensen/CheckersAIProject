import pygame
from pygame import Surface, display
from pygame.event import Event
from pygame.time import Clock

from codes import Codes
from connect_four_guis.const import *
from gui_components import BoundingBoxObject, Screen


class ConnectFourGui:
    COLUMN_BOUNDING_BOX_SIZE = (
        round(DEFAULT_DISPLAY_SIZE[0] / 7),
        DEFAULT_DISPLAY_SIZE[1],
    )

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

        """BOUNDING BOX OBJECTS"""
        for i in range(7):
            column_bounding_box = BoundingBoxObject(
                name="column{0}Bbx".format(i),
                width=self.COLUMN_BOUNDING_BOX_SIZE[0],
                height=self.COLUMN_BOUNDING_BOX_SIZE[1],
                border=True,
            )
            column_bounding_box.position = (
                int(column_bounding_box.width * i),
                0,
            )
            self.game_object_id[column_bounding_box.name] = len(
                self.screen.game_objects
            )
            self.screen.game_objects.add(column_bounding_box)
        return

    def _event_check(self, event: Event) -> Codes:
        if event.type == pygame.QUIT:
            return Codes.QUIT
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
