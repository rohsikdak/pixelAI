class pixel:
    status = 0
    def __init__(self):
        self.status = 0
    # 0 undefined, 1 p1, 2 p2

class pixel_Game:
    board = list()
    slider_x = 0
    slider_y = 0
    def __init__(self):
        self.board = list()
        self.slider_x = 3
        self.slider_y = 4
		
    def init_board(self):
        for i in range(8):
            self.board.append(list())
            for j in range(8):
                temp_pixel = pixel()
                temp_pixel.status = 0
                self.board[i].append(temp_pixel)
        self.board[3][4].status = 1
        self.board[4][3].status = 2
    
    def print_board(self):
        for i in range(8):
            print(7-i,end=" ")
            for j in range(8):
                print(self.board[j][7-i].status ,end=" ")
            print()
        print(end="  ")
        for i in range(8):
            print(i, end = " ")
        print(end ="\n\n")

    def get_board(self):
        return board

    def set_pixel(self,turn,x,y,fin):
        if x>7 or y>7 or x<0 or y<0:
            return False
        if self.slider_x == x or self.slider_y == y :
            if self.board[x][y].status == 0:
                self.board[x][y].status = turn
                self.slider_x = x
                self.slider_y = y
                if self.is_fin(turn,x,y):
                    fin[0] = True
                    fin.append(turn)
                return True
        return False

    def is_fin(self,turn,x,y):
        if self.horizon4(turn,x,y,0):
            return True
        elif self.vertical4(turn,x,y,0):
            return True
        elif self.cross4(turn,x,y,0):
            return True
        elif self.cross4_1(turn,x,y,0):
            return True
        return False

    def horizon4(self,turn,x,y,count):
        if count == 3:
            return True
        if count == 0 and x-1 >= 0 and self.board[x-1][y].status == turn:
            return self.horizon4(turn,x-1,y,count)
        if x+1 < 8 and self.board[x+1][y].status == turn:
            return self.horizon4(turn,x+1,y,count+1)
        return False

    def vertical4(self,turn,x,y,count):
        if count == 3:
            return True
        if count == 0 and y-1>=0 and self.board[x][y-1].status == turn:
            return self.vertical4(turn,x,y-1,count)
        if y+1 < 8 and self.board[x][y+1].status == turn:
            return self.vertical4(turn,x,y+1,count+1)
        return False
#/ 방향
    def cross4(self,turn,x,y,count):
        if count == 3:
            return True
        if count==0 and y-1>=0and x-1>=0and self.board[x-1][y-1].status == turn:
            return self.cross4(turn,x-1,y-1,count)
        if y+1<8 and x+1<8 and self.board[x+1][y+1].status == turn:
            return self.cross4(turn,x+1,y+1,count+1)
        return False
#\방향
    def cross4_1(self,turn,x,y,count):
        if count == 3:
            return True
        if count==0 and y-1>=0 and x+1<8 and self.board[x+1][y-1].status == turn:
            return self.cross4(turn,x+1,y-1,count)
        if y+1<8 and x>0 and self.board[x-1][y+1].status == turn:
            return self.cross4(turn,x-1,y+1,count+1)
        return False

def main():
    g1 = pixel_Game()
    g1.init_board()
    g1.print_board()
    turn = 1
    fin = [False]
    while(not fin[0]):
        while(True):
            print(turn, "번 플레이어의 차례입니다.")
            x = int(input("x를 입력하세요 : "))
            y = int(input("y를 입력하세요 : "))
            if(g1.set_pixel(turn,x,y,fin)):
                turn = turn % 2 + 1
                break
        g1.print_board()
    print("player",fin[1],"win!!")

main()
