# -----------------------------------------------------------------------------
# GAMESTATE LAB - MENU
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# A minimum of 3 possible unique backdrops
# A minimum of 2 buttons that when clicked will change the view of the user
# A method to return to the main menu
# HTML Buttons
# Uses gamestates
# LEVEL 4
# A minimum of 4 possible unique windows
# A minimum of 3 buttons that when clicked will change the backdrop or view of the user
# A method to return to the main menu
# Use gamestates
# Collision detection style buttons
# LEVEL 4+
# Everything listed in level 3 and 4
# Add sound effects when the button is pressed or add a mouseover effect to the button (the button highlights or changes looks when the mouse goes over the locations of the button)
# Recommended Lessons:
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Images
# Pygame Animation
# Pygame Sounds
# Pygame The Game Loop
# Pygame Events
# Pygame Gamestates
# Pygame Collision Detection
# Pygame Sprites
# 
# Challenge Difficulty:****
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gamestate Lab")
font = pygame.font.SysFont("Arial", 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)

state = "MENU"

def draw_button(text, x, y, w, h, action_if_clicked):
    global state
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    rect = pygame.Rect(x, y, w, h)
    color = LIGHT_GRAY if rect.collidepoint(mouse_pos) else GRAY
    
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 3) 
    
    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)
    if rect.collidepoint(mouse_pos) and click:
        state = action_if_clicked
        pygame.time.delay(150)
# MAIN LOOP 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state == "MENU":
        screen.fill(WHITE)
        title1 = pygame.font.Font('fonts/NotoSansJP-VariableFont_wght.ttf',30)
        title = title1.render("MAIN MENU", True, BLACK)
        screen.blit(title, (320, 50))
        draw_button("Go to Plaid", 300, 150, 200, 50, "PLAID")
        draw_button("Go to Stripes", 300, 220, 200, 50, "STRIPES")
        draw_button("Go to Solids", 300, 290, 200, 50, "SOLIDS")
    elif state == "PLAID":
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (0, 0, 100, HEIGHT))
        pygame.draw.rect(screen, RED, (200, 0, 100, HEIGHT))
        pygame.draw.rect(screen, RED, (400, 0, 100, HEIGHT))
        pygame.draw.rect(screen, RED, (600, 0, 100, HEIGHT))
        pygame.draw.rect(screen, BLUE, (0, 100, WIDTH, 50))
        pygame.draw.rect(screen, BLUE, (0, 300, WIDTH, 50))
        pygame.draw.rect(screen, BLUE, (0, 500, WIDTH, 50))
        draw_button("Back to Menu", 50, 500, 200, 50, "MENU")
    elif state == "STRIPES":
        screen.fill(WHITE)
        for i in range(0, WIDTH, 40):
            pygame.draw.line(screen, GREEN, (i, 0), (i, HEIGHT), 5)
            
        draw_button("Back to Menu", 50, 500, 200, 50, "MENU")

    elif state == "SOLIDS":
        screen.fill(BLUE)
        draw_button("Back to Menu", 50, 500, 200, 50, "MENU")
    pygame.display.flip()

pygame.quit()
sys.exit()
