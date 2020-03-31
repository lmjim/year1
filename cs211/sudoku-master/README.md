# Sudoku

A solver for the classic puzzle, as a programming 
project for CIS 211 at University of Oregon. 

The project will have two phases.  In the first phase 
we implement constraint propagation to solve simple 
puzzles.  In the second phase we will add back-tracking
search to solve harder puzzles. 

We will use a model-view-controller organization to 
associate either a graphical display or a textual 
display with the game. 

# Note
'Naked single' and 'hidden single' should be implemented
week one. Week one you should turn in sdk_tile.py,
sdk_group.py, and sdk_board.py.

Week two turn in sdk_tile.py, sdk_board.py, sdk_group.py, and sdk_solver.py


#Note on self.groups
self.groups = [[row_0], [row_1],..., [row_8],[col_0], [col_1],..., [col_8],[block_0], [block_1],... [block_8]]


#Psuedocode
Pseudocode for recursive back-tracking search


Search (partial solution):

    if the partial solution is complete:
        return true
    if the partial solution can't possibly work:
        #If there are no candidates left for this tile
        return False
    for each possible next step:
        Apply the step to partial solution
        #Find tile with low number of candidates
        if Search(partial solution):
            return True
        else: 
            Undo the step
    # All the possible next steps have failed
    return False
    
    
OR:
    
Solve:

    propagate
    check if solved -> True/False?
    check if not consistent -> True/False?
    
    find a tile that doesn't have a value and has the least number of candidates
    
    save the board make a guess for the tile value
    check if the solve(board) is True/False?
        yes -> True
        no -> reset to save position