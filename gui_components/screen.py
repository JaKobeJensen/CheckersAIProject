from pygame import Surface
from pygame.sprite import LayeredUpdates


class Screen:
    def __init__(
        self,
        x_position: int = 0,
        y_position: int = 0,
        width: int = 600,
        height: int = 600,
        screen_scaling_factor: float = 1.0,
        background_color: tuple[int, int, int] = None,
    ) -> None:
        self._width: int = round(width * screen_scaling_factor)
        self._height: int = round(height * screen_scaling_factor)
        self.screen: Surface = Surface((self._width, self._height))
        self._scaling_factor = screen_scaling_factor
        self.gameObjects: LayeredUpdates = LayeredUpdates()
        self.x: int = x_position
        self.y: int = y_position
        self._background_color: tuple[int, int, int] = background_color
        if self.background_color:
            self.screen.fill(self.background_color)
        return

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def scaling_factor(self) -> float:
        return self._scaling_factor

    @scaling_factor.setter
    def scaling_factor(self, new_scaling_factor: float) -> None:
        self._scaling_factor = new_scaling_factor
        self.change_size(self._width, self._height)
        return

    @property
    def background_color(self) -> tuple[int, int, int]:
        return self._background_color

    @background_color.setter
    def background_color(self, new_background_color: tuple[int, int, int]) -> None:
        self._background_color = new_background_color
        self.screen.fill(self._background_color)
        return

    def get_size(self) -> tuple[int, int]:
        return (self._width, self._height)

    def change_size(self, new_size: tuple[int, int]) -> None:
        self._width = new_size[0] * self._scaling_factor
        self._height = new_size[1] * self._scaling_factor
        self.screen = Surface((self._width, self._height))
        return

    def clear(self) -> None:
        if self._background_color is None:
            self.screen.fill((0, 0, 0))
        else:
            self.screen.fill(self._background_color)
        return
