The MIT License (MIT) <br>
Copyright (c) 2016 Stephan Kristyn (meshfields.de) <br>
http://meshfields.de/mit-license/ <br>

# Console Drawing Tool README

*With this tool you can draw on console in Linux. It uses Python.*

## Versions

- v0.1: First Fully Working Version

# Libraries

- unittest (for TDD)
- sys (for basic tools)
- regex (for input handling)

# Usage

*You can draw lines, rectangles and use bucket fills after you declared a canvas.*<br><br>

Start: ./main.py <br>
Tests: ./test.py <br>
Development: methods.py and helpers.py <br>


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


# Design-Decisions and Trade-Offs

- Decided against nCurses or gnuPlot because of requirement to not use a library
- Emphasised on self-explanatory Code and helpful UX/UI
- DRY is not fully followed, since there wasn't enough time. The introduced technical debt should be handled in the ToDo's below.

## ToDo's: 

- Re-Write as Class for cleaner testing
- Then move 2 remaining Test to test.py
- Modularise further

Questions and Feedback to nottinhill@ecomail.at.