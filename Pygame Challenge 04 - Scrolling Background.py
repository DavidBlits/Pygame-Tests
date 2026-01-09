# -----------------------------------------------------------------------------
# ANIMATION LAB - SCROLLING BACKGROUND
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# A background that scrolls across the screen creating the illusion of movement
# LEVEL 4+
# Everything listed in level 3 
# Multiple layers moving at different speeds to create the parallax effect, like you see to the left
# 
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
# 
# Challenge Difficulty:*
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githunb when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

import pygame
pygame.init()
screen= pygame.display.set_mode((800, 400))
clock=pygame.time.Clock()
scroll=0
ground_image = pygame.image.load('images/grass.jpeg')
mountain_image = pygame.image.load('images/mount.jpeg')
cloud_background = pygame.transform.scale(pygame.image.load('images/cloud.jpeg'),(800,400))
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scroll-=5

    sky_x=(scroll*0.2) % 800
    screen.blit(cloud_background,(sky_x-800,0))
    screen.blit(cloud_background,(sky_x,0))

    cloud_x = (scroll * 0.5) % 800 
    screen.blit(mountain_image, (cloud_x - 800, 100))
    screen.blit(mountain_image, (cloud_x, 100))

    ground_x = scroll % 800
    screen.blit(ground_image, (ground_x - 800, 300))
    screen.blit(ground_image, (ground_x, 300))

    

    pygame.display.flip()


