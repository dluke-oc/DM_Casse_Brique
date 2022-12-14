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
totbrick = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

b1 = 1
b2 = 1
b3 = 1
b4 = 1
b5 = 1
b6 = 1
b7 = 1
b8 = 1
b9 = 1
b10 = 1
b11 = 1
b12 = 1

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
    
    return x, y

def ballxbrick(x, y):
    global exright, exleft, textop, texbtom, bextop, bexbtom, xball_speed, yball_speed, brick_x, brick_y, brick_x2, brick_y2, score, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12
    if b1 == 1:
        if (38) <= x < (68) and 62 <= y <= 76:     
            i = brick_x.index(38)
            brick_x.pop(i)
            brick_y.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 15
            b1 = b1 + 1
    if b2 == 1:
        if (68) <= x < (98) and 62 <= y <= 76:       
            i = brick_x.index(68)
            brick_x.pop(i)
            brick_y.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed
            score = score + 15
            b2 = b2 + 1
    if b3 == 1:
        if (98) <= x < (128) and 62 <= y <= 76:       
            i = brick_x.index(98)
            brick_x.pop(i)
            brick_y.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 15
            b3 = b3 + 1
    if b4 == 1:
        if (128) <= x < (158) and 62 <= y <= 76:    
            i = brick_x.index(128)
            brick_x.pop(i)
            brick_y.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 15
            b4 = b4 + 1
    if b5 == 1:
        if (158) <= x < (188) and 62 <= y <= 76:       
            i = brick_x.index(158)
            brick_x.pop(i)
            brick_y.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 15
            b5 = b5 + 1
    if b6 == 1:
        if (188) <= x <= (218) and 62 <= y <= 76:        
            i = brick_x.index(188)
            brick_x.pop(i)
            brick_y.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 15
            b6 = b6 + 1
    if b7 == 1:
        if (38) <= x < (68) and 90 <= y <= 104:        
            i = brick_x2.index(38)
            brick_x2.pop(i)
            brick_y2.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 10
            b7 = b7 + 1
    if b8 == 1:
        if (68) <= x < (98) and 90 <= y <= 104:        
            i = brick_x2.index(68)
            brick_x2.pop(i)
            brick_y2.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 10
            b8 = b8 + 1
    if b9 == 1:
        if (98) <= x < (128) and 90 <= y <= 104:       
            i = brick_x2.index(98)
            brick_x2.pop(i)
            brick_y2.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 10
            b9 = b9 + 1
    if b10 == 1:
        if (128) <= x < (158) and 90 <= y <= 104:        
            i = brick_x2.index(128)
            brick_x2.pop(i)
            brick_y2.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 10
            b10 = b10 + 1
    if b11 == 1:
        if 158 <= x < 188 and 90 <= y <= 104:        
            i = brick_x2.index(158)
            brick_x2.pop(i)
            brick_y2.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 10
            b11 = b11 + 1
    if b12 == 1:
        if (188) <= x <= 218 and 90 <= y <= 104:        
            i = brick_x2.index(188)
            brick_x2.pop(i)
            brick_y2.pop(i)
            xball_speed = xball_speed*1.050
            yball_speed = -yball_speed*1.050
            score = score + 10
            b12 = b12 + 1
        
           
    return 

def life(game, vie):
    global ball_y
    if ball_y > 250:
        vie = vie - 1
        game = False
    return game, vie

def victory(win):
    global score
    if score >= 150:
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
        ballxbrick(ball_x, ball_y)
       
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global vaisseau_x, vaisseau_y, ball_x, ball_y, brick_x, brick_y, xball_speed, yball_speed, score, vie, game, win

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
    pyxel.circ(int(ball_x),int(ball_y), 5, 4)
    for i in range(0, len(brick_x)):
        b = brick_x[i]
        c = brick_y[i]
        pyxel.rectb(b, c, 30, 14, 10)
    for i in range(0, len(brick_x)):
        d = brick_x2[i]
        e = brick_y2[i]
        pyxel.rectb(d, e, 30, 14, 11)
    
    if vie == 0:
        pyxel.cls(0)
        pyxel.text(110, 128, "Game Over", 7)
    
    if win == True:
        pyxel.cls(0)
        pyxel.text(110, 128, "Victory", 7)
   
    

pyxel.run(update, draw)
