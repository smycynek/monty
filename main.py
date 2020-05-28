"""
Super simple Monty Hall problem simulator
"""

import random
import functools

NUM_TRIALS = 100000 # Adjust as you like

class Door:
    """
    Model a door with a number, whether it has a prize,
    whether the contestant originally chose it, or if the host
    revealed it (presumably as empty)
    """

    def __init__(self, number, open=False, prize=False, guessed_originally=False):
        self.number = number
        self.open = open
        self.prize = prize
        self.guessed_originally = guessed_originally

    def winner_marker(self):
        """
        Return a small annotation if the door is a winner and which choice, the 
        alternate or original, would have chosen it.
        """
        if self.guessed_originally and self.prize:
            return "(Original choice wins)"
        if self.prize:
            return "(Switch choice wins)"
        return ""

    def __str__(self):
        return f"Door number {self.number}, open={self.open}, prize={self.prize}, guessed_originally={self.guessed_originally} {self.winner_marker()}"


def choice_012():
    """ Make a random choice of 0, 1, or 2 """
    return random.randint(0, 2)


def make_door_set():
    """ 
    Set up thee doors numbered 0,1,2 -- set one of them
    at random to have a prize 
    """
    door_index = choice_012()
    doors = [Door(0), Door(1), Door(2)]
    doors[door_index].prize = True
    return doors


def print_door_set(door_set):
    print(functools.reduce(lambda a, b: f"{a}\n{b}", door_set))


def initial_choice(door_set):
    """ 
    Mark one of the doors at random as initially chosen by the
    contestant
    """
    choice = choice_012()
    door_set[choice].guessed_originally = True


def can_be_shown(door):
    """
    Return True if a door was not chosen originally and does not have
    a prize 
    (These are the door(s) that the host can open, revealing
    an empty door, after the
    contestant makes their first choice)
    """
    return door.guessed_originally is False and door.prize is False


def valid_alternate_choice(door):
    """
    Return True if a door was not chosen originally and was not opened
    by the host.  This door is the "switch option" the contestant could choose
    to pick later.
    """
    return door.guessed_originally is False and door.open is False


def original_choice(door):
    """
    Return True if this door was picked originally by the contestant """
    return door.guessed_originally is True


def host_remove(door_set):
    """
    Find the door or doors that the host can show as empty after the contestant
    makes their original choice, pick one at random, and mark it as "open."
    """
    available_doors = list(filter(can_be_shown, door_set))
    index = 0
    if len(available_doors) > 1:
        index = random.randint(0, 1)
    door_set[available_doors[index].number].open = True


def get_alternate_choice(door_set):
    """
    Get the door that the contestant may optionally switch to after the
    reveal of an empty door.
    """
    available_doors = list(filter(valid_alternate_choice, door_set))
    return available_doors[0]


def get_original_choice(door_set):
    """
    Get the door that the contestant chose originally
    """
    available_doors = list(filter(original_choice, door_set))
    return available_doors[0]


results = {"original choice wins": 0, "switch choice wins": 0}


def trial(data):
    """
    Set up 3 doors, one with a prize at random.

    Have the contestant pick one of the doors at random.

    Have the host show one of the unpicked doors without a prize
    as empty

    Analyze which choice was the winner, the original or the switch, 
    and record the results
    """
    door_set = make_door_set()
    initial_choice(door_set)
    host_remove(door_set)
    alternate = get_alternate_choice(door_set)
    original = get_original_choice(door_set)
    print_door_set(door_set)
    print("-------")
    if alternate.prize is True:
        data["switch choice wins"] += 1
    if original.prize is True:
        data["original choice wins"] += 1


for _ in range(NUM_TRIALS):
    trial(results)
print(f"Trials: {NUM_TRIALS}")
print(results)
print(
    f'Switch choice winner probability: {(results["switch choice wins"]/NUM_TRIALS)*100}%')

if results["switch choice wins"] + results["original choice wins"] != NUM_TRIALS:
    print("Something really strange happened here that I obviously didn't have time to think about...")

