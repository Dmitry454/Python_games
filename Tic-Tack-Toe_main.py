import pygame as pg
import sys

# здесь определяются константы,
# классы и функции
FPS = 2
flag = True # regulator of the main loop
# Определим переменные-константы для цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
# Координаты вершин сетки
x0 = 150
x1 = 250
x2 = 350
x3 = 450
y0 = 50
y1 = 150
y2 = 250
y3 = 350

x0_y0_free = True
x1_y0_free = True
x2_y0_free = True
x0_y1_free = True
x1_y1_free = True
x2_y1_free = True
x0_y2_free = True
x1_y2_free = True
x2_y2_free = True

is_correct = False
#counter = 0 # variable, which should count number of actions
# a list, which will be used for checking the situation
# C = [[0(x0), 0(x1), 0(x2)](y0), [0(x0), 0(x1), 0(x2)](y1), [0(x0), 0(x1), 0(x2)](y2)]
C = [[1, 1, 1] for i in range(3)]

def three_elem_the_same(a, b, c, cross_the_first):
    if a == b == c:
        if cross_the_first == True:
            pg.quit()
            flag = False
            print('The winner is x')
        elif cross_the_first == False:
            pg.quit()
            flag = False
            print('The winner is 0')


def draw_circle(x, y):
    """The function recieves coordinates (x, y) of the left top point of the square"""
    pg.draw.circle(sc, LIGHT_BLUE, [x + 50, y + 50] , 40)
    pg.draw.circle(sc, BLACK, [x + 50, y + 50], 35)


def draw_cross(x, y):
    """The function recieves coordinates (x, y) of the left top point of the square"""
    pg.draw.aaline(sc, GREEN, [x + 20, y + 20], [x + 80, y + 80])
    pg.draw.aaline(sc, GREEN, [x + 20, y + 80], [x + 80, y + 20])


def draw_field():
    # рисуем рамку игровой доски (толщина рамки - 4 пикселя)
    pg.draw.rect(sc, WHITE, (150, 50, 300, 300), 4)

    # рисуем вертикальные границы полей
    pg.draw.aaline(sc, WHITE, [250, 50], [250, 350])
    pg.draw.aaline(sc, WHITE, [350, 50], [350, 350])

    # горизонтальный вертикальные границы полей
    pg.draw.aaline(sc, WHITE, [150, 150], [450, 150])
    pg.draw.aaline(sc, WHITE, [150, 250], [450, 250])


# здесь происходит инициация,
# создание объектов
while is_correct == False:
    k = input("Who is the first (print x or 0)? ")
    if k == 'x':
        cross_the_first = True
        is_correct = True
    elif k == '0':
        cross_the_first = False
        is_correct = True
    else:
        print('incorrect symbol, try again.')

pg.init()
sc = pg.display.set_mode((600, 400))
clock = pg.time.Clock()

draw_field()
pg.display.update()

