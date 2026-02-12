


   




def find_king(board):
    for y in range(4):
        for x in range(4):
            if board[y][x] == 'K':
                return (x, y)
    return None

def find_rook(board):
    for y in range(4):
        for x in range(4):
            if board[y][x] == 'R':
                return (x, y)
    return None
def find_pawn(board):
    for y in range(4):
        for x in range(4):
            if board[y][x] == 'P':
                return (x, y)
    return None

def find_queen(board):
    for y in range(4):
        for x in range(4):
            if board[y][x] == 'Q':
                return (x, y)
    return None

def find_bishop(board):
        for y in range(4):
            for x in range(4):
                if board[y][x] == 'B':
                    return (x, y)
        return None

def attack_by_rook(king_pos, rook_pos):
    king_x, king_y = king_pos
    rook_x, rook_y = rook_pos
    if king_x == rook_x or king_y == rook_y:
        return True
    return False

def attack_by_pawn(king_pos, pawn_pos):
    king_x, king_y = king_pos
    pawn_x, pawn_y = pawn_pos
    if king_y == pawn_y - 1 and abs(king_x - pawn_x) == 1:
        return True
    return False

def attack_by_queen(king_pos, queen_pos):
    king_x, king_y = king_pos
    queen_x, queen_y = queen_pos
    if king_x == queen_x or king_y == queen_y or abs(king_x - queen_x) == abs(king_y - queen_y):
        return True
    return False

def attack_by_bishop(king_pos, bishop_pos):
    king_x, king_y = king_pos
    bishop_x, bishop_y = bishop_pos
    if abs(king_x - bishop_x) == abs(king_y - bishop_y):
        return True
    return False

def checkmate(board):
    king_pos = find_king(board)
    rook_pos = find_rook(board)
    pawn_pos = find_pawn(board)
    queen_pos = find_queen(board)
    bishop_pos = find_bishop(board)

    if rook_pos and attack_by_rook(king_pos, rook_pos):
        return 'Success'
    if pawn_pos and attack_by_pawn(king_pos, pawn_pos):
        return 'Success'
    if queen_pos and attack_by_queen(king_pos, queen_pos):
        return 'Success'
    if bishop_pos and attack_by_bishop(king_pos, bishop_pos):
        return  'Success'

    return 'Fail'



