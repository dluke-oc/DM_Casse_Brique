import pyxel


# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(256, 256, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 128
vaisseau_y = 220
ball_x = 60
ball_y = 80


xball_speed = 5
yball_speed = 5
brick_x = [38, 68, 98, 128, 158, 188, 38, 68, 98, 128, 158, 188, 38, 68, 98, 128, 158, 188] 
brick_y = [62, 62, 62, 62, 62, 62, 76, 76, 76, 76, 76, 76, 90, 90, 90, 90, 90, 90]
exleft = 38
exright = 218
extop = 62
exbtom = 104

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 202) :
            x = x + 4
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 20) :
            x = x - 4
    return x, y

def ball_movement(x, y):
    global xball_speed, yball_speed, vaisseau_x, vaisseau_y, ball_x, ball_y, brick_x, brick_y, exleft, exright, exbtom, extop
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
        if (vaisseau_x -20) <= x < (vaisseau_x):
            ball_y = ball_y + 5
            xball_speed = -xball_speed#*1.015
            yball_speed = -yball_speed#*1.015
        elif vaisseau_x <= x <= (vaisseau_x +55):
            ball_y = ball_y + 5
            xball_speed = xball_speed #*1.015
            yball_speed = -yball_speed#*1.015
   #if ball_x == exright and extop <= y <= exbtom: #rebond contre brique droite
    #    xball_speed = -xball_speed
     #   yball_speed = yball_speed      
    #if ball_x == exleft and extop <= y <= exbtom: #rebond contre brique gauche
     #   xball_speed = xball_speed
      #  yball_Speed = -yball_speed
    #if ball_y == extop and exleft <= ball_x <= exright: #rebond contre brique en-dessous
     #   xball_speed = xball_speed
     #   yball_speed = -yball_speed
    #if ball_y == exbtom and exleft <= ball_x <= exright: #rebond contre brique au-dessus
     #   xball_speed = xball_speed
      #  yball_speed = -yball_speed"""
       
    #if 62 <= y <= 90:
           #for l in range (5):
            #if brick_x[l -1] <= x <= brick_x[l]:
                #xball_speed = xball_speed 
                #yball_speed = -yball_speed
    else:
        xball_speed = xball_speed
        yball_speed = yball_speed
    
    return x, y

def brique_destruction():
    global brick_x, brick_y, yball_speed, xball_speed
    for i in range(0, 19):
        if brick_x[i]<= x <= brick_x[i - 30] and y == brick_y[i]:
            brick_x.pop(i)
            brick_y.pop(i)
            xball_speed = xball_speed
            yball_speed = -yball_speed
    return xball_speed, yball_speed, brick_x, brick_y
            
 
      



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, ball_x, ball_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    ball_x, ball_y = ball_movement(ball_x, ball_y)
    
    
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

    
    pyxel.circ(ball_x,ball_y, 5, 4)
    for i in range(0, 19):
        b = brick_x[i - 1]
        c = brick_y[i - 1]
        pyxel.rectb(b, c, 30, 14, 10)
    
    #for by in range(4):
        #for i in range(0, 7):
         #   pyxel.rectb(brick_x[i - 1], brick_y[by -1], 30, 14, 10+by)
          #  """pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
           # pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
            #pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
            #pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)
            #pyxel.rectb(brick_x[i - 1], (24+(i*7))*2, 15*2, (brick_x[i] - [brick_x[i - 1]), 10+i)"""
    
pyxel.run(update, draw)