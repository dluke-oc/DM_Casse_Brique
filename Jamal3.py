import pyxel
import phys

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")
space = phys.space(gravity=(0, 25))

phys.margin(col=pyxel.COLOR_RED)

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 100
ballz_x = 60
ballz_y = 80

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1

    return x, y

def ballz_movement(x, y):
 radius = 2
 for _ in range(50):
     x, y = uniform(0, 120), uniform(0, 80)
     phys.circ(x, y, radius, vel=(uniform(-25, 25), uniform(-25, 25)))



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    ballz_x, ballz_y = ballz_movement(ballz_x, ballz_y)
       
    
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 4, 8)
    
    pyxel.circ(ballz_x,ballz_y, 5, 4)
    
pyxel.run(update, draw)
