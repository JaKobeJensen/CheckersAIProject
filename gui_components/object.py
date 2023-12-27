from pygame import Rect, Surface
from pygame.math import Vector2
from pygame.sprite import Sprite


class Object(Sprite):
    def __init__(
        self,
        name: str,
        image: Surface,
        position: Vector2 = Vector2(),
        direction: Vector2 = Vector2(),
        velocity: float = 0.0,
        terminal_velocity: float = 10.0,
        acceleration: float = 0.0,
        visible: bool = True,
    ) -> None:
        super.__init__(self)
        self._name = name
        self._image: Surface = image
        self._position: Vector2 = position.copy
        self._rect: Rect = Rect((self.x, self.y), (self.width, self.height))
        self._direction: Vector2 = direction.normalize()
        self._velocity: float = velocity
        self.terminal_velocity: float = terminal_velocity
        self.acceleration: float = acceleration
        self.visible: bool = visible
        return

    @property
    def name(self) -> str:
        return self._name

    @property
    def image(self) -> Surface:
        return self._image

    @image.setter
    def image(self, new_image: Surface) -> None:
        self._image = new_image
        self._rect = Rect((self.x, self.y), (self.width, self.height))
        return

    @property
    def width(self) -> int:
        return self._image.get_width()

    @property
    def height(self) -> int:
        return self._image.get_height()

    @property
    def position(self) -> Vector2:
        return self._position.copy

    @position.setter()
    def position(self, new_position: Vector2) -> None:
        self._position = new_position
        self._rect.x = new_position[0]
        self._rect.y = new_position[1]
        return

    @property
    def x(self) -> int:
        return int(self._position.x)

    @x.setter
    def x(self, new_x: int | float) -> None:
        self.position = Vector2(new_x, self.y)
        return

    @property
    def y(self) -> int:
        return int(self._position.y)

    @y.setter
    def y(self, new_y: int | float) -> None:
        self.position = Vector2(self.x, new_y)
        return

    @property
    def direction(self) -> Vector2:
        return self._direction.copy

    @direction.setter
    def direction(self, new_direction: Vector2) -> None:
        self._direction = new_direction.normalize()
        return

    @property
    def velocity(self) -> float:
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity) -> None:
        if new_velocity < self.terminal_velocity:
            self._velocity = new_velocity
        else:
            self._velocity = self.terminal_velocity
        return

    def update(self) -> None:
        self.velocity += self.acceleration
        self.velocity_vector = self._direction * self._velocity
        self.position += self.velocity_vector
        return
