#   Build tests to see if a chess board if valid or not.
#   If it is, return true, else false.

#   Create a mock board
chessBoard = {
    "1a":"bking",
    "1b":"bqueen",
    "1c":"bknight",
    "1d":"brook",
    "1e":"bbishop",
    "1f":"bpawn",
    "1g":"bpawn",
    "1h":"bpawn",
    "2a":"bpawn",
    "2b":"bpawn",
    "2c":"bpawn",
    "2d":"bpawn",
    "2e":"bpawn",
    "2f":"wking",
    "2g":"wqueen",
    "2h":"wknight",
    "3a":"wrook",
    "3b":"wbishop",
    "3c":"wpawn",
    "3d":"wpawn",
    "3e":"wpawn",
    "3f":"wpawn",
    "3g":"wpawn",
    "3h":"wpawn",
    "4a":"wpawn",
    "4b":"wpawn",
    "4c":"bknight",
    "4d":"brook",
    "4e":"bbishop",
    "4f":"wknight",
    "4g":"wrook",
    "4h":"wbishop",
    "5a":"",
    "5b":"",
    "5c":"",
    "5d":"",
    "5e":"",
    "5f":"",
    "5g":"",
    "5h":"",
    "6a":"",
    "6b":"",
    "6c":"",
    "6d":"",
    "6e":"",
    "6f":"",
    "6g":"",
    "6h":"",
    "7a":"",
    "7b":"",
    "7c":"",
    "7d":"",
    "7e":"",
    "7f":"",
    "7g":"",
    "7h":"",
    "8a":"",
    "8b":"",
    "8c":"",
    "8d":"",
    "8e":"",
    "8f":"",
    "8g":"",
    "8h":"",
}

# Function to parse board and validate
def isBoardValidated(board):
    #   Check if atleast 1 king is on the board.
    if "wking" not in board.values() or "bking" not in board.values():
        return False
    #   Check if there are a maximum of 16 pieces.
    #   b, w = black and white piece counters.
    b, w = 0, 0
    #   convert board to list, so we can take the values.
    board_values = list(board.values())
    for i, values in enumerate(board_values):
        #   Check if the value is blank (no chess piece)
        #   and discard it.
        if values is not "":
            if values[0] == "w":
                w += 1
            elif values[0] == "b":
                b += 1
        #   If there are more than 16 black or white pieces,
        #   something's up, so return false
        if(w > 16 or b > 16):
            return False
    #   Check if there are stuff that are beyond 8h coords.
    board_keys = list(board.keys())
    for j, keys in enumerate(board_keys):
        #   If there's a piece above 8 in the board, i.e 9a,
        #   somethings up. So return false.
        if int(keys[0]) > 8:
            return False
    #   If all is good, and the above cases don't return false,
    #   there should be no problems going on, so return true
    else:
        return True
