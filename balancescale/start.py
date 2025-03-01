import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display and window's title
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Balance Scale')

# Set up the logo
icon = pygame.image.load('balancescale/assets/logo.png')
pygame.display.set_icon(icon)

# Set up the background
background = pygame.image.load('balancescale/assets/testbackground.jpg')
background = pygame.transform.scale(background, (width, height))
screen.blit(background, (0, 0))
pygame.display.update()

# Set up font and text
font = pygame.font.Font("balancescale/assets/fonts/Montserrat-VariableFont_wght.ttf", 60)
text = font.render("Kaita isn't gay", True, (0, 0, 0))
text_rect = text.get_rect(center=(width // 2, height // 2))

#Load Background Music
pygame.mixer.music.load('balancescale/assets/music/06052021_1_loading_screen_fresh_air_saturation.mp3')
pygame.mixer.music.play(-1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the text on the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()