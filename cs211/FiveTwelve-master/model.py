"""
The game state and logic (model component) of 512,
a game based on 2048 with a few changes.
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event
notifications to trigger view updates.

Author: Lily Jim
Extra Credit: Chance of 4 Tile
Extra Credit: Score like 2048
Extra Credit: Disable ineffective moves
"""

import random

# Configuration constants
GRID_SIZE = 4


class Game_Element(object):
    """Base class for game elements, especially to support
    depiction through Model-View-Controller.
    """

    def __init__(self):
        """Each game element can have zero or more listeners.
        Listeners are view components that react to notifications.
        """
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def notify(self, event, data={}):
        """Instead of handling graphics in the model component,
        we notify view components of each significant event and let
        the view component decide how to adjust the graphical view.
        When additional information must be packaged with an event,
        it goes in the optional 'data' parameter.
        """
        for listener in self.listeners:
            listener.notify(event, self, data)


class Grid(Game_Element):
    """The game grid."""
    total_score = 0  # Keeps track of total score, gets updated each time a tile is merged------------------Extra Credit

    def __init__(self):
        super().__init__()
        self.rows = GRID_SIZE
        self.cols = GRID_SIZE
        self.movement = []  # Keep track if a movement happened or not--------------------------------------Extra Credit
        # Initialize tiles as a matrix of "None" (empty)
        self.tiles = []
        for row in range(self.rows):
            columns = []
            for col in range(self.cols):
                columns.append(None)
            self.tiles.append(columns)

    def __str__(self):
        rep = []
        for row in self.tiles:
            labels = [str(x) for x in row]
            rep.append("[{}]".format(",".join(labels)))
        return "[{}]".format(",".join(rep))

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def as_list(self):
        """Grid as a list of lists of numbers; for serialization
        and especially for testing.
        """
        rep = []
        for row in self.tiles:
            value_list = []
            for tile in row:
                if tile is None:
                    value_list.append(0)
                else:
                    value_list.append(tile.value)
            rep.append(value_list)
        return rep

    def set_tiles(self, rep):
        """Set tiles to a saved configuration, which must
        have the correct dimensions (e.g., 4 rows of 4 columns
        if grid size is 4).
        """
        self.tiles = []
        for row in range(self.rows):
            row_tiles = []
            for col in range(self.cols):
                if rep[row][col] == 0:
                    row_tiles.append(None)
                else:
                    val = rep[row][col]
                    tile = Tile(self, row, col, value=val)
                    row_tiles.append(tile)
                    self.notify("New", data={"tile": tile})
            self.tiles.append(row_tiles)

    def score(self):
        """The score is the total of every merged value"""
        return Grid.total_score  # When game_manager.py calls grid.score() at the end of the game return the total score
        # --------------------------------------------------------------------------------------------------Extra Credit

    # Game logic
    def find_empty(self):
        """Find an empty cell (where we can drop a new tile).
        Returns a row,col pair or None to indicate there are no
        empty spots in the grid.
        """
        candidates = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.tiles[row][col] is None:
                    pos = (row, col)
                    candidates.append(pos)
        if candidates == []:
            return None
        return random.choice(candidates)

    def place_tile(self):
        """Place a new tile somewhere on the grid.
        New value is 2 or 4. There is a 10% chance of
        getting a 4, like in 2048.
        """
        spot = self.find_empty()
        assert(spot)
        row, col = spot
        choices = (2, 2, 2, 2, 2, 2, 2, 2, 2, 4)  # New tile value has a 1/10 chance of being 4-------------Extra Credit
        value = random.choice(choices)  # Randomly choose a spot in choices, giving 4 a 10% chance----------Extra Credit
        tile = Tile(self, row, col, value)  # Set the new tile value to the randomly selected value---------Extra Credit
        self.tiles[row][col] = tile
        self.notify("New", data={"tile": tile})

    def moved(self):
        """Determines if anything moved by looking for 'True' in self.movement
        if 'True' does not appear, no movement happened"""
        for i in self.movement:
            if self.movement[i]:
                self.movement = [True]  # At least one tile moved-------------------------------------------Extra Credit
                break
            elif i != len(self.movement):
                pass
            else:
                self.movement = [False]  # No tiles moved---------------------------------------------------Extra Credit

    def left(self):
        """Slide tiles to the left"""
        self.movement = [False]  # Start with no movement---Extra Credit
        movement_vector = (0, -1)
        for row in self.tiles:
            for tile in row:
                if tile:
                    tile.slide(self, movement_vector)
        self.moved()  # Check if anything moved----Extra Credit

    def right(self):
        """Slide tiles to the right"""
        self.movement = [False]  # Start with no movement---Extra Credit
        movement_vector = (0, 1)
        for row in self.tiles:
            for tile in reversed(row):
                if tile:
                    tile.slide(self, movement_vector)
        self.moved()  # Check if anything moved---Extra Credit

    def up(self):
        """Slide tiles up"""
        self.movement = [False]  # Start with no movement---Extra Credit
        movement_vector = (-1, 0)
        for row in self.tiles:
            for tile in row:
                if tile:
                    tile.slide(self, movement_vector)
        self.moved()  # Check if anything moved---Extra Credit

    def down(self):
        """Slide tiles down"""
        self.movement = [False]  # Start with no movement---Extra Credit
        movement_vector = (1, 0)
        for row in reversed(self.tiles):
            for tile in row:
                if tile:
                    tile.slide(self, movement_vector)
        self.moved()  # Check if anything moved---Extra Credit


class Tile(Game_Element):
    """A slide-y numbered thing."""

    def __init__(self, grid, row, col, value=2):
        super().__init__()
        self.grid = grid
        self.row = row
        self.col = col
        self.value = value

    def slide(self, grid, movement_vector):
        """Slide the tile in given direction
        Note we must update grid as well as
        tile. Movement vector should be a
        pair (dx, dy) where each of dx, dy is
        -1, 0, or 1.  For example, left is (0, -1).
        """
        dx, dy = movement_vector
        row, col = self.row, self.col
        while True:
            trial_x = row + dx
            trial_y = col + dy
            if not self.grid.in_bounds(trial_x, trial_y):
                # Reached edge of board
                break
            if not self.grid.tiles[trial_x][trial_y]:
                # Slide over empty space
                row, col = trial_x, trial_y
                self.move(self.grid, row, col)
                grid.movement.append(True)  # Note that a movement did happen-------------------------------Extra Credit
            elif self.grid.tiles[trial_x][trial_y].value == self.value:
                # Matching tile, merge and continue
                row, col = trial_x, trial_y
                self.merge(self.grid.tiles[trial_x][trial_y])
                self.move(self.grid, row, col)
                grid.movement.append(True)  # Note that a movement did happen-------------------------------Extra Credit
            else:
                # Reached tile with a different value
                break

    def move(self, grid, row, col):
        """Update position"""
        self.grid.tiles[self.row][self.col] = None
        self.row = row
        self.col = col
        self.grid.tiles[row][col] = self
        self.notify("Update")

    def merge(self, other):
        """Let this tile be the sum of it and another
        and update the total score"""
        self.value = self.value + other.value
        other.remove()
        self.notify("Update")
        Grid.total_score += self.value  # Add value of merged tile to total score---------------------------Extra Credit

    def remove(self):
        self.notify("Remove")

    def __str__(self):
        return str(self.value)
