"""
Overall control for 2048 clone 512.  Coordinates
model and view and implements controller
functionality by interpreting keyboard input

Author: Lily Jim
Extra Credit: Chance of 4 Tile
Extra Credit: Score like 2048
Extra Credit: Disable ineffective moves
"""
import model
import view
import keypress


def main():
    # Set up model component
    grid = model.Grid()
    # Set up view component
    game_view = view.GameView(600, 600)
    grid_view = view.GameGrid(game_view, len(grid.tiles))
    grid.add_listener(grid_view)
    # Handle control component responsibility here
    commands = keypress.Command(game_view)
    grid.place_tile()

    # Game continues until there is no empty
    # space for a tile
    while grid.find_empty():
        cmd = commands.next()
        if cmd == keypress.LEFT:
            grid.left()
        elif cmd == keypress.RIGHT:
            grid.right()
        elif cmd == keypress.UP:
            grid.up()
        elif cmd == keypress.DOWN:
            grid.down()
        else:
            assert cmd == keypress.UNMAPPED
        if cmd == keypress.UNMAPPED:
            pass  # If an unmapped key is pressed don't do anything-----------------------------------------Extra Credit
        elif grid.movement[0]:  # If a movement happened, grid.movement[0] will be True---------------------Extra Credit
            grid.place_tile()  # A new tile is placed only if a movement happened---------------------------Extra Credit

    game_view.lose(grid.score())


if __name__ == "__main__":
    main()