# главный цикл
while flag:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:

                if (i.pos[0] > x0 and i.pos[0] < x1 and i.pos[1] > y0 and i.pos[1] < y1 and x0_y0_free):

                    if cross_the_first:
                        draw_cross(x0, y0)
                        cross_the_first = False
                        C[0][0] = 'x'

                    else:
                        draw_circle(x0, y0)
                        cross_the_first = True
                        C[0][0] = 0

                    x0_y0_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][0], C[0][1], C[0][2], not cross_the_first)
                    three_elem_the_same(C[0][0], C[1][0], C[2][0], not cross_the_first)
                    three_elem_the_same(C[0][0], C[1][1], C[2][2], not cross_the_first)

                elif (i.pos[0] > x1 and i.pos[0] < x2 and i.pos[1] > y0 and i.pos[1] < y1 and x1_y0_free):

                    if cross_the_first:
                        draw_cross(x1, y0)
                        cross_the_first = False
                        C[0][1] = 'x'
                    else:
                        draw_circle(x1, y0)
                        cross_the_first = True
                        C[0][1] = 0

                    x1_y0_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][0], C[0][1], C[0][2], not cross_the_first)
                    three_elem_the_same(C[0][1], C[1][1], C[2][1], not cross_the_first)

                elif (i.pos[0] > x2 and i.pos[0] < x3 and i.pos[1] > y0 and i.pos[1] < y1 and x2_y0_free):

                    if cross_the_first:
                        draw_cross(x2, y0)
                        cross_the_first = False
                        C[0][2] = 'x'
                    else:
                        draw_circle(x2, y0)
                        cross_the_first = True
                        C[0][2] = 0

                    x2_y0_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][0], C[0][1], C[0][2], not cross_the_first)
                    three_elem_the_same(C[0][2], C[1][2], C[2][2], not cross_the_first)
                    three_elem_the_same(C[0][2], C[1][1], C[2][0], not cross_the_first)

                elif (i.pos[0] > x0 and i.pos[0] < x1 and i.pos[1] > y1 and i.pos[1] < y2 and x0_y1_free):

                    if cross_the_first:
                        draw_cross(x0, y1)
                        cross_the_first = False
                        C[1][0] = 'x'
                    else:
                        draw_circle(x0, y1)
                        cross_the_first = True
                        C[1][0] = 0

                    x0_y1_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][0], C[1][0], C[2][0], not cross_the_first)
                    three_elem_the_same(C[1][0], C[1][1], C[1][2], not cross_the_first)

                elif (i.pos[0] > x1 and i.pos[0] < x2 and i.pos[1] > y1 and i.pos[1] < y2 and x1_y1_free):

                    if cross_the_first:
                        draw_cross(x1, y1)
                        cross_the_first = False
                        C[1][1] = 'x'
                    else:
                        draw_circle(x1, y1)
                        cross_the_first = True
                        C[1][1] = 0
                    x1_y1_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][1], C[1][1], C[2][1], not cross_the_first)
                    three_elem_the_same(C[1][0], C[1][1], C[1][2], not cross_the_first)
                    three_elem_the_same(C[0][0], C[1][1], C[2][2], not cross_the_first)
                    three_elem_the_same(C[2][0], C[1][1], C[0][2], not cross_the_first)

                elif (i.pos[0] > x2 and i.pos[0] < x3 and i.pos[1] > y1 and i.pos[1] < y2 and x2_y1_free):

                    if cross_the_first:
                        draw_cross(x2, y1)
                        cross_the_first = False
                        C[1][2] = 'x'
                    else:
                        draw_circle(x2, y1)
                        cross_the_first = True
                        C[1][2] = 0
                    x2_y1_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][2], C[1][2], C[2][2], not cross_the_first)
                    three_elem_the_same(C[1][0], C[1][1], C[1][2], not cross_the_first)

                elif (i.pos[0] > x0 and i.pos[0] < x1 and i.pos[1] > y2 and i.pos[1] < y3 and x0_y2_free):

                    if cross_the_first:
                        draw_cross(x0, y2)
                        cross_the_first = False
                        C[2][0] = 'x'
                    else:
                        draw_circle(x0, y2)
                        cross_the_first = True
                        C[2][0] = 0
                    x0_y2_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][0], C[1][0], C[2][0], not cross_the_first)
                    three_elem_the_same(C[2][0], C[1][1], C[0][2], not cross_the_first)
                    three_elem_the_same(C[2][0], C[2][1], C[2][2], not cross_the_first)

                elif (i.pos[0] > x1 and i.pos[0] < x2 and i.pos[1] > y2 and i.pos[1] < y3 and x1_y2_free):

                    if cross_the_first:
                        draw_cross(x1, y2)
                        cross_the_first = False
                        C[2][1] = 'x'
                    else:
                        draw_circle(x1, y2)
                        cross_the_first = True
                        C[2][1] = 0
                    x1_y2_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][1], C[1][1], C[2][1], not cross_the_first)
                    three_elem_the_same(C[2][0], C[2][1], C[2][2], not cross_the_first)

                elif (i.pos[0] > x2 and i.pos[0] < x3 and i.pos[1] > y2 and i.pos[1] < y3 and x2_y2_free):

                    if cross_the_first:
                        draw_cross(x2, y2)
                        cross_the_first = False
                        C[2][2] = 'x'
                    else:
                        draw_circle(x2, y2)
                        cross_the_first = True
                        C[2][2] = 0
                    x2_y2_free = False
                    pg.display.update()
                    three_elem_the_same(C[0][2], C[1][2], C[2][2], not cross_the_first)
                    three_elem_the_same(C[0][0], C[1][1], C[2][2], not cross_the_first)
                    three_elem_the_same(C[2][0], C[2][1], C[2][2], not cross_the_first)


        if i.type == pg.MOUSEBUTTONUP and i.button == 1:
            pass
