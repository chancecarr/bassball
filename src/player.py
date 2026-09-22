from dataclasses import dataclass
import random

FIRST_NAMES: list[str] = [
    "Salmon",
    "Gills",
    "Finley",
    "Cod",
    "Bass",
    "Ray",
    "Mako",
    "Skip",
    "Roe",
    "Bait",
    "Pike",
    "Hook",
    "Rod",
    "Gilligan",
    "Finnegan",
    "Scales",
    "Mackerel",
    "Pollock",
    "Guppy",
    "Chum",
    "Slippery",
    "Salty",
    "Bubbles",
    "Barnacle",
    "Briny",
    "Squishy",
    "Splash",
    "Floppy",
    "Glub",
    "Nibbles",
    "Muddy",
    "Cheeky",
    "Slimy",
    "Wriggly",
    "Spiny",
    "Crabby",
    "Chippy",
    "Zippy",
    "Bouncy",
    "Fiery",
    "Anchovy",
    "Tetra",
    "Minnow",
    "Haddock",
    "Herring",
    "Trout",
    "Kelp",
    "Coral",
    "Shoal",
    "Reef",
]

LAST_NAMES: list[str] = [
    "McFish",
    "O'Gill",
    "DeLaBass",
    "VonTrout",
    "Saint-Salmon",
    "FitzFin",
    "VanDock",
    "MacRoe",
    "O'Scales",
    "LePike",
    "Snapper",
    "Flounder",
    "Halibut",
    "Sturgeon",
    "Barracuda",
    "Grouper",
    "Marlin",
    "Swordsman",
    "Catfish",
    "Walleye",
    "Mullet",
    "Puffer",
    "Tarpon",
    "Sculpin",
    "Bluegill",
    "Baitmaster",
    "Trawler",
    "Castman",
    "Chum bucket",
    "Shipwreck",
    "Tidepool",
    "Driftwood",
    "Reefboard",
    "Breakwater",
    "Sandbar",
    "Seabed",
    "Kelpmoss",
    "Harpooner",
    "Netmaker",
    "Dockside",
    "Finbender",
    "Scale-Striker",
    "Gill-Smasher",
    "Catch-of-the-Day",
    "Swimmer",
    "Deep-Diver",
    "Bottom-Feeder",
    "Mud-Skipper",
    "Splash-Down",
    "High-Tide",
]

STATS: dict[str, list[str]] = {
    "Batting": ["Contact", "Placement"], 
    "Running": ["Speed", "Stealing"], 
    "Pitching": ["Arm", "Technique"], 
    "Fielding": ["Catching", "Sense"]
}

@dataclass
class Player:
    first_name: str
    last_name: str
    stats: dict[str, dict[str, int]]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def generate_player(cls, seed: int | None) -> "Player":
        if seed is not None:
            random.seed(seed)

        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        stats = Player.generate_stats()
        return Player(first_name, last_name, stats)

    @classmethod
    def generate_stats(cls) -> dict[str, dict[str, int]]:
        stats: dict[str, dict[str, int]] = dict()

        # Magic numbers in use here. I'm targeting an average of 70 across a player's skill stats, with reasonable variation due to natural talent.
        overall_pts: int = int(random.gauss(560, 40))
        stat_distribution: list[int] = Player.distribute_with_min(overall_pts, 8)

        for category in STATS:
            stats[category] = {}
            for skill in STATS[category]:
                stats[category][skill] = stat_distribution.pop()

        return stats

    @classmethod
    def distribute_with_min(cls, total, num_attributes):
        # Players in Bassball have a minimum base level of athleticism across their stats
        min_val: int = (total // num_attributes) // 2
        free_points: int = total - (min_val * num_attributes)

        # Points distributed using stars and bars algorithm
        cuts: list[int] = sorted(random.sample(range(1, free_points), num_attributes - 1))
        distributed: list[int] = [a - b for a, b in zip(cuts + [free_points], [0] + cuts)]

        return [val + min_val for val in distributed]