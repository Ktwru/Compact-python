import pygame
import sys
import spiral

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
    window = pygame.display.set_mode((850, 600))
    window.fill((202, 151, 39))
    folded_snake_xray = pygame.Surface((500, 500))
    folded_snake_pic = pygame.Surface((500, 500))
    folded_snake_xray.fill((202, 151, 39))
    folded_snake_pic.fill((202, 151, 39))
    text = ['Python length:', 'fold', 'X-ray']
    font = pygame.font.Font('PixelFont.ttf', 36)
    lenghtX = 260
    python_lenght = 1
    xray = 0
    part_pic = pygame.image.load('media/part.png')
    head_pic = pygame.image.load('media/head.png')
    angle_pic = pygame.image.load('media/angle.png')
    tail_pic = pygame.image.load('media/tail.png')

    pygame.display.update()
    while True:
        buttondown = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                buttondown = 1
        pygame.time.delay(20)
        if xray == 0:
            colors = [(202, 151, 39), (0, 0, 0), (255, 255, 255)]
        else:
            colors = [(0, 0, 0), (255, 255, 255), (0, 0, 0)]
        window.fill(colors[0])
        pos = pygame.mouse.get_pos()
        mos = pygame.mouse.get_pressed()[0]
        t_p_l = font.render(text[0], 0, colors[1])
        window.blit(t_p_l, (15, 30))
        lenght = pygame.draw.rect(window, colors[1], (270, 43, 450, 5))
        pygame.draw.rect(window, colors[1], (lenghtX-10, 33, 20, 20))
        if pos[0] >= lenght.left and pos[0] <= lenght.left + lenght.width and pos[1] >= 5 and pos[1] <= 70:
            if mos:
                lenghtX = pos[0]
                pygame.draw.rect(window, (255, 5, 255), (lenghtX-10, 33, 20, 20))
                python_lenght = lenghtX - lenght.left
                if python_lenght == 0:
                    python_lenght = 1
        pygame.draw.rect(window, colors[2], (740, 21, 85, 50))
        pygame.draw.rect(window, colors[1], (740, 21, 85, 50), 5)
        num_p_l = font.render(str(python_lenght), 0, colors[1])
        window.blit(num_p_l, (760, 30))


        pygame.draw.rect(window, colors[2], (700, 100, 125, 50))
        pygame.draw.rect(window, colors[1], (700, 100, 125, 50), 5)
        if pos[0] >= 700 and pos[0] <= 825 and pos[1] >= 100 and pos[1] <= 150:
            pygame.draw.rect(window, (0, 200, 0), (700, 100, 125, 50), 5)
            if buttondown:
                mat = spiral.spiral(python_lenght)
                matrix_side = mat[1]
                matrix = mat[0]
                part_cords = [0, 0]
                part_size = 500//matrix_side
                if matrix_side <= 3:
                    coef = 1
                else:
                    coef = 2
                part_font_size = coef * (500//matrix_side)//len(str(python_lenght))
                folded_snake_xray.fill((0, 0, 0))
                folded_snake_pic.fill((202, 151, 39))
                part_font = pygame.font.Font('PixelFont.ttf', part_font_size)
                part_pic_sized = pygame.transform.scale(part_pic, (part_size, part_size))
                head_pic_sized = pygame.transform.scale(head_pic, (part_size, part_size))
                tail_pic_sized = pygame.transform.scale(tail_pic, (part_size, part_size))
                angle_pic_sized = pygame.transform.scale(angle_pic, (part_size, part_size))
                rot = 0

                angles = [2, 3]
                dif = 2
                while angles[-1] < python_lenght:
                    for i in range(2):
                        angles.append(angles[-1] + dif)
                    dif += 1

                for y in range(len(matrix)):
                    for x in matrix[y]:
                        folded_snake_xray.blit(part_font.render((str(x)), 0, (255, 255, 255)), (part_cords[0], part_cords[1]))
                        if x == 1:
                            folded_snake_pic.blit(head_pic_sized, (part_cords[0], part_cords[1]))
                        elif x == python_lenght:
                            if y == matrix_side-1 and matrix[y].index(x) != 0:
                                tail_pic_sized = pygame.transform.rotate(tail_pic_sized, 180)
                                print(1)
                            elif matrix[y].index(x) == matrix_side-1 and y != matrix_side-1:
                                tail_pic_sized = pygame.transform.rotate(tail_pic_sized, 270)
                                print(2)
                            elif matrix[y].index(x) == 0 and y > 1 :
                                tail_pic_sized = pygame.transform.rotate(tail_pic_sized, 90)
                                print(3, x, y)

                            folded_snake_pic.blit(tail_pic_sized, (part_cords[0], part_cords[1]))
                        elif x in range(2, python_lenght):
                            if x in angles:
                                angle_pic_sized_rotated = pygame.transform.rotate(angle_pic_sized, angles.index(x)*90)
                                folded_snake_pic.blit(angle_pic_sized_rotated, (part_cords[0], part_cords[1]))
                            else:
                                if x in matrix[y][rot:matrix_side-rot]:
                                    part_pic_sized_rotated = part_pic_sized
                                else:
                                    part_pic_sized_rotated = pygame.transform.rotate(part_pic_sized, 90)
                                folded_snake_pic.blit(part_pic_sized_rotated, (part_cords[0], part_cords[1]))
                        part_cords[0] += part_size
                    if y < matrix_side//2:
                        rot += 1
                    else:
                        rot -= 1
                    part_cords[1] += part_size
                    part_cords[0] = 0
        t_f = font.render(text[1], 0, colors[1])
        window.blit(t_f, (730, 110))
        pygame.draw.rect(window, colors[2], (700, 200, 125, 50))
        if xray == 0:
            pygame.draw.rect(window, colors[1], (700, 200, 125, 50), 5)
        else:
            pygame.draw.rect(window, (0, 200, 0), (700, 200, 125, 50), 5)
        if pos[0] >= 700 and pos[0] <= 825 and pos[1] >= 200 and pos[1] <= 250:
            if buttondown and xray == 0:
                xray = 1
            elif buttondown and xray == 1:
                xray = 0
            pygame.draw.rect(window, (0, 200, 0), (700, 200, 125, 50), 5)
        t_x = font.render(text[2], 0, colors[1])
        window.blit(t_x, (720, 210))
        if xray == 1:
            window.blit(folded_snake_xray, (50, 80))
        else:
            window.blit(folded_snake_pic, (50, 80))
        pygame.display.update()

if __name__ == "__main__":
    main()