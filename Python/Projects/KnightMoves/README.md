# ♞  Valid Knight Moves

## Overview

You are given `(x, y)` coordinates of a `2D array` which represents the position of a knight on a 8x8 chessboard. 


### ⚙️ Task

Convert these given coordinate into [algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)), and return a `mixed-tuple` which contains:
1. a `str` of the given coordinates converted into `algebraic noation`, and
2. a sorted `list`, in ascending order, of all legal knight moves in `algebraic notation` from this given position. 

### Background Information
#### What is Algebraic Notation?

`Algebraic Notation` is the standard method for recording and describing the moves in a chess game. It is based on a system of coordinates that uniquely identify each square on the chessboard. 

#### Naming Squares
Each square of the chessboard is identified by a unique coordinate pair such as a (`letter` and a `number`), from White's point of view. The vertical columns of squares, called `"files"`, are labeled `"a"` through `"h"` from White's left (the queenside) to right (the kingside). The horizontal rows of squares, called `"ranks"`, are numbered `"1"` to `"8"` starting from White's side of the board. Thus each square has a unique identification of `file letter` followed by `rank number` (*See screenshot below for example*).

![image](https://user-images.githubusercontent.com/72005563/173207879-239c81f2-45d7-400f-8bce-3f15d60d354b.png)

#### How a Knight Moves

The knight moves in an “L-shape” pattern. They can move two squares in any direction vertically followed by one square horizontally, or two squares in any direction horizontally followed by one square vertically (*see screenshot below for example*).

![image](https://user-images.githubusercontent.com/72005563/173208265-25dfff32-f9d3-4c09-b4df-c97eae85beef.png)



<!-- ![image](https://user-images.githubusercontent.com/72005563/173203984-8ea4b13d-b5e8-41a2-bfa8-30ef10b887bf.png)
For example, in the sreenshot below, the position of White's knight is designated as `"e4"`.  

--> 


Now that you have some background information let's see an example.

## Example  

#### Input 

```python
(4, 4)
```
#### Output

```python
('e4', ['c3', 'c5', 'd2', 'd6', 'f2', 'f6', 'g3', 'g5'])
```

## Explaination
The coordinates `(4, 4)` represent the `row` and `column` of a 2D array which corrolates to `"e4"` on a chess board (*see screenshot below*). This represents the position of a knight on a 8x8 chess board. Therefore, `"e4"` is the first element of the output, and the datatype should be `str`.


![image](https://user-images.githubusercontent.com/72005563/173206544-3e50972f-4a89-40f2-af28-0b2043b1792f.png)

The second element of the output is a list of all legal moves that the knight can make, from this given position, in algebraic notation, in ascending order which would be `['c3', 'c5', 'd2', 'd6', 'f2', 'f6', 'g3', 'g5']`. 


Therefore, the complete output is:

```python
('e4', ['c3', 'c5', 'd2', 'd6', 'f2', 'f6', 'g3', 'g5'])
```

See screenshot below for a visual cue of these squares hightlighted in red.

![image](https://user-images.githubusercontent.com/72005563/173208524-d564a940-ab45-443f-bf85-50f53fa08d2c.png)


## Code


```python

#!/usr/bin/env python3
"""
created: 2022-06-11 02:55:38
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Legal Knight Moves
metadoc: 
license: None
"""


def valid_knight_moves(coordinates: tuple) -> tuple[str:list]:
    positions = {
        (0, 0): {'a8': ['b6', 'c7']},
        (0, 1): {'b8': ['a6', 'c6', 'd7']},
        (0, 2): {'c8': ['a7', 'b6', 'd6', 'e7']},
        (0, 3): {'d8': ['b7', 'c6', 'e6', 'f7']},
        (0, 4): {'e8': ['c7', 'd6', 'f6', 'g7']},
        (0, 5): {'f8': ['d7', 'e6', 'g6', 'h7']},
        (0, 6): {'g8': ['e7', 'f6', 'h6']},
        (0, 7): {'h8': ['f7', 'g6']},
        (1, 0): {'a7': ['c6', 'c8', 'b5']},
        (1, 1): {'b7': ['a5', 'c5', 'd6', 'd8']},
        (1, 2): {'c7': ['a6', 'a8', 'b5', 'd5', 'e6', 'e8']},
        (1, 3): {'d7': ['b6', 'b8', 'c5', 'e5', 'f6', 'f8']},
        (1, 4): {'e7': ['c6', 'c8', 'd5', 'f5', 'g6', 'g8']},
        (1, 5): {'f7': ['d8', 'd6', 'e5', 'g5', 'h6', 'h8']},
        (1, 6): {'g7': ['e6', 'e8', 'f5', 'h5']},
        (1, 7): {'h7': ['f6', 'f8', 'g5']},
        (2, 0): {'a6': ['b4', 'b8', 'c5', 'c7']},
        (2, 1): {'b6': ['a4', 'a8', 'c4', 'c8', 'd5', 'd7']},
        (2, 2): {'c6': ['a5', 'a7', 'b4', 'b8', 'd4', 'd8', 'e5', 'e7']},
        (2, 3): {'d6': ['b5', 'b7', 'c4', 'c8', 'e4', 'e8', 'f5', 'f7']},
        (2, 4): {'e6': ['c5', 'c7', 'd4', 'd8', 'f4', 'f8', 'g5', 'g7']},
        (2, 5): {'f6': ['d5', 'd7', 'e4', 'e8', 'g4', 'g8', 'h5', 'h7']},
        (2, 6): {'g6': ['e5', 'e7', 'f4', 'f8', 'h4', 'h8']},
        (2, 7): {'h6': ['f5', 'f7', 'g4', 'g8']},
        (3, 0): {'a5': ['b3', 'b7', 'c4', 'c6']},
        (3, 1): {'b5': ['a3', 'a7', 'c3', 'c7', 'd4', 'd6']},
        (3, 2): {'c5': ['a4', 'a6', 'b3', 'b7', 'd3', 'd7', 'e4', 'e6']},
        (3, 3): {'d5': ['b4', 'b6', 'c3', 'c7', 'e3', 'e7', 'f4', 'f6']},
        (3, 4): {'e5': ['c4', 'c6', 'd3', 'd7', 'f3', 'f7', 'g4', 'g6']},
        (3, 5): {'f5': ['d4', 'd6', 'e3', 'e7', 'g3', 'g7', 'h4', 'h6']},
        (3, 6): {'g5': ['e4', 'e6', 'f3', 'f7', 'h3', 'h7']},
        (3, 7): {'h5': ['f4', 'f6', 'g3', 'g7']},
        (4, 0): {'a4': ['b2', 'b6', 'c5', 'c3']},
        (4, 1): {'b4': ['a2', 'a6', 'c2', 'c6', 'd5', 'd3']},
        (4, 2): {'c4': ['a3', 'a5', 'b2', 'b6', 'd2', 'd6', 'e3', 'e5']},
        (4, 3): {'d4': ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']},
        (4, 4): {'e4': ['c3', 'c5', 'd2', 'd6', 'f2', 'f6', 'g3', 'g5']},
        (4, 5): {'f4': ['d3', 'd5', 'e2', 'e6', 'g2', 'g6', 'h3', 'h5']},
        (4, 6): {'g4': ['e3', 'e5', 'f2', 'f6', 'h2', 'h6']},
        (4, 7): {'h4': ['f3', 'f5', 'g2', 'g6']},
        (4, 0): {'a3': ['b1', 'b5', 'c4', 'c2']},
        (5, 1): {'b3': ['a1', 'a5', 'c1', 'c5', 'd2', 'd4']},
        (5, 2): {'c3': ['a2', 'a4', 'b1', 'b5', 'd1', 'd5', 'e2', 'e4']},
        (5, 3): {'d3': ['b2', 'b4', 'c1', 'c5', 'e1', 'e5', 'f2', 'f4']},
        (5, 4): {'e3': ['d1', 'c2', 'c4', 'd5', 'f5', 'g2', 'f1', 'g4']},
        (5, 5): {'f3': ['d2', 'd4', 'e1', 'e5', 'g1', 'g5', 'h2', 'h4']},
        (5, 6): {'g3': ['e2', 'e4', 'f1', 'f5', 'h1', 'h5']},
        (5, 7): {'h3': ['f2', 'g1', 'f4', 'g5']},
        (6, 0): {'a2': ['a3', 'c3', 'd2']},
        (6, 1): {'b2': ['a4', 'c4', 'd1', 'd3']},
        (6, 2): {'c2': ['a1', 'a3', 'b4', 'd4', 'e1', 'e3']},
        (6, 3): {'d2': ['b1', 'b3', 'c4', 'e4', 'f3', 'f1']},
        (6, 4): {'e2': ['c1', 'c3', 'd4', 'f4', 'g1', 'g3']},
        (6, 5): {'f2': ['d1', 'd3', 'e4', 'g4', 'h1', 'h3']},
        (6, 6): {'g2': ['e1', 'e3', 'f4', 'h4']},
        (6, 7): {'h2': ['f1', 'f3', 'g4']},
        (7, 0): {'a1': ['b3', 'f2']},
        (7, 1): {'b1': ['b3', 'c3', 'd2']},
        (7, 2): {'c1': ['a2', 'b3', 'd3', 'e2']},
        (7, 3): {'d1': ['b2', 'c3', 'e4', 'f2']},
        (7, 4): {'e1': ['c2', 'd3', 'f3', 'g2']},
        (7, 5): {'f1': ['d2', 'e3', 'g3', 'h2']},
        (7, 6): {'g1': ['e2', 'f3', 'h3']},
        (7, 7): {'h1': ['f2', 'g3']},
    }
    item = positions.get(coordinates)
    starting_position = item.keys()
    all_legal_moves = item.values()
    return list(starting_position)[0], list(all_legal_moves)[0]

```


