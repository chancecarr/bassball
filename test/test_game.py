import pytest
import random
from team import Team
from game import Game, Half

def test_game_over():
    rng = random.Random(1)
    home_team = Team.generate_team(rng)
    away_team = Team.generate_team(rng)
    game = Game(home_team, away_team, home_score=1, inning=9, half=Half.BOTTOM, outs=3)
    assert game.is_game_over == True

def test_not_game_over():
    rng = random.Random(1)
    home_team = Team.generate_team(rng)
    away_team = Team.generate_team(rng)
    game = Game(home_team, away_team, home_score=1, inning=9, half=Half.TOP, outs=3)
    assert game.is_game_over == False
