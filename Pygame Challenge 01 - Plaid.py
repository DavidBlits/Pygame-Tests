# -----------------------------------------------------------------------------
# COLOUR LAB - PLAID
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# The plaid must have 2 different colours
# LEVEL 4
# Everything listed in level 3 
# The plaid has 2 different strokeWeights
# LEVEL 4+
# Everything listed in level 4
# The plaid uses alpha colour
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
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
Width,Height = 800,800
window = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Plaid pattern")
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
TRANSPARENT_BLUE =(0, 0, 255, 100)
overlay = pygame.Surface((Width, Height), pygame.SRCALPHA)
window.fill(WHITE)
for x in range(0,Width,100):
    pygame.draw.line(window, RED, (x,0),(x,Height),20)
    pygame.draw.line(window, RED, (x + 30, 0),(x + 30, Height),5)
for y in range(0,Height,100):
    pygame.draw.line(overlay, TRANSPARENT_BLUE, (0, y),(Width, y    ),20)
    pygame.draw.line(overlay, TRANSPARENT_BLUE, (0, y+30),(Width, y+30),5)
window.blit(overlay, (0, 0))
pygame.display.flip()
exit= True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
pygame.quit()
