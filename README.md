# monty

* Version 1.0.1

* Copyright 2020 Steven Mycynek

* A quick Monty Hall problem simulator - python 3.7

Every once in a while, the topic of the famous Monty Hall
problem comes up (https://en.wikipedia.org/wiki/Monty_Hall_problem),
and I can reason through why you should switch doors if I sit down
for minute to think.  Then I forget the reasoning an hour later :)  

So, I made a simulation to show the process of:

* The host setting up the doors with the prize
* The contestant making an initial guess
* The host opening a door that has no prize that the guest didn't choose
* The host asking if the contestant wants to switch doors
* Whether the prize is behind the original guess or the alternate

This simulation is then run 1000 times, and the results are summarized.

Have fun!

## Usage

```
python3 monty.py
python3 monty.py -t 2000 # 2000 trials, etc.

# output...
...
... other 998 trials...
-------
Door number 1: opened=False, prize=False, guessed_originally=True
Door number 2: opened=True, prize=False, guessed_originally=False
Door number 3: opened=False, prize=True, guessed_originally=False (Switch choice wins)
-------
Door number 1: opened=False, prize=True, guessed_originally=True (Original choice wins)
Door number 2: opened=True, prize=False, guessed_originally=False
Door number 3: opened=False, prize=False, guessed_originally=False
-------
Trials: 1000
{'original choice wins': 309, 'switch choice wins': 691}
Switch choice winner probability: 69.1% # will vary
```
