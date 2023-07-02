import pygame
import math
pygame.init()

window = pygame.display.set_mode((900,600))

joystick_pos = pygame.Vector2(290,290) 
joy_pos  = () 

def get_relative(mouse_pos):
    mouse_dist =  math.dist([290,290],[mouse_pos[0],mouse_pos[1]])
    if mouse_dist > 100:
        return (290,290)
    else:
        return pygame.mouse.get_pos()

def joy_input(joy_pos,radius):
    print((math.floor(math.sin(joy_pos[0])),math.floor(math.sin(joy_pos[1]))))
running = True

while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
    window.fill("blue")
    pygame.draw.circle(window,"red",joystick_pos,100,5)
    joy_pos = get_relative(pygame.mouse.get_pos()) 
    pygame.draw.circle(window,"white",joy_pos,40,100)
    joy_input(joy_pos,100)
    pygame.display.flip()

pygame.quit()
