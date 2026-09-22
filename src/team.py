from dataclasses import dataclass
from player import Player
from itertools import cycle
import random

TEAM_HOMES = [
    "Ankle Deep",
    "Bait Cove",
    "Brine Port",
    "Bubble Bay",
    "Carp Creek",
    "Castaway Reef",
    "Chum Beach",
    "Clam Port",
    "Cod City",
    "Coral Key",
    "Deep Trench",
    "Driftwood",
    "Dune Point",
    "Eel Bend",
    "Filet Falls",
    "Fish Hook",
    "Flounder Town",
    "Gill Gulch",
    "Guppy Gap",
    "High Tide",
    "Kelp Bed",
    "Krill Bay",
    "Low Tide",
    "Lox Harbor",
    "Mackerel Heights",
    "Marlin Rock",
    "Minnow Bay",
    "Mussel Shoal",
    "Net-Drop Point",
    "Oyster Cove",
    "Perch Peak",
    "Plankton Place",
    "Pollock Rock",
    "Pond Scum",
    "Puffer Hill",
    "Red Tide",
    "Reef City",
    "Salty Flats",
    "Scaly Cove",
    "Seattle",
    "Seaweed",
    "Shark Key",
    "Shoal End",
    "Shrimp Port",
    "Starfish Slums",
    "Tacklebox",
    "Tidepool",
    "Trout Run",
    "Tuna Town",
    "Walleye",
]

TEAM_MASCOTS = [
    "Anarchists",
    "Bait Thieves",
    "Barnacle Boys",
    "Beauties",
    "Bottom Feeders",
    "Big Hitters",
    "Chums",
    "Clobberers",
    "Codfathers",
    "Crazies",
    "Drifts",
    "Eel Kissers",
    "Filet-o-Fishes",
    "Fin-atics",
    "Freaks",
    "Flops",
    "Fly-Fisher Phantoms",
    "Giggles",
    "Glub-Glub Gang",
    "Goofs",
    "Worms",
    "Hook Dodgers",
    "Jellies",
    "Kooks",
    "Thrills",
    "Bagel Toppers",
    "Tarter Saucers",
    "Maniacs",
    "Muddy Buddies",
    "Tanglers",
    "Off-the-Hookers",
    "Punks",
    "PowerFins",
    "Scoundrels",
    "Pop-Fly Puffers",
    "Rusty Hooks",
    "Squeezers",
    "Scallywags",
    "Clowns",
    "Ouchies",
    "Swillers",
    "Shark Bait",
    "Scampis",
    "Slimy Suckers",
    "Soggy Crackers",
    "Sponge Soakers",
    "Squid Kids",
    "Stinky Scales",
    "Tacklebox Trash",
    "Tuna Canners",
]
POSITIONS = ["P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF"]

@dataclass
class Team:
    name: str
    roster: dict[str, Player]

    def __post_init__(self):
        self.batting_order: cycle[Player] = self.generate_batting_order()

    def generate_batting_order(self) -> cycle[Player]:
        # Batting order is sorted by the sum of overall batting stats, descending. Not completely true to real-life baseball, but serviceable.
        return cycle(sorted(self.roster.values(), reverse=True, key=lambda player: sum(player.stats["Batting"].values())))

    @classmethod
    def generate_team(cls, seed: int | None=None) -> "Team":
        if seed is not None:
            random.seed(seed)

        roster: dict[str, Player] = dict()
        name = f"The {random.choice(TEAM_HOMES)} {random.choice(TEAM_MASCOTS)}"
        # Positions are randomly assigned for now
        for position in POSITIONS:
            roster[position] = Player.generate_player()

        return Team(name, roster)

