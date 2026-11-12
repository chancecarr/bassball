import random

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
            return replace(game, inning=new_inning, half=new_half, outs=0, bases=Bases())
        else:
            batter: Player = next(game.home.batting_order) if game.half == Half.BOTTOM else next(game.away.batting_order)
            return self.play_at_bat(game, batter, balls=0, strikes=0)

    def play_at_bat(self, game: Game, batter: Player, balls: int, strikes: int, rng: random.Random | None = None) -> Game:
        fielding_team = game.home if game.half == Half.TOP else game.away

        # Simulate pitch
        #   - In strike zone?
        # Simulate swing
        #   - If strike, looking or swinging?
        #   - Determine contact
        #       - Possibilities on contact:
        #           - Foul ball
        #           - Out (ground out/fly out)
        #           - Fielder's choice/sacrifice play
        #           - Base hit (nonnegotiable Single, Double, Triple, or HR)
        #           - Purposeful sacrifice bunt or fly
        # Simulate run
        #   - Number of bases?
        #   - Fielder's choice
        