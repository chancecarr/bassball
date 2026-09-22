import pytest
from team import Team
from player import Player
import random

def test_team_generation():
    expected = Team(
        name='The Cod City Squeezers', 
        roster={
            'P': Player(
                first_name='Shoal', 
                last_name='Saint-Salmon', 
                stats={'Batting': {'Contact': 70, 'Placement': 42}, 'Running': {'Speed': 45, 'Stealing': 70}, 'Pitching': {'Arm': 121, 'Technique': 93}, 'Fielding': {'Catching': 68, 'Sense': 49}}
            ), 
            'C': Player(
                first_name='Briny', 
                last_name='Castman', 
                stats={'Batting': {'Contact': 44, 'Placement': 111}, 'Running': {'Speed': 103, 'Stealing': 63}, 'Pitching': {'Arm': 56, 'Technique': 102}, 'Fielding': {'Catching': 88, 'Sense': 39}}
            ), 
            '1B': Player(
                first_name='Gills', 
                last_name="O'Gill", 
                stats={'Batting': {'Contact': 72, 'Placement': 84}, 'Running': {'Speed': 46, 'Stealing': 59}, 'Pitching': {'Arm': 120, 'Technique': 41}, 'Fielding': {'Catching': 134, 'Sense': 53}}
            ), 
            '2B': Player(
                first_name='Cheeky', 
                last_name='Seabed', 
                stats={'Batting': {'Contact': 86, 'Placement': 94}, 'Running': {'Speed': 63, 'Stealing': 64}, 'Pitching': {'Arm': 36, 'Technique': 41}, 'Fielding': {'Catching': 136, 'Sense': 47}}
            ), 
            '3B': Player(
                first_name='Splash', 
                last_name='Seabed', 
                stats={'Batting': {'Contact': 64, 'Placement': 39}, 'Running': {'Speed': 76, 'Stealing': 82}, 'Pitching': {'Arm': 55, 'Technique': 90}, 'Fielding': {'Catching': 72, 'Sense': 98}}
            ), 
            'SS': Player(
                first_name='Chum', 
                last_name='Catfish', 
                stats={'Batting': {'Contact': 54, 'Placement': 37}, 'Running': {'Speed': 44, 'Stealing': 73}, 'Pitching': {'Arm': 39, 'Technique': 111}, 'Fielding': {'Catching': 141, 'Sense': 52}}
            ), 
            'LF': Player(
                first_name='Splash', 
                last_name='Gill-Smasher', 
                stats={'Batting': {'Contact': 64, 'Placement': 42}, 'Running': {'Speed': 72, 'Stealing': 69}, 'Pitching': {'Arm': 144, 'Technique': 64}, 'Fielding': {'Catching': 47, 'Sense': 81}}
            ), 
            'CF': Player(
                first_name='Squishy', 
                last_name='Sculpin', 
                stats={'Batting': {'Contact': 41, 'Placement': 44}, 'Running': {'Speed': 83, 'Stealing': 47}, 'Pitching': {'Arm': 120, 'Technique': 172}, 'Fielding': {'Catching': 44, 'Sense': 53}}
            ), 
            'RF': Player(
                first_name='Squishy', 
                last_name='Scale-Striker', 
                stats={'Batting': {'Contact': 49, 'Placement': 40}, 'Running': {'Speed': 49, 'Stealing': 92}, 'Pitching': {'Arm': 125, 'Technique': 52}, 'Fielding': {'Catching': 132, 'Sense': 43}}
            )
        }
    )
    actual = Team.generate_team(random.Random(1))
    assert actual == expected