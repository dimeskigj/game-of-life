<h4>Game of Life</h4>

This is my implementation of the Game of Life. The program saves a .gif output. 
There are initial configurations in starters.py that you can try out.

The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
It is a zero-player game, meaning that its evolution is determined by its initial state,
requiring no further input.
One interacts with the Game of Life by creating an initial configuration and observing how it evolves.
It is Turing complete and can simulate a universal constructor or any other Turing machine.

Rules:
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

src: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

<h3>Demo</h3>
<img src='output.gif'>