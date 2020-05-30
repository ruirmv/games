def game():
    T = TicTacToe()
    
    while T.end_game() == 0:
        #print(T.percept())
        
        ans = input("Choose a number between 1-9: ")
        if int(ans) == -1 : break
        T.execute_action(None, ans)
        
        T.printBoard()
        
class Environment():
    def execute_action(self, agent, action):
        raise NotImplementedError
    
    def percept(self, agent):
        raise NotImplementedError
        
class TicTacToe(Environment):
    def __init__(self):
        self.last = -1
        self.state = [0] * 9
    
    
    def end_game(self):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]
        
        for i in [self.last, -self.last]:
            for j in wins:
                w = True
                for k in j:
                    if self.state[k] != i:
                        w = False
                        break
                if w == True: 
                    if i > 0: winner = 'O'
                    else: winner = 'X'
                    print(f"The winner is {winner}.")
                    return i
        if all([x != 0 for x in self.state]):
            print("It's a draw.")
            return 2
                    
        return 0

    def execute_action(self, agent, action):
        a = int(action)
        if (a > 9) | (a < 1): return
        if self.state[a-1] == 0: 
            self.state[a-1] = -self.last
            self.last = -self.last
            
    def percept(self, agent):
        return self.state
            
    def freePosition(self):
        return [x for x in range(9) if self.state[x] == 0]
    
    
    def printBoard(self):
        line1 = " | | \n"
        line2 = "-----\n"
        
        M = [0, 2, 4, 12, 14, 16, 24, 26, 28]
        
        L = (line1 + line2) * 2 + line1
        
        board = list(L)
        
        for i in range(9):
            if self.state[i] == 0: continue
            elif self.state[i] == 1: sym = 'O'
            else: sym = 'X'
            
            board[M[i]] = sym
        
        s = ''.join([str(n) for n in board])
        print(s)
        return
