from game import Game, Half
from player import Player
from bases import Bases
from dataclasses import replace

class GameEngine:
    def __init__(self):
        ...

    def advance_game(self, game: Game) -> Game:
        if game.is_game_over:
            return replace(game, game_over=True)
        elif game.outs == 3:
            new_inning = game.inning + 1
            new_half = Half.TOP if game.half == Half.BOTTOM else Half.BOTTOM
            return replace(game, inning=new_inning, half=new_half, outs=0, bases=Bases.clear_bases())
        else:
            batter: Player = next(game.home.batting_order) if game.half == Half.BOTTOM else next(game.away.batting_order)
            return self.play_at_bat(game, batter)

    def play_at_bat(self, game: Game, batter: Player) -> Game:
        raise NotImplementedError