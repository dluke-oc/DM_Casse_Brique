import pyxel


# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 100
ball_x = 60
ball_y = 80
dx = 2
dy = 2
btop = 123
bbtom = 5
bleft = 5
bright = 123


def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1

    return x, y
def ball_movement(x, y, dx, dy):
    x = dx
    y = dy
    if (y < bbtom) or (y > btop):
        dy *= -1
    if (x < bleft) or (x > bright):
        dx *= -1
    return x, y, dx ,dy



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
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 4, 8)
    
    pyxel.circ(ball_x,ball_y, 5, 4)
    
pyxel.run(update, draw)
