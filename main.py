from ursina import *

app = Ursina()

window.borderless = False

# Terrain (mountain/hill style)
terrain = Entity(model='plane', scale=(100, 1, 100), texture='grass', texture_scale=(100,100))
hills = [Entity(model='sphere', color=color.brown, position=(x*8, 5, z*8), scale=5)
         for x, z in [(-4,-2),(3,6),(7,-6)]]

# Car setup
car = Entity(model='cube', color=color.red, position=(0,1,0), scale=(1.5,0.6,2))
car.velocity = 0

camera.parent = car
camera.position = (0,3,-8)
camera.rotation_x = 10

# Obstacles
obstacles = [Entity(model='cube', color=color.orange, scale=(1,1,1), position=(x,1,z))
             for x,z in [(-10,10),(20,-20),(30,5),(-25,-10)]]

def update():
    # Car forward/back motion
    if held_keys['w']:
        car.velocity += 0.05
    if held_keys['s']:
        car.velocity -= 0.025
    car.velocity = max(min(car.velocity,0.4),-0.2)
    car.position += car.forward * car.velocity
    
    # Car left/right rotation
    if held_keys['a']:
        car.rotation_y += 2
    if held_keys['d']:
        car.rotation_y -= 2

    # Collisions with obstacles (simple check)
    for obs in obstacles:
        if distance(car.position, obs.position) < 2.1:
            car.color = color.lime
            car.velocity = -0.2
        else:
            car.color = color.red

    # Hill climb: gravity effect
    # If above hills, slow down
    for h in hills:
        if distance(car.position, h.position) < 6:
            car.velocity *= 0.97

app.run()
