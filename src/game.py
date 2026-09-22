from team import Team
from enum import Enum
from bases import Bases
from dataclasses import dataclass, field

class Half(Enum):
    TOP = "Top"
    BOTTOM = "Bottom"

@dataclass
class Game:
    home: Team
    away: Team
    inning: int = 1
    half: Half = Half.TOP
    home_score: int = 0
    away_score: int = 0
    outs: int = 0
    bases: Bases = field(default_factory=Bases)

    @property
    def is_game_over(self) -> bool:
        is_bottom_half = self.half == Half.BOTTOM
        is_half_over = self.outs == 3
        does_a_team_lead = self.home_score != self.away_score
        nine_innings_played = self.inning >= 9
        return (
            is_bottom_half
            and is_half_over
            and does_a_team_lead
            and nine_innings_played
        )
    