from math import floor

# At its current state it will only validate puzzles.

class SudokuGrid:
    def __init__(self,g=[0]*81):
        self.grid = g
        self.possibilities = [[]]*81

    def asChunk(self,x,y,g):
        c = [g[((y*3+i)*3+x)*3:((y*3+i)*3+x)*3+3] for i in [0,1,2]]
        return [x for l in c for x in l]

    def row(self,y,g):
        return g[y*9:y*9+9]

    def column(self,x,g): 
        return g[x::9]
    
    def solve(self):
        print('not done')
        
    def genPossibilities(self):
        self.possibilities = [[]]*81
        for i in range(len(self.grid)):
            if self.grid[i] == 0:
                p = []
                for j in range(1,10):
                    if self.isPossibility(i,j):
                        p.append(j)
                else:
                    self.possibilities[i] = p
                     

    def isPossibility(self,i,j):
        x, y = i%9, (i//9)*9
        return not (j in self.row(y, self.grid) or j in self.column(x, self.grid) or     
                    j in self.asChunk(x//3, y//3, self.grid))

    def validate(self):
        if sum(self.grid)!=405:
            return False
        for i in range(0,9):
            if sum(self.row(i,self.grid)) != 45 or sum(self.column(i,self.grid)) != 45 or sum(self.asChunk(i%3, i//3, self.grid)) != 45:
                print(i, sum(self.row(i,self.grid)), sum(self.column(i,self.grid)), sum(self.asChunk(i%3, i//3, self.grid)))
        return True
            

    def printGrid(self):
        text = ''
        for i in range(len(self.grid)):
            text += str(self.grid[i]) + ' '
            if ((i+1)%9)==0:
                text += '\n'*(2 if ((i+1)%27==0) else 1)
            elif ((i+1)%3)==0:
                text += '  '
        print(text)


example = [0,0,6,  0,0,0,  4,3,9,
           0,8,0,  0,0,1,  7,2,0,
           3,4,7,  2,0,0,  0,0,8,
           
           0,3,0,  0,0,0,  0,0,0,
           0,1,2,  8,4,3,  6,9,0,
           0,0,0,  0,0,0,  0,8,0,

           4,0,0,  0,0,7,  9,1,2,
           0,9,3,  6,0,0,  0,7,0,
           5,7,1,  0,0,0,  8,0,0]

if __name__ == '__main__':
    sg = SudokuGrid(example)
    sg.printGrid()
