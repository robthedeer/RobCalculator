import pygame
import random

pygame.init()

display = pygame.display.set_mode((450,640))
pygame.display.set_caption("SLIDE PUZZLE")

backgroundColor =(255,255,255)
tilecolor =(0,0,0)

#Functions
tiles = []


def drawTile():
    tile_size =100
    tile_margin =5
    rows,cols =4,4

    for row in range(rows):
        for col in range(cols):
            tile_no =row*cols + col
            if tile_no != rows*cols -1:
                tile =pygame.Surface((tile_size,tile_size))
                tile.fill(tilecolor)
                tile_rect =tile.get_rect()
                tile_rect.topleft =(col*(tile_size + tile_margin),row*(tile_size +tile_margin))

                tiles.append(tile)


    
        display.blit(tile,tile_rect,tile_no)




    

#game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
    
    display.fill(backgroundColor)
    drawTile()


    pygame.display.update()
    pygame.display.flip()

pygame.quit()