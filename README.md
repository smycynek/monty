# monty
A quick monty-hall problem simulator

Every once in a while, the topic of the famous monty-hall
problem comes up (https://en.wikipedia.org/wiki/Monty_Hall_problem),
and I can reason through why you should switch doors if I sit down
for minute -- then I forget it an hour later :)  

So, I made a simulation to show the process of:
* The host setting up the doors with the prize
* The contestant making an initial guess
* The host opening a door that has no prize that the guest didn't choose
* The host asking if the contestant wants to switch doors
* Whether or not the prize is behind the original guess or the alternate

## Usage...
```
python3 monty.py

# output...
...
...
...
Trials: 1000
{'original choice wins': 309, 'switch choice wins': 691}
Switch choice winner probability: 69.1% # will vary
```
