# -----------------------------------------------------------------------------
# TEXT & FONT LAB - RANSOM NOTE
# 
# Use your new knowledge of text in Pygame to make a ransom note similar to the picture above.
# 
# You use whatever fonts you want as long as you use at least 1 custom font.
# 
# The message can say whatever you want as long as it is school safe (remember the code of conduct).
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different font styles
# Use 3 different colours
# Write a message that is school safe and does not have anyone’s personal information (including names)

# LEVEL 4
# Everything listed in level 3 
# Use at least 4 different font styles
# Use 4 different colours

# LEVEL 4+
# Everything listed in level 4
# Use a custom downloaded font
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Text & Fonts
# 
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

import pygame
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ransom Note")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
screen.fill(BLACK)

font1 = pygame.font.SysFont("arial", 40, bold=True)
font2 = pygame.font.SysFont("courier", 50, italic=True)
font3 = pygame.font.SysFont("times", 45)
font4 = pygame.font.SysFont("verdana", 35, bold=True)

text1 = font1.render("YOU ARE", True, RED)
text2 = font2.render("A BOT", True, BLUE)
text3 = font3.render("KEEP CODING", True, GREEN)
text4 = font4.render("AND WATCH D RICHARD VIDEOS", True, YELLOW)

screen.blit(text1, (150, 100))
screen.blit(text2, (120, 200))
screen.blit(text3, (100, 320))
screen.blit(text4, (140, 450))

pygame.display.flip()


exit=True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit=False
pygame.quit()


