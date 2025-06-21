import pygame

# dont change it
width, height = 600, 600    
FPS = 60
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("TicTacToe Game")


# locations
# coordinates for drawing 'o'
o_coords = [(120, 120), (300, 120), (480, 120), 
            (120, 300), (300, 300), (480, 300),
            (120, 480), (300, 480), (480, 480)]

# coordinates for drawing 'x'
x_coords = [(80, 80), (260, 80), (440, 80),
            (80, 260), (260, 260), (440, 260),
            (80, 440), (260, 440), (440, 440)]

x_on_board, o_on_board = [], []


# customize
pygame.font.init()
winner_font = pygame.font.SysFont('Sunshine', 50)
bgcolor = (249, 249, 249)
line_color = (56, 57, 59)
o_color = (34, 124, 112)
x_color = (250, 112, 112)


# var for game
turn = 'x' #first player has 'x'
count = 0

board = ["1", "2", "3", 
         "4", "5", "6", 
         "7", "8", "9"]


def draw():
    window.fill(bgcolor)

    # drawing lines
    # args --> screen, color, [posx, posy, width, height]
    pygame.draw.rect(window, line_color, (70, 210, 460, 2))
    pygame.draw.rect(window, line_color, (70, 390, 460, 2))
    pygame.draw.rect(window, line_color, (210, 70, 2, 460))
    pygame.draw.rect(window, line_color, (390, 70, 2, 460))

    for i in o_on_board:
        pygame.draw.circle(window, o_color, (i[0], i[1]), 50, 4)
    
    for i in x_on_board:
        pygame.draw.line(window, x_color,(i[0], i[1]), (i[0] + 80, i[1] + 80), 4 )
        pygame.draw.line(window, x_color,(i[0], i[1] + 80), (i[0] + 80, i[1]), 4 )

    pygame.display.update()

def announce_winner(txt):
     txt = winner_font.render(txt, 1, (255, 255, 255))
     txt_bg = pygame.image.load("txt_bg.jpg")
     txt_bg = pygame.transform.smoothscale(txt_bg, (250, 100))

     window.blit(txt_bg, (width/2 - txt_bg.get_width()/2, height/2 - txt_bg.get_height()/2))
     window.blit(txt, (width/2 - txt.get_width()/2, height/2 - txt.get_height()/2))
     pygame.display.update()
     pygame.time.delay(5000)   

def check_win():
    global run
    # checks rows
    for i in [0, 3, 6]:
        if (board[i] == board[i + 1] == board[i + 2]):
            announce_winner("{} wins!".format(board[i]))
            run = False
    
    # checks cols
    for i in [0, 1, 2]:
        if (board[i] == board[i + 3] == board[i + 6]):
            announce_winner("{} wins!".format(board[i]))
            run = False

    # checks diagonals
    for i in [0]:
        if (board[i] == board[i + 4] == board[i + 8]):
            announce_winner("{} wins!".format(board[i]))
            run = False

    for i in [2]:
        if (board[i] == board[i + 2] == board[i + 4]):
            announce_winner("{} wins!".format(board[i]))
            run = False
    
    # checks for a tie
    if count == 9:
         announce_winner("Tie")
         run = False

def player_1(temp):
    global turn, count
    if board[temp] == "x" or board[temp] == "o" :
          return
    
    board[temp] = "x"
    count += 1
    x_on_board.append(x_coords[temp])
    # nxt turn is of 'o'
    turn = 'o'
    
def player_2(temp):
    global turn, count
    if board[temp] == "x" or board[temp] == "o" :
          return
    
    board[temp] = "o"
    count += 1
    o_on_board.append(o_coords[temp])
    # nxt turn is of 'x'
    turn = 'x'

def click_loc(x, y):
    
    # constraint of +- 80 pix from the center taking loc from o_coords

    if (x > 40 and y > 40) and (x <= 200 and y <= 200):       
            return 0
    elif (x > 220 and y > 40) and (x <= 380 and y <= 200):        
            return 1
    elif (x > 400 and y > 40) and (x <= 560 and y <= 200):        
            return 2
    elif (x > 40 and y > 220) and (x <= 200 and y <= 380):
            return 3
    elif (x > 220 and y > 220) and (x <= 380 and y <= 380):
            return 4
    elif (x > 400 and y > 220) and (x <= 560 and y <= 380):
            return 5
    elif (x > 40 and y > 400) and (x <= 200 and y <= 560):
            return 6
    elif (x > 220 and y > 400) and (x <= 380 and y <= 560):
            return 7
    elif (x > 400 and y > 400) and (x <= 560 and y <= 560):
            return 8

def game():
    global x, y, temp, run

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        
        # checking all the events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = event.pos[0]
                y = event.pos[1]   

                if turn == 'x':
                    temp = click_loc(x, y)
                    if temp != None:
                        player_1(temp)
                else:
                    temp = click_loc(x, y)
                    if temp != None:
                        player_2(temp)
                
        draw()
        check_win()
         
    pygame.quit() 

game()