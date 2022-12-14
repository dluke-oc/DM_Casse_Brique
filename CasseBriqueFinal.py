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
vie = 5
game = False
win = False
rule = True

xball_speed = 5
yball_speed = 3

brick_x = [38, 68, 98, 128, 158, 188] 
brick_y = [62, 62, 62, 62, 62, 62]
brick_x2 = [38, 68, 98, 128, 158, 188]
brick_y2 = [90, 90, 90, 90, 90, 90]
totbrick = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
brick_corx = [98, 128, 38, 68, 158, 188, 38, 68, 98, 128, 158, 188]
brick_cory = [34, 34, 62, 62, 62, 62, 90, 90, 90, 90, 90, 90] #62 and 90 w/ ecart = 14
brick_col = [10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12]
a = 0

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
    global xball_speed, yball_speed, vaisseau_x, vaisseau_y, ball_x, ball_y
    x -= xball_speed
    y -= yball_speed
    if (x < 5) or (x > 246):
        xball_speed = -xball_speed
        yball_speed = yball_speed
    elif (y < 10):
        xball_speed = xball_speed
        y = y + 5
        yball_speed = -yball_speed
    if  215 <= y <= (238):
        if (vaisseau_x -20) <= x < (vaisseau_x-2) or (vaisseau_x + 35) < x <= (vaisseau_x + 55):
            ball_y = ball_y + 5
            xball_speed = -xball_speed
            yball_speed = -yball_speed
        elif vaisseau_x <= x <= (vaisseau_x +32):
            ball_y = ball_y + 5
            xball_speed = xball_speed
            yball_speed = -yball_speed
            
    return x, y

def ballxbrick():
    global brick_corx, brick_cory, xball_speed, yball_speed, score, totbrick, a, brick_col
    if len(totbrick) > 0:
        for i in range(0, len(totbrick)):
            if brick_corx[i] <= ball_x <= (brick_corx[i] + 30) and brick_cory[i] <= ball_y <= (brick_cory[i] + 14):
                if brick_col[i] == 10:
                    brick_corx.pop(i)
                    brick_cory.pop(i)
                    totbrick.pop(a)          
                    xball_speed = xball_speed*1.28
                    yball_speed = -yball_speed*1.28
                    score = score + 15         
                if brick_col[i] == 11:
                    brick_corx.pop(i)
                    brick_cory.pop(i)
                    totbrick.pop(a)
                    xball_speed = xball_speed*1.03
                    yball_speed = -yball_speed*1.03
                    score = score + 10
                if brick_col[i] == 12:
                    brick_col[i] = 11
                    xball_speed = xball_speed*1.03
                    yball_speed = -yball_speed*1.03
                    score = score + 5
    return 

def life(game, vie):
    global ball_y
    if ball_y > 250:
        vie = vie - 1
        game = False
    return game, vie

def victory(win):
    global totbrick
    if len(totbrick) == 0:
        win = True
    return win
        
     

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, ball_x, ball_y, xball_speed, yball_speed, score, vie, game, win, brick_corx, brick_cory, brick_col, rule
    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    game, vie = life(game, vie)
    win = victory(win)
    if game == False:
        ball_x, ball_y = 128, 128
    if pyxel.btnr(pyxel.KEY_SPACE):
        game = True
        rule = False
    if game == True:
        ball_x, ball_y = ball_movement(int(ball_x), int(ball_y))
        ballxbrick()
       
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global vaisseau_x, vaisseau_y, ball_x, ball_y, xball_speed, yball_speed, score, vie, game, win, brick_corx, brick_cory, brick_col, totbrick, rule

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 14, 8)
    pyxel.tri(vaisseau_x, vaisseau_y, vaisseau_x, vaisseau_y+15, vaisseau_x-15, vaisseau_y+15, 8)
    pyxel.tri(vaisseau_x+32, vaisseau_y, vaisseau_x+32, vaisseau_y+15, vaisseau_x+47, vaisseau_y+15, 8)

    pyxel.text(20, 20, "score : %s " % str(score), 7)  
    pyxel.text(200, 225, "vie : %s " % str(vie), 7)
    pyxel.circ(int(ball_x),int(ball_y), 5, 4)

    
    for i in range(0, len(totbrick)):
        pyxel.rectb(brick_corx[i], brick_cory[i], 30, 14, brick_col[i])
        
    if rule == True:
        pyxel.text(0, 150, "Les briques jaunes accelerent la balle + contaminent les autres!", 10)
        pyxel.text(60, 180, "Essayer de les garder pour la fin", 10)
    if vie == 0:
        pyxel.cls(0)
        pyxel.text(110, 128, "Game Over", 7)
    
    if win == True:
        pyxel.cls(0)
        pyxel.text(110, 128, "Victory", 7)
   
    

pyxel.run(update, draw)
