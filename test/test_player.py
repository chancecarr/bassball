import pytest
from player import Player
import random

def test_player_generation():
    expected_stats = {
        "Batting": {"Contact": 86, "Placement": 49},
        "Running": {"Speed": 48, "Stealing": 73},
        "Pitching": {"Arm": 101, "Technique": 60},
        "Fielding": {"Catching": 84, "Sense": 98},
    }
    expected: Player = Player("Roe", "Kelpmoss", expected_stats)
    actual = Player.generate_player(random.Random(1))
    assert expected == actual

def test_throw_pitch():
    rng = random.Random(1)
    expected = (73, 63, 100)
    player = Player.generate_player(rng)
    actual = player.throw_pitch(rng)
    assert expected == actual
