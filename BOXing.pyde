from math import pi
rotation_rate=100.0                                       
def setup():
    size(1000, 1000, P3D)
def draw():
    global rotation_rate
    background(0)
    noFill()
    stroke(255)
    translate(width / 2, height / 2, 0)
    edge_length = 6400
    for b in range(15):
        pushMatrix()
        angle = frameCount / rotation_rate * b
        if keyPressed:
            rotation_rate-=0.1
        rotateX(angle)
        rotateY(angle)
        stroke(100 + b * (156 / 15), 100 + b * (156 / 15), 0)
        box(edge_length)
        popMatrix()
        edge_length /= 2
        
        