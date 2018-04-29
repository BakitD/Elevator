# Elevator


### Installation

> `git clone git@github.com:BakitD/Elevator.git`

### Run

> `cd Elevator`


To run program

> `python src/main.py -floors FLOORS -height HEIGHT -speed SPEED -wait_time`

Example

> `python src/main.py -floors=5 -height=2 -speed=1.2 -wait_time=3`

To get information about arguments format

> `python src/main.py -h`


To run tests

> `python -m unittest -v tests/*.py`


### Syntax of the commands

To call elevator input

> `call FLOOR_NUM`

To go to the specific floor input

> `go FLOOR_NUM`

FLOOR_NUM - integer


### Output example

```
>> call 0
Elevator opened doors on the 0 floor
Waiting with opened doors !
Waiting with opened doors !
Waiting with opened doors !
Doors are closed !
>> call 4
Elevator started from 0 floor
Elevator passes 1 floor
Elevator passes 2 floor
Elevator passes 3 floor
Elevator arrived on the 4 floor
Elevator opened doors on the 4 floor
Waiting with opened doors !
Waiting with opened doors !
Waiting with opened doors !
Doors are closed !
>> go 1
Elevator started from 4 floor
Elevator passes 3 floor
Elevator passes 2 floor
Elevator arrived on the 1 floor
Elevator opened doors on the 1 floor
Waiting with opened doors !
Waiting with opened doors !
Waiting with opened doors !
Doors are closed !
>> 
```