import pygame
import sys

pygame.init()


# def main():
#     window = pygame.display.set_mode((900, 600))
#     window.fill((202, 151, 39))
#     f1 = pygame.font.Font('PixelFont.ttf', 36)
#
#     pygame.draw.rect(window, (255, 255, 255), (700, 150, 150, 50))
#     pygame.draw.rect(window, (0, 0, 0), (700, 150, 150, 50), 5)
#     text1 = f1.render('Button', 0, (0, 0, 0))
#     window.blit(text1, (720, 160))
#
#     surf = pygame.Surface((50, 50))
#     surf.fill((255, 0, 0))
#     rect1 = surf.get_rect()
#     pos = pygame.mouse.get_pos()
#     window.blit(surf, rect1)
#
#     tom = pygame.image.load('media/Tom.jpg')
#     window.blit(tom, (300,300))
#     tomrect = tom.get_rect()
#     ang = 0
#
#     pygame.display.update()
#     pressed = pygame.mouse.get_pressed()
#     while True:
#         pygame.time.delay(20)
#         window.fill((0, 0, 0))
#         for i in pygame.event.get():
#             if i.type == pygame.QUIT:
#                 return
#             if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
#                 window.blit(f1.render('click', 0, (0,0,0)), (i.pos[0]-20, i.pos[1]-10))
#             if pygame.mouse.get_focused():
#                 pos = pygame.mouse.get_pos()
#                 pygame.draw.circle(window, (0,0,0), pos, 5)
#         rect1.x += 1
#         window.blit(surf, rect1)
#
#
#         pygame.display.update()

def main():
    window = pygame.display.set_mode((900, 600))
    window.fill((202, 151, 39))
    text = ['Python length:', 'fold', 'X-ray']
    font = pygame.font.Font('PixelFont.ttf', 36)
    t_p_l = font.render(text[0], 0, (0, 0, 0))
    t_f = font.render(text[1], 0, (0, 0, 0))
    t_x = font.render(text[2], 0, (0, 0, 0))
    lenghtX = 260
    python_lenght = 1

    pygame.display.update()
    while True:
        pygame.time.delay(20)
        window.fill((202, 151, 39))
        pos = pygame.mouse.get_pos()
        mos = pygame.mouse.get_pressed()[0]
        window.blit(t_p_l, (15, 30))
        lenght = pygame.draw.rect(window, (0, 0, 0), (270, 43, 450, 5))
        pygame.draw.rect(window, (255, 255, 255), (lenghtX-10, 33, 20, 20))
        if pos[0] >= lenght.left and pos[0] <= lenght.left + lenght.width and pos[1] >= 5 and pos[1] <= 70:
            if mos:
                lenghtX = pos[0]
                pygame.draw.rect(window, (255, 5, 255), (lenghtX-10, 33, 20, 20))
                python_lenght = lenghtX - lenght.left
                if python_lenght == 0:
                    python_lenght = 1
        pygame.draw.rect(window, (255, 255, 255), (740, 21, 85, 50))
        pygame.draw.rect(window, (0, 0, 0), (740, 21, 85, 50), 5)
        num_p_l = font.render(str(python_lenght), 0, (0, 0, 0))
        window.blit(num_p_l, (760, 30))


        pygame.draw.rect(window, (255, 255, 255), (700, 100, 125, 50))
        pygame.draw.rect(window, (0, 0, 0), (700, 100, 125, 50), 5)
        if pos[0] >= 700 and pos[0] <= 825 and pos[1] >= 100 and pos[1] <= 150:
                pygame.draw.rect(window, (0, 200, 0), (700, 100, 125, 50), 5)
        window.blit(t_f, (730, 110))
        pygame.draw.rect(window, (255, 255, 255), (700, 200, 125, 50))
        pygame.draw.rect(window, (0, 0, 0), (700, 200, 125, 50), 5)
        if pos[0] >= 700 and pos[0] <= 825 and pos[1] >= 200 and pos[1] <= 250:
            pygame.draw.rect(window, (0, 200, 0), (700, 200, 125, 50), 5)
        window.blit(t_x, (720, 210))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()

if __name__ == "__main__":
    main()