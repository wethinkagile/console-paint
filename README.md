The MIT License (MIT) <br>
Copyright (c) 2016 Stephan Kristyn (meshfields.de) <br>
http://meshfields.de/mit-license/ <br>

# Console Drawing Tool README

*With this tool you can draw on console in Linux. It uses Python.*

## Versions

### v0.1 
First fully working version

### v0.2
Moved all test calls over to test.py and fixed some tests

# Libraries

`unittest`: (for TDD) <br>
`sys`: (basic python interpreter methods)<br>
`regex`: (for user input sanitation)<br>

# Usage

*You can draw lines, rectangles and use bucket fills after you declared a canvas.*<br><br>

Start: `./main.py` <br>
Tests: `./test.py` <br>
Development: `methods.py` and `helpers.py` <br>


## Screenshot

    .....................
    .ooooooooooooooooooo.
    .ooooooooooooooooooo.
    .ooooooooooooooooooo.
    .oooxxxxxxxxxxxooooo.
    .oooxxxxxxxxxxxxxxxxx
    .oooxx        x-----.
    .oooxx        x-----.
    .oooxx        x-----.
    .oooxx        x-----.
    .oooxx        x-----.
    .oooxx        x-----.
    .oooxx        x-----.
    .oooxx        x-----.
    .oooxxxxxxxxxxx-----.
    .oooox--------------.
    .ooooxxxxxxxxxxxxxxxx
    .ooooooooooooooooooo.
    .ooooooooooooooooooo.
    .ooooooooooooooooooo.
    .....................
    [Line] [Canvas] [Rectangle] [Bucketfill] [Quit]


# Development

## Testing

This is what you want to see: <br>

    Unit Tests

    > Should plot a 5,9 Canvas
	> Should bucket fill a 20,4 Canvas with o
	> Should substitute tuples in pixels
	> Should Get Color Of Coordinates
	> Should substitute tuples in pixels
	> Should Set Color for a specific Coordinate
	> Should substitute tuples in pixels
	> Should Init Canvas Area 20,4 with ' '
	> Should get colored Canvas
	> Should get colored Rectangle
	> Should colorise the Coordinates
	> Should get Coordinates of Line

	10 Tests passed.

Also, in `methods.py`:<br>
`testDrawFourNeighbour()` remaining because of testing of global 'pixels'. (which can't be returned from recursive function for testing purposes)

## Design-Decisions and Trade-Offs

- Decided against nCurses or gnuPlot because of requirement to not use a library
- Emphasised on self-explanatory Code and helpful UX/UI
- DRY is not fully followed, since there wasn't enough time. The possibly introduced technical debt should be managed soon in order to scale-up.
- 1 remaining test in methods.py

## ToDo's: 

- Re-Write as Class for cleaner testing
- Then move 2 remaining Test to test.py
- Modularise further

Questions and Feedback to nottinhill@ecomail.at.