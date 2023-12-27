from pygame.font import Font, SysFont
from pygame.math import Vector2

from gui_components import Object


class TextObject(Object):
    def __init__(
        self,
        name: str,
        text: str,
        text_color: tuple[int, int, int] = (0, 0, 0),
        text_font: Font = SysFont("Aptos", 16),
        position: Vector2 = Vector2(),
        direction: Vector2 = Vector2(),
        velocity: float = 0.0,
        terminal_velocity: float = 10.0,
        acceleration: float = 0.0,
        visible: bool = True,
    ) -> None:
        self._text: str = text
        self._text_color: tuple[int, int, int] = text_color
        self._text_font: Font = text_font
        image = self._text_font.render(self._text, 1, self._text_color)
        super().__init__(
            name,
            image,
            position,
            direction,
            velocity,
            terminal_velocity,
            acceleration,
            visible,
        )
        return

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text
        self.image = self._text_font.render(self._text, 1, self._text_color)
        return

    @property
    def text_color(self) -> tuple[int, int, int]:
        return self._text_color

    @text.setter
    def text_color(self, new_text_color: tuple[int, int, int]) -> None:
        self._text_color = new_text_color
        self.image = self._text_font.render(self._text, 1, self._text_color)
        return

    @property
    def text_font(self) -> Font:
        return self._text_font

    @text_font.setter
    def text_font(self, new_text_font: Font) -> None:
        self._text_font = new_text_font
        self.image = self._text_font.render(self._text, 1, self._text_color)
        return
