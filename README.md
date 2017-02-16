## Task ##

Your task is to implement the rules of Conway's Game of Life as explained in the document statement. You can use the code skeleton provided here as a starting point. In that case, implement the `evolve` method in `Life.py`. Feel free to make changes to the code that help you capture all the rules of the game. You can add more tests to `testlife.py` to verify the correctness of your code.


## Prerequisites ##
* Your favorite text editor
* Install [nosetests](http://nose.readthedocs.io/en/latest/)

## How to run the tests ##
In a command line, navigate to this directory and just run `nosetests -v`

## Assumptions ##

From the supplied specification, I assumed a TDD approach.

From the intial test case, I decided to use a 3x3 board size approach.

STATE = [[0,0,0],
         [0,0,0],
         [0,0,0]]

I then implemented the logic using the 4 universal Game of Life rules:

    1) Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    2) Any live cell with two or three live neighbours lives on to the next generation.
    3) Any live cell with more than three live neighbours dies, as if by overpopulation.
    4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

I then modified the code to make use of the Class based aporoached, initialising the class with the STATE and SIZE of the board.

STATE must be the same size as the SIZE paramter or the simulation will not run.