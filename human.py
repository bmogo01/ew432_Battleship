import ship, game_board, sprites
from random import randint
from typing import List, Tuple, Optional


class Human:
    """ A human player"""

    def __init__(self):

        # list of ship objects
        self._my_ships: List[ship.Ship] = []
        # list of (row,col) coordinates
        self._my_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates
        self._my_hits: List[Tuple[int, int]] = []
        # list of ship objects
        self._sunk_ships: List[ship.Ship] = []
        # list of (row,col) coordinates
        self._their_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates
        self._their_hits: List[Tuple[int, int]] = []

        # the board matrix is a 10x10 structure with
        # pointers to ship objects. Initialize to all
        # None values- no ships are on the board
        self._board_matrix: List[List[Optional[ship.Ship]]] = [[None] * 10 for _ in range(10)]

        # set to True if all opponent's ships are sunk
        self.complete: bool = False

    def initialize(self):
        """ Create a valid ship layout
        This function populates
        _my_ships and _board_matrix

        Ship Type  | Length
        -----------|-------
        Carrier    |   5
        Battleship |   4
        Cruiser    |   3
        Submarine  |   3
        Destroyer  |   2

        * the ship type is just FYI, it is not used in the game *
        """

        for ship_length in [5, 4, 3, 3, 2]:
            # --------- BEGIN YOUR CODE ----------
            validPlac = False
            while validPlac is False:
                # 1.) create ship of the given length at a random (row,col)
                #     position either horizontal or vertical
                orient = randint(0, 1)
                if orient == 1:
                    row = randint(0, 10-ship_length)
                    col = randint(0,9)
                else:
                    row = randint(0,9)
                    col = randint(0, 10-ship_length)

                my_ship = ship.Ship(ship_length, row, col, orient)

                # 2.) check if this conflicts with any of the other ships by
                #     by making sure that every entry in _board_matrix is None
                conflict = ['No']
                # 2b.) If the ship is not valid, retry step 1
                if orient == 1:
                    for n in range(ship_length):
                        if self._board_matrix[row+n][col] is None:
                            conflict.append('No')
                        else:
                            conflict.append('Yes')

                else:
                    for n in range(ship_length):
                        if self._board_matrix[row][col+n] is None:
                            conflict.append('No')
                        else:
                            conflict.append('Yes')
                print(conflict)
                if 'Yes' not in conflict:
                    # 3.) If the ship is valid set the appropriate elements _board_matrix array
                    #     equal to the ship
                    # Example: to place a vertical destroyer at C2:
                    #    board_matrix[2][2] = my_ship
                    #    board_matrix[3][2] = my_ship

                    for n in range(ship_length):
                        if orient == 1:
                            self._board_matrix[row+n][col] = my_ship
                        else:
                            self._board_matrix[row][col+n] = my_ship

                    self._my_ships.append(my_ship)
                    validPlac = True

            # --------- END YOUR CODE ----------

    def guess(self, row, col) -> Tuple[int, Optional[ship.Ship]]:
        """
        Tell the other player whether a row and column guess is a hit or miss.
        Record the (row,col) guess in either self._their_hits or self._their_misses

        If a space is guessed twice do not hit the ship twice. That's cheating :)

        Returns a tuple of (status, ship) where
            status = 0: miss
                   = 1: hit
                   = 2: sunk

            ship   = None if a hit or miss
                   = ship object if sunk

        """
        my_ship: ship.Ship = self._board_matrix[row][col]

        # if my_ship is None the guess is a miss, otherwise its a hit

        # --------- BEGIN YOUR CODE ----------

        # Hit logic:
        # make sure this is a *new* hit (no double guesses)
        # add to _their_hits
        # hit the ship
        # check if ship is sunk
        # return either (1,None) or (2,my_ship)

        # Miss logic:
        # add to _their_misses
        # return (0, None)

        # --------- END YOUR CODE ----------


    def take_turn(self, opponent):
        """
        Prompt the user to guess a row and column. The user should enter a lower case letter
        followed by a number. Updates self._my_hits, self._my_misses, and self._sunk_ships
        """

        # --------- BEGIN YOUR CODE ----------

        # 1.) Prompt user for a guess. Valid input would be a string like c,4
        #     If the guess is not valid ask the user to enter another guess

        # 2.) Call opponent.guess() to check wether the guess is a hit or miss

        # 3.) Update my_hits, my_misses, and sunk_ships accordingly

        # 4.) If the sunk_ships array has 5 ships in it set self.complete to True

        # --------- END YOUR CODE ----------

    def print_board(self):
        """
        Print the player's board as text, useful for debugging
        """

        print("=" * 10)
        for row in self._board_matrix:
            for entry in row:
                if entry is None:
                    print("_", end="")
                else:
                    print(entry.length, end="")
            print("")
        print("=" * 10)

    def draw(self,
             my_board: game_board.GameBoard,
             their_board: game_board.GameBoard):

        """ Add sprites to the game board's to indicate
        ship positions, guesses, hits, etc """

        for my_ship in self._my_ships:
            my_ship.draw(my_board)
        for miss in self._their_misses:
            my_board.add_sprite(sprites.miss, miss)
        for hit in self._their_hits:
            my_board.add_sprite(sprites.hit, hit)

            # draw hit indicators on their board
        for miss in self._my_misses:
            their_board.add_sprite(sprites.miss, miss)
        for their_ship in self._sunk_ships:
            their_ship.draw(their_board)
        for hit in self._my_hits:
            their_board.add_sprite(sprites.hit, hit)
