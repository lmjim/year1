>>> tiles = []
>>> for row in range(4):
	columns = []
	for col in range(4):
		columns.append(None)
	tiles.append(columns)

	
>>> print(tiles)
[[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
>>> rep = []
>>> for row in tiles:
        value_list = []
        for tile in row:
            if tile is None:
                value_list.append(0)
            else:
                value_list.append(tile.value)
        rep.append(value_list)

            
>>> print(rep)
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
>>> tiles = []
>>> for row in range(4):
        row_tiles = []
        for col in range(4):
            if rep[row][col] == 0:
                row_tiles.append(None)
            else:
                val = rep[row][col]
                tile = Tile(self, row, col, value=val)
                row_tiles.append(tile)
                #self.notify("New", data={"tile": tile})
        tiles.append(row_tiles)


>>> print(tiles)
[[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
>>> print(row_tiles)
[None, None, None, None]





