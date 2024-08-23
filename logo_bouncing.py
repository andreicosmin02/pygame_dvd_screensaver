import pygame
from PIL import Image
import random
import pyautogui

background_colour = (0, 0, 0)
(width, height) = pyautogui.size()

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
running = True

img_path = "./assets/logo.jpg"
resized_img_path = './assets/logo.jpg'

base_width = 250
img = Image.open(img_path)
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)

img.save(resized_img_path)
logo = pygame.image.load(resized_img_path).convert_alpha()

img_pos = {
    'x': random.randint(0, width - base_width - 1),
    'y': random.randint(0, height - hsize - 1)
}
moving_speed = {
    'x': 200, 
    'y': 200
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock = pygame.time.Clock().tick(60)
    dt = clock / 1000

    
    if img_pos['x'] + moving_speed['x']* dt < 0 or img_pos['x'] + moving_speed['x']* dt + base_width > width:
        moving_speed['x'] *= -1
    if img_pos['y'] + moving_speed['y']* dt < 0 or img_pos['y'] + moving_speed['y']* dt + base_width > height:
        moving_speed['y'] *= -1

    img_pos['x'] += moving_speed['x'] * dt
    img_pos['y'] += moving_speed['y'] * dt
    
    
    screen.fill(background_colour)
    screen.blit(logo, (img_pos['x'], img_pos['y']))


    pygame.display.flip()

