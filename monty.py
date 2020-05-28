#!/usr/bin/env python3
"""
Super simple Monty Hall problem simulator
"""
import getopt
import functools
import random
import sys

USAGE = "-t (number of trials)"

class Door:
    """
    Model a door with a number, whether it has a prize,
    whether the contestant originally chose it, or if the host
    revealed it (presumably as empty)
    """

    def __init__(self, number, opened=False, prize=False, guessed_originally=False):
        self.number = number
        self.opened = opened
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
        return f"Door number {self.number + 1}, opened={self.opened}," +\
            f"prize={self.prize}, guessed_originally={self.guessed_originally} " +\
            f"{self.winner_marker()}"


def choice_012():
    """ Make a random choice of 0, 1, or 2 """
    return random.randint(0, 2)


def make_door_set():
    """
    Set up three doors numbered 0,1,2 -- set one of them
    at random to have a prize
    """
    door_index = choice_012()
    doors = [Door(0), Door(1), Door(2)]
    doors[door_index].prize = True
    return doors


def print_door_set(door_set):
    """
    Nicely format door setup
    """
    print(functools.reduce(lambda a, b: f"{a}\n{b}", door_set))


def initial_choice(door_set):
    """
    Mark one of the doors at random as initially chosen by the
    contestant
    """
    choice = choice_012()
    door_set[choice].guessed_originally = True
    return choice

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
    return door.guessed_originally is False and door.opened is False


def original_choice(door):
    """
    Return True if this door was picked originally by the contestant """
    return door.guessed_originally is True


def host_remove(door_set):
    """
    Find the door or doors that the host can show as empty after the contestant
    makes their original choice, pick one at random, and mark it as "opened."
    """
    available_doors = list(filter(can_be_shown, door_set))
    index = 0
    if len(available_doors) > 1:
        index = random.randint(0, 1)
    door_set[available_doors[index].number].opened = True
    return available_doors[index].number

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

def run_trials(args):
    """
    Run a set of trials, collect data, print results
    """
    trials = 1000
    try:
        opts, _ = getopt.getopt(args, "ht:",
                                ["trials=", "help"])

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                sys.exit(1)
            elif opt in ("-t", "--trials"):
                trials = int(arg)

    except (ValueError, getopt.GetoptError):
        print(FULL_USAGE)
        sys.exit(2)

    for _ in range(trials):
        trial(results)
    print(f"Trials: {trials}")
    print(results)
    print(
        f'Switch choice winner probability: {(results["switch choice wins"]/trials)*100}%')

    if results["switch choice wins"] + results["original choice wins"] != trials:
        print("""Something really strange happened here that I
            obviously didn't have time to think about...""")

if __name__ == '__main__':
    FULL_USAGE = f'{__doc__}\nUsage: python3 {sys.argv[0]} {USAGE}'
    run_trials(sys.argv[1:])
