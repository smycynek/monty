import random
import functools

class Door:
  def __init__(self, number, open=False, prize=False, guessed=False):
    self.number = number
    self.open = open
    self.prize = prize
    self.guessed = guessed
  def __str__(self):
    return f"Door number {self.number}, open={self.open}, prize={self.prize}, guessed={self.guessed}"

def choice_012():
    return random.randint(0,2) 

def make_door_set():
  door_index = choice_012()
  doors = [Door(0), Door(1), Door(2)]
  doors[door_index].prize = True
  return doors

def print_door_set(door_set):
    print (functools.reduce(lambda a,b : f"{a}\n{b}",door_set)) 

def initial_choice(door_set):
    choice = choice_012()
    door_set[choice].guessed = True

def can_be_shown(door):
    return door.guessed is False and door.prize is False

def valid_alternate_choice(door):
    return door.guessed is False and door.open is False

def original_choice(door):
    return door.guessed is True

def host_remove(door_set):
    available_doors = list(filter(can_be_shown, door_set))
    index = 0
    if len(available_doors) > 1:
        index = random.randint(0,1)
    door_set[available_doors[index].number].open = True

def get_alternate_choice(door_set):
    available_doors = list(filter(valid_alternate_choice, door_set))
    return available_doors[0]

def get_original_choice(door_set):
    available_doors = list(filter(original_choice, door_set))
    return available_doors[0]

data = {"original choice wins":0, "switch choice wins":0}
def trial():
  door_set = make_door_set()
  initial_choice(door_set)
  host_remove(door_set)
  alternate = get_alternate_choice(door_set)
  original = get_original_choice(door_set)
  if alternate.prize is True:
      data["switch choice wins"] +=1
  if original.prize is True:
      data["original choice wins"] +=1

num_trials = 1000
for _ in range(num_trials):
    trial()
print(f"Trials: {num_trials}")
print(data)

