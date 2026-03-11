class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        total = 0
        rook_pos = self.findRook(board)
        total += self.findHori(board[rook_pos[0]])
        total += self.findHori(self.findVert(board, rook_pos[1]))
        return total

    def findRook(self, board) -> List[int]:
        for i in range(0, 8):
			for position, b in enumerate(board[i]):
				if b == "R":
					return [i, position]

    def findHori(self, row):
        pos = 7
        right_attack = False
        left_attack = False
        while row[pos] != "R":
            if row[pos] == 'p':
                right_attack = True
            if row[pos] != 'p' and row[pos] != '.':
                right_attack = False
            pos -= 1
        pos = 0
        while row[pos] != "R":
            if row[pos] == 'p':
                left_attack = True
            if row[pos] != 'p' and row[pos] != '.':
                left_attack = False
            pos += 1
        result = 0
        if left_attack == True:
            result += 1
        if right_attack == True:
            result += 1
		return result


    def findVert(self, board, rook_pos):
        chosen_row = []
        for b in board:
            for pos, char in enumerate(b):
                if pos == rook_pos:
                    chosen_row.append(char)
        return chosen_row
