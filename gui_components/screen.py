from pygame import Surface
from pygame.sprite import LayeredUpdates, Sprite

from gui_components.objects import Object


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
        self._groups: dict[str, dict[str, tuple(int, bool)]] = {}
        self._groups["all"] = {}
        self._sprite_group: LayeredUpdates = LayeredUpdates()
        self.x: int = x_position
        self.y: int = y_position
        self._background_color: tuple[int, int, int] = background_color
        self._top_layer_count: int = 0
        self._bottom_layer_count: int = 0
        self.clear()

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
            self.screen.fill((255, 255, 255))
        else:
            self.screen.fill(self._background_color)
        return

    def add_new_group(self, group_name: str) -> None:
        self._groups[group_name] = {}
        return
    
    def add_new_sprite(self, sprite: Object, sprite_name: str, group_name: str=None, top: bool=True) -> None:
        if group_name is not None and group_name in self._groups and group_name != "all":
            if top:
                self._groups[group_name][sprite_name] = (self._top_layer_count, top)
            else:
                self._groups[group_name][sprite_name] = (self._bottom_layer_count, top)
        else:
            return
        self._sprite_group.add(sprite)
        if top:
            self._groups["all"][sprite_name] = (self._top_layer_count, top)
            self._top_layer_count+=1
            self._sprite_group.move_to_front(sprite)
        else:
            self._groups["all"][sprite_name] = (self._bottom_layer_count, top)
            self._bottom_layer_count+=1
            self._sprite_group.move_to_back(sprite)
        return
    
    def get_sprite(self, sprite_name: str) -> Object:
        sprite = self._groups["all"][sprite_name]
        if sprite[1]:
            return self._sprite_group.get_sprite(sprite[0] + self._bottom_layer_count)
        else:
            return self._sprite_group.get_sprite(sprite[0])
    
    def get_sprites_from_group(self, group_name: str) -> list[Object]:
        sprites = []
        for sprite_name, sprite in self._groups[group_name].items():
            if sprite[1]:
                sprites.append(self._sprite_group.get_sprite(sprite[0] + self._bottom_layer_count))
            else:
                sprites.append(self._sprite_group.get_sprite(sprite[0]))
        return sprites

    def update(self) -> None:
        self.clear()
        self._sprite_group.update()
        self._sprite_group.draw(self.screen)
