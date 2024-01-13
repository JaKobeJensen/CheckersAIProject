from time import sleep
import random
import copy

import pygame
from pygame import Surface, display
from pygame.event import Event
from pygame.font import SysFont
from pygame.time import Clock

from codes import Codes
from connect_four import ConnectFour
from connect_four_guis.const import *
from connect_four_objects import GameBoard, RedPiece, YellowPiece
from gui_components import BoundingBoxObject, Screen, TextObject
from minmax_connect_four_ai import MinimaxConnectFourAI


class ConnectFourGui:
    PLAYER_NAMES_SIZE = 32
    PLAYER_PIECE_INDICATOR_SCALING = 0.4
    
    def __init__(
        self,
        player1_name: str,
        player2_name: str,
        mode: str = "pvp",
        computer_difficulty: str = None,
        scaling_factor: float = 1.0,
    ) -> None:
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
        
        if random.randint(0,1) == 0:
            self.connect_four = ConnectFour(player1_name, player2_name)
            self.player1_name: str = player1_name
            self.player2_name: str = player2_name
            if mode == "pvc":
                self._computer = MinimaxConnectFourAI(player2_name, self.connect_four.PLAYER2_SPACE, computer_difficulty)
            else:
                self._computer = None
        else:
            self.connect_four = ConnectFour(player2_name, player1_name)
            self.player1_name: str = player2_name
            self.player2_name: str = player1_name
            if mode == "pvc":
                self._computer = MinimaxConnectFourAI(player2_name, self.connect_four.PLAYER1_SPACE, computer_difficulty)
            else:
                self._computer = None
        
        self._mode: str = mode
        self._computer_difficulty: str = computer_difficulty
        self.scaling_factor: float = scaling_factor
        self.clock: Clock = Clock()
        self._current_column: int = 0

        self.screen.add_new_group("static_objects")
        self.screen.add_new_group("played_pieces")
        self.screen.add_new_group("chooser_pieces")
        self.screen.add_new_group("column_bounding_boxes")

        """PLAYER1 NAME TEXT"""
        player1_name_text = TextObject(
            name="player1NameTxt",
            text=self.player1_name,
            text_font=SysFont(DEFAULT_FONT_TYPE, self.PLAYER_NAMES_SIZE),
            scaling_factor=scaling_factor,
        )
        player1_name_text.position = (
            round(self.screen.width * 0.02),
            round(self.screen.height * 0.02),
        )
        self.screen.add_new_sprite(player1_name_text, player1_name_text.name, "static_objects")

        """PLAYER2 NAME TEXT"""
        player2_name_text = TextObject(
            name="player2NameTxt",
            text=self.player2_name,
            text_font=SysFont(DEFAULT_FONT_TYPE, self.PLAYER_NAMES_SIZE),
            scaling_factor=scaling_factor,
        )
        player2_name_text.position = (
            round(
                (self.screen.width - player2_name_text.width)
                - (self.screen.height * 0.02)
            ),
            round(self.screen.width * 0.02),
        )
        self.screen.add_new_sprite(player2_name_text, player2_name_text.name, "static_objects")

        """PLAYER 1 PIECE INDICATOR"""
        player1_piece_indicator = RedPiece(
            name="player1Indicator",
            scaling_factor=scaling_factor * self.PLAYER_PIECE_INDICATOR_SCALING,
        )
        player1_piece_indicator.position = (
            round(player1_name_text.rect.right + player1_piece_indicator.width * 0.5),
            round(
                player1_name_text.y
                - (player1_piece_indicator.height - player1_name_text.height)
            ),
        )
        self.screen.add_new_sprite(player1_piece_indicator, player1_piece_indicator.name, "static_objects")

        """PLAYER 2 PIECE INDICATOR"""
        player2_piece_indicator = YellowPiece(
            name="player2Indicator",
            scaling_factor=scaling_factor * self.PLAYER_PIECE_INDICATOR_SCALING,
        )
        player2_piece_indicator.position = (
            round(
                player2_name_text.rect.left
                - player2_piece_indicator.width
                - player2_piece_indicator.width * 0.5
            ),
            round(
                player2_name_text.y
                - (player2_piece_indicator.height - player2_name_text.height)
            ),
        )
        self.screen.add_new_sprite(player2_piece_indicator, player2_piece_indicator.name, "static_objects")

        """CONNECT FOUR BOARD"""
        connect_four_board = GameBoard(name="gameboard", scaling_factor=scaling_factor)
        connect_four_board.position = (
            round(self.screen.width / 2 - connect_four_board.width / 2),
            round(
                (self.screen.height - connect_four_board.height)
                - (self.screen.height * 0.05)
            ),
        )
        self.screen.add_new_sprite(connect_four_board, connect_four_board.name, "static_objects", top_layer=True)

        """RED PIECE CHOOSER"""
        red_piece_chooser = RedPiece(
            name="redPieceChooser", scaling_factor=scaling_factor, visible=True
        )
        red_piece_chooser.position = (
            connect_four_board.x,
            connect_four_board.y
            - red_piece_chooser.height
            - round(red_piece_chooser.height * 0.3),
        )
        self.screen.add_new_sprite(red_piece_chooser, red_piece_chooser.name, "chooser_pieces")

        """YELLOW PIECE CHOOSER"""
        yellow_piece_chooser = YellowPiece(
            name="yellowPieceChooser", scaling_factor=scaling_factor, visible=False
        )
        yellow_piece_chooser.position = (
            connect_four_board.x,
            connect_four_board.y
            - yellow_piece_chooser.height
            - round(yellow_piece_chooser.height * 0.3),
        )
        self.screen.add_new_sprite(yellow_piece_chooser, yellow_piece_chooser.name, "chooser_pieces")

        """BOUNDING BOX OBJECTS"""
        for i in range(7):
            column_bounding_box = BoundingBoxObject(
                name="column{0}Bbx".format(i),
                width=84,
                height=self.screen.height,
                scaling_factor=scaling_factor,
                visible=False,
            )
            column_bounding_box.position = (
                round((column_bounding_box.width * i) + (connect_four_board.x + 7)),
                0,
            )
            self.screen.add_new_sprite(column_bounding_box, column_bounding_box.name, "column_bounding_boxes")

        return

    def _event_check(self, event: Event) -> Codes:
        if event.type == pygame.QUIT:
            return Codes.QUIT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._drop_piece()
            if self._check_winner():
                self._wait_for_click()
                return Codes.WINNER
            if self._mode == "pvc":
                return Codes.COMPUTER_TURN
        return Codes.RUNNING

    def _mouse_hover_column_bounding_box_check(self) -> None:
        for column_index, column in enumerate(self.screen.get_sprites_from_group("column_bounding_boxes")):
            if type(column) is not BoundingBoxObject: continue
            if column.move_hover():
                for chooser in self.screen.get_sprites_from_group("chooser_pieces"):
                    chooser.x = round(column.x + (column.width / 2 - chooser.width / 2))
                    self._current_column = column_index
        return

    def _drop_piece(self) -> None:
        if self.connect_four.winner is not None:
            return
        self.connect_four.player_move(self._current_column)
        
        """NEW PIECE"""
        if self.connect_four.whos_turn == self.player2_name:
            new_piece = RedPiece(
                name="redPiece{0}".format(
                    int(self.connect_four.number_of_moves - 1 / 2)
                ),
                scaling_factor=self.scaling_factor,
                visible=True,
            )
            self.screen.get_sprite("redPieceChooser").visible = False
            self.screen.get_sprite("yellowPieceChooser").visible = True
        else:
            new_piece = YellowPiece(
                name="yellowPiece{0}".format(
                    round(self.connect_four.number_of_moves - 1 / 2)
                ),
                scaling_factor=self.scaling_factor,
                visible=True,
            )
            self.screen.get_sprite("redPieceChooser").visible = True
            self.screen.get_sprite("yellowPieceChooser").visible = False 
        new_piece.position = (
            self.screen.get_sprite("redPieceChooser").x, 
            (self.screen.get_sprite("gameboard").y + 15) + (self.screen.get_sprite("column0Bbx").width * self.connect_four.last_piece_played_position[0]),
        )
        self.screen.add_new_sprite(new_piece, new_piece.name, "played_pieces", top_layer=False)
        
        return

    def _check_winner(self) -> bool:
        if len(self.connect_four.legal_moves()) == 0:
            self.screen.get_sprite("redPieceChooser").visible = False
            self.screen.get_sprite("yellowPieceChooser").visible = False
            tie_text = TextObject(
                name="tieTxt",
                text="Tie",
                text_font=SysFont(DEFAULT_FONT_TYPE, 72),
                scaling_factor=self.scaling_factor,
            )
            tie_text.position = (
                round(self.screen.width / 2 - tie_text.width / 2),
                round(self.screen.height * 0.1),
            )
            self.screen.add_new_sprite(tie_text, tie_text.name, "static_objects")
            return True
        elif self.connect_four.winner is not None:
            self.screen.get_sprite("redPieceChooser").visible = False
            self.screen.get_sprite("yellowPieceChooser").visible = False
            winner_text = TextObject(
                name="winnerTxt",
                text="{0} Wins".format(self.connect_four.winner),
                text_font=SysFont(DEFAULT_FONT_TYPE, 72),
                scaling_factor=self.scaling_factor,
            )
            winner_text.position = (
                round(self.screen.width / 2 - winner_text.width / 2),
                round(self.screen.height * 0.1),
            )
            self.screen.add_new_sprite(winner_text, winner_text.name, "static_objects")
            return True
        return False
    
    def _wait_for_click(self) -> None:
        click_to_continue = TextObject(
            name="continueTxt",
            text="Click To Continue",
            text_font=SysFont(DEFAULT_FONT_TYPE, 84),
            scaling_factor=self.scaling_factor,
        )
        click_to_continue.position = (
            round(self.screen.width / 2 - click_to_continue.width / 2),
            round(self.screen.height / 2 - click_to_continue.height / 2),
        )
        self.screen.add_new_sprite(click_to_continue, click_to_continue.name, "static_objects")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
            self.screen.update()
            self.display.blit(
                self.screen.screen,
                (self.screen.x, self.screen.y),
            )
            display.update()
            self.clock.tick(DEFAULT_FRAMERATE)

    def _computer_play(self) -> Codes:
        self.update_display()
        computer_move = self._computer.move(copy.deepcopy(self.connect_four))
        if self._computer_difficulty != "master":
            sleep(1)
        pygame.mouse.set_pos(self.screen.get_sprite("column{0}Bbx".format(computer_move)).rect.center)
        self._mouse_hover_column_bounding_box_check()
        self.update_display()
        sleep(0.5)
        self._drop_piece()
        if self._check_winner():
            self._wait_for_click()
            return Codes.WINNER
        return Codes.RUNNING
    
    def update_display(self) -> None:
        self.screen.update()
        self.display.blit(
            self.screen.screen,
            (self.screen.x, self.screen.y),
        )
        display.update()
        self.clock.tick(DEFAULT_FRAMERATE)
        return
    
    def start(self) -> Codes:
        if self._computer is not None and self.connect_four.player1_name == self._computer.name:
            self._computer_play()
        
        code = Codes.RUNNING
        while code is Codes.RUNNING:
            for event in pygame.event.get():
                code = self._event_check(event)
                if code == Codes.COMPUTER_TURN:
                    code = self._computer_play()

            self._mouse_hover_column_bounding_box_check()

            self.update_display()
                
        return code
