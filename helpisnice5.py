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
    global xball_speed, yball_speed, vaisseau_x
    x -= xball_speed
    y -= yball_speed
    if (x < 5) or (x > 246):
        xball_speed = -xball_speed
        yball_speed = yball_speed
    elif (y < 5) or (y > 246):
        xball_speed = xball_speed
        yball_speed = -yball_speed
    else:
        xball_speed = xball_speed
        yball_speed = yball_speed
    if vaisseau_x < (x, y) < (vaisseau_x + 63):
        xball_speed = xball_speed
        yball_speed = -yball_speed        
   
     
   
    return x, y

 
      



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
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 18, 8)
    pyxel.tri(vaisseau_x, vaisseau_y, vaisseau_x, vaisseau_y+15, vaisseau_x-15, vaisseau_y+15, 8)
    pyxel.tri(vaisseau_x+32, vaisseau_y, vaisseau_x+32, vaisseau_y+15, vaisseau_x+47, vaisseau_y+15, 8)
    pyxel.rect(vaisseau_x-15, vaisseau_y+15, 63, 4, 8)
    
    pyxel.circ(ball_x,ball_y, 5, 4)
    
    for i in range(0, 3):
        pyxel.rectb(19*2, (24+(i*7))*2, 15*2, 7*2, 10+i)
        pyxel.rectb(34*2, (24+(i*7))*2, 15*2, 7*2, 10+i)
        pyxel.rectb(49*2, (24+(i*7))*2, 15*2, 7*2, 10+i)
        pyxel.rectb(64*2, (24+(i*7))*2, 15*2, 7*2, 10+i)
        pyxel.rectb(79*2, (24+(i*7))*2, 15*2, 7*2, 10+i)
        pyxel.rectb(94*2, (24+(i*7))*2, 15*2, 7*2, 10+i)
    
pyxel.run(update, draw)
