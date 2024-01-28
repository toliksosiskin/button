def setup():
    size(500,500)
def draw():
    rect(100,100,300,300)
def mouseClicked():
    if mouseX>100 and mouseX<400 and mouseY>100 and mouseY<400:
        background(255,0,0)
        fill(255,0,0)
        noStroke()
