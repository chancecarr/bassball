from dataclasses import dataclass, field
from player import Player

@dataclass 
class Bases:
    occupancy: dict[str, Player | None] = field(default_factory=lambda: {"First": None, "Second": None, "Third": None})