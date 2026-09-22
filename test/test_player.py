import pytest
from player import Player

def test_player_generation():
    expected_stats = {
        "Batting": {"Contact": 86, "Placement": 49},
        "Running": {"Speed": 48, "Stealing": 73},
        "Pitching": {"Arm": 101, "Technique": 60},
        "Fielding": {"Catching": 84, "Sense": 98},
    }
    expected: Player = Player("Roe", "Kelpmoss", expected_stats)
    actual = Player.generate_player(1)
    assert expected == actual