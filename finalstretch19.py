import pyxel


# taille de la fenetre 256x256 pixels
# ne pas modifier
pyxel.init(256, 256, title="Casse_Brique")


# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 128
vaisseau_y = 220
ball_x = 128
ball_y = 210
score = 0
vie = 3
game = False
win = False

xball_speed = 5
yball_speed = 3
brick_x = [38, 68, 98, 128, 158, 188] 
brick_y = [62, 62, 62, 62, 62, 62]
brick_x2 = [38, 68, 98, 128, 158, 188]
brick_y2 = [90, 90, 90, 90, 90, 90]
exleft = 38
exright = 218
textop = 62
texbtom = 76
bextop = 90
bexbtom = 118

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 202) :
            x = x + 6
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 20) :
            x = x - 6
    return x, y

def ball_movement(x, y):
    global xball_speed, yball_speed, vaisseau_x, vaisseau_y, ball_x, ball_y, brick_x, brick_y
    x -= xball_speed
    y -= yball_speed
    if (x < 5) or (x > 246):
        xball_speed = -xball_speed
        yball_speed = yball_speed
    elif (y < 5):
        xball_speed = xball_speed
        ball_y = ball_y - 5
        yball_speed = -yball_speed
    if  215 <= y <= (238):
        if (vaisseau_x -20) <= x < (vaisseau_x) or (vaisseau_x + 32) < x <= (vaisseau_x + 55):
            ball_y = ball_y + 5
            xball_speed = -xball_speed*1.015
            yball_speed = -yball_speed*1.015
        elif vaisseau_x <= x <= (vaisseau_x +32):
            ball_y = ball_y + 5
            xball_speed = xball_speed*1.015
            yball_speed = -yball_speed*1.015
      
      
    #if ball_y == extop and exleft <= ball_x <= exright: #rebond contre brique en-dessous
     #   xball_speed = xball_speed
      #  yball_speed = -yball_speed
    #if ball_y == exbtom and exleft <= ball_x <= exright: #rebond contre brique au-dessus
     #   xball_speed = xball_speed
      #  yball_speed = -yball_speed
    #if brick_y[0] <= ball_y <= (brick_y[11]+14):
     #   for l in range (12):
      #      if brick_x[l -1] <= x <= (brick_x[l-1]+30):
       #         xball_speed = xball_speed 
        #        yball_speed = -yball_speed    
    else:
        xball_speed = xball_speed
        yball_speed = yball_speed
    
    return x, y

def ballxbrick(ball_x, ball_y):
    global exright, exleft, textop, texbtom, bextop, bexbtom, xball_speed, yball_speed, brick_x, brick_y, brick_x2, brick_y2, score
    for h in range(0, len(brick_x)):
        if brick_x[h-1] <= ball_x and ball_x <= (brick_x[h-1] + 30) and textop <= ball_y <= texbtom: #rebond contre brique nivsup
            brick_x.pop(h - 1)
            brick_y.pop(h - 1)
            xball_speed = xball_speed
            yball_speed = -yball_speed  
            score = score + 10
            break
    for i in range(0, len(brick_x2)):
        if brick_x2[i-1] <= ball_x and ball_x <= (brick_x2[i-1] + 30) and bextop <= ball_y <= bexbtom: #rebond contre brique  nivinf
            brick_x2.pop(i - 1)
            brick_y2.pop(i - 1)
            ball_speed = xball_speed
            yball_speed = -yball_speed
            score = score + 15
            break
     
           
    return ball_x, ball_y

def life(game, vie):
    global ball_y
    if ball_y > 250:
        vie = vie - 1
        game = False
    return game, vie

def victory(win):
    global brick_x, brick_y, brick_x2, brick_y2
    if len(brick_x) == 6 and len(brick_y) == 6 and len(brick_x2) == 5 and len(brick_y2) == 5:
        win = True
    return win
        
     

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, ball_x, ball_y, brick_x, brick_y, xball_speed, yball_speed, score, vie, game, win
    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    game, vie = life(game, vie)
    win = victory(win)
    if game == False:
        ball_x, ball_y = 128, 200
    if pyxel.btnr(pyxel.KEY_SPACE):
        game= True
    if game == True:
        ball_x, ball_y = ball_movement(ball_x, ball_y)
        ball_x, ball_y = ballxbrick(ball_x, ball_y)
    
   
    #if game == False:
     #   ball_x, ball_y = 128, 210
    #if pyxel.btnr(pyxel.KEY_SPACE):
     #   game = True
    
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 14, 8)
    pyxel.tri(vaisseau_x, vaisseau_y, vaisseau_x, vaisseau_y+15, vaisseau_x-15, vaisseau_y+15, 8)
    pyxel.tri(vaisseau_x+32, vaisseau_y, vaisseau_x+32, vaisseau_y+15, vaisseau_x+47, vaisseau_y+15, 8)
    """
    pyxel.rect(vaisseau_x-15, vaisseau_y+15, 63, 4, 8)
    """

    pyxel.text(20, 20, "score : %s " % str(score), 7)  
    pyxel.text(200, 225, "vie : %s " % str(vie), 7)
    pyxel.circ(ball_x,ball_y, 5, 4)
    for i in range(0, 6):
        b = brick_x[i - 1]
        c = brick_y[i - 1]
        pyxel.rectb(b, c, 30, 14, 10)
    for i in range(0, 6):
        d = brick_x2[i - 1]
        e = brick_y2[i - 1]
        pyxel.rectb(d, e, 30, 14, 11)
    
    if vie == 0:
        pyxel.cls(0)
        pyxel.text(110, 128, "Game Over", 7)
    
    if win == True:
        pyxel.cls(0)
        pyxel.text(110, 128, "Victory", 7)
   
    
    #for by in range(4):
        #for i in range(0, 7):
         #   pyxel.rectb(brick_x[i - 1], brick_y[by -1], 30, 14, 10+by)
          #  """pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
           # pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
            #pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
            #pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
            #pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)"""
    
pyxel.run(update, draw)
