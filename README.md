# sudoku_solver
let's make the computers capable of solving Sudoku puzzles

## solvers: 
All solvers follow the same algorithm written in different languages. The algorithm is a simple backtrack with a few improvements for decreasing computation time. 

The solvers work for any square Sudoku puzzle, whether it be 9\*9, 16\*16, or so on. 

## tester:
The tester is written in python and bash. It contains a folder named "inputs" which stores a few Sudoku puzzles. Outputs aren't stored because a Sudoku puzzle may have multiple solutions. So there is a python program, `check_outputs.py`, which verify the proposed solutions by solvers. 

You can run the tests for both python and cpp by passing "cpp" or "python" to the script(e.g. `./run_tests.sh python`)

