# -----------------------------------------------------------------------------
# IMAGE LAB - IMAGE COLLAGE
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different images to create a collage
# You can repeat the same images must use other commands to change the look (example, tint)

# LEVEL 4
# Everything listed in level 3 
# Create a scene with images

# LEVEL 4+
# Everything listed in level 4
# Randomize or animate something

# Recommended Lessons:
# P5.js intro
# P5.js drawing
# P5.js colour
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githun when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

import pygame
import random
import math
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Collage")

white = (255, 255, 255)
light_gray = (200, 200, 200)

Flight = pygame.image.load('images/flight.jpeg')
TripleT= pygame.image.load('images/TripleT.png')
Lobby = pygame.image.load('images/lobby.jpeg')
Lobby = pygame.transform.scale(Lobby,(800,600))

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.blit(Lobby,(0,0))
    screen.blit(Flight,(100,300))
    screen.blit(TripleT,(500,250))
    pygame.display.flip()

