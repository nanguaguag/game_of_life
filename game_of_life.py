import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1400, 800), 0, 32)

blue = (0, 0, 255)
s_dead = set([])
length = 20
run = False
clock = pygame.time.Clock()
speed = 20

abc = '''
bob2o$5o$2o3bo$3b2o$3b2o$6b4o$5bo3bo$4b2o2b2o$o2bo3bo$7o2$7o$o2bo3bo$
4b2o2b2o$5bo3bo$6b4o$3b2o$3b2o$2o3bo$5o$bob2o!
'''

s_alive = set([])
x = 0
y = 0
for count in range(len(abc)):
    q = abc[count]
    t = abc[count-1]
    e = abc[count-2]
    if q == '$':
        try:
            try:
                y += int(e)*length*10+int(t)*length
                x = 0
            except ValueError:
                y += int(t)*length
                x = 0
        except ValueError:
            y += length
            x = 0
    elif q == 'b':
        try:
            try:
                x += int(e)*length*10+int(t)*length
            except ValueError:
                x += int(t)*length
        except ValueError:
            x += length
    elif q == 'o':
        try:
            try:
                for p in range(int(e)*10+int(t)):
                    x += length
                    s_alive.add((x,y))
            except ValueError:
                for p in range(int(t)):
                    x += length
                    s_alive.add((x,y))
        except ValueError:
            x += length
            s_alive.add((x,y))

def live(x,y):
    live = 0
    if (x-length,y-length) in s_alive:
        live += 1
    if (x,y-length) in s_alive:
        live += 1
    if (x+length,y-length) in s_alive:
        live += 1
    if (x-length,y+length) in s_alive:
        live += 1
    if (x,y+length) in s_alive:
        live += 1
    if (x+length,y+length) in s_alive:
        live += 1
    if (x-length,y) in s_alive:
        live += 1
    if (x+length,y) in s_alive:
        live += 1
    return live

while True:
    pos = pygame.mouse.get_pos()
    pos_x,pos_y = pos[0]//length*length,pos[1]//length*length

    for event in pygame.event.get():
        if event.type == QUIT:
           exit()
        if event.type == MOUSEBUTTONDOWN:
            if (pos_x,pos_y) in s_alive:
                s_alive.remove((pos_x,pos_y))
            else:
                s_alive.add((pos_x,pos_y))
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
               run = not run
            if event.key == K_BACKSPACE:
               s_dead.clear()
               s_alive.clear()
            if event.key == K_RIGHT:
               speed += 2
            if event.key == K_LEFT:
               speed -= 2
    for x,y in s_alive:
        if (x-length,y-length) not in s_alive:
            s_dead.add((x-length,y-length))
        if (x,y-length) not in s_alive:
            s_dead.add((x,y-length))
        if (x+length,y-length) not in s_alive:
            s_dead.add((x+length,y-length))
        if (x-length,y+length) not in s_alive:
            s_dead.add((x-length,y+length))
        if (x,y+length) not in s_alive:
            s_dead.add((x,y+length))
        if (x+length,y+length) not in s_alive:
            s_dead.add((x+length,y+length))
        if (x-length,y) not in s_alive:
            s_dead.add((x-length,y))
        if (x+length,y) not in s_alive:
            s_dead.add((x+length,y))
    screen.fill((0,0,0))

    for count in s_alive:
        pygame.draw.rect(screen, blue, Rect(count,(length,length)))
    if run:
        l_alive = list(s_alive)
        for q in s_alive:
            liv_ = live(*q)
            if (liv_ > 3) or (liv_ < 2):
                l_alive.remove(q)
        for p in s_dead:
            liv = live(*p)
            if liv == 3:
                l_alive.append(p)
        s_alive = set(l_alive)
        s_dead.clear()

    pygame.display.update()
    clock.tick(speed)


#       [][]
#       [][]



#       []
#     [][][]
#   []      []
# []  [][][]  []
#   [][][][][]




#             [][][]
#                 []
#               []






#         [][][]
#       []      []
#     []          []
#     [][]  []  [][]


#           []
#         []  []
#         []  []
#           []

#           [][]
#           [][]

#bleeder
# 38b4o$37bo3bo12bo2bo$41bo16bo$37bo2bo13bo3bo$55b4o2$31bo$32bo18bobo$
# 30b3o12b3ob2o3bo$42b2o4b4obob2o$40b2o5b5o4bo$26bo13b2o4bo5bo3bo$27bo
# 12b5o8b3o$25b3o14b2o9bo$13b5o$12bo4bo29b2o5bo2bo$17bo3bo24b4o8bo$12bo
# 3bo5bo23b2ob2o3bo3bo$14bo5b3o18b2o5b2o5b4o$30bo8b2ob2o$28bobo4bo3b4o$
# 16bo10bo2bo5bo3b2o$17bo9bo6bo2bo32b2o5b4o$15b3o9bo2bo5bo3b2o26b2ob2o3b
# o3bo$28bobo4bo3b4o25b4o8bo$30bo8b2ob2o25b2o5bo2bo$41b2o$64b2o9bo$30b2o
# 30b5o8b3o$29b4o29b2o4bo5bo3bo$29b2ob2o28b2o5b5o4bo$31b2o31b2o4b4obob2o
# $67b3ob2o3bo$73bobo2$53bo$bo49b2o24b4o$2bo49b2o22bo3bo$3o56b4o17bo12b
# 2o$58bo3bo13bo2bo11b2ob2o13b2o$38bo23bo28b4o13b4o$36b2o20bo2bo30b2o14b
# 2ob2o$5b2o30b2o12bo2bo55b2o$5b2o31bo16bo$38b2o11bo3bo$7b2o14bo16bo11b
# 4o35bo4b2o$7b3o11b2o12bo7b2o2b3o32bo7b3o3b2o9b2o$6b2obo5b2o5b2o10bo8b
# 2o2b3o33b2o4b2ob2o12bo2bo$6bo8b2o18bo7b2o2b3o12b3o17b2o4b3ob3o11bo2b2o
# $5b2o33bo11b4o5b5o22b3ob2o11bo2b2o$6b2o30b2o11bo3bo5b3ob2o23bobo12b4o$
# 4bo50bo8b2o11bo$5bo45bo2bo23b2o$76bob2o8b2o19b2o$75bo2bo7b2ob2o9b4o4b
# 4o$82bo3b4o9bo3bo4b2ob2o$9bo29bo26bo7bo2bo5bo3b2o14bo6b2o$8bobo5b2o20b
# obo5b2o16b5o5bo6bo2bo14bo2bo$8bobo4bobo20bobo4bobo16b2ob3o4bo2bo5bo3b
# 2o$9bo5b2o22bo5b2o17b5o6bobo4bo3b4o$66bo10bo8b2ob2o$88b2o5$90b2o$68bo
# 10bo8b2ob2o$11bo5b2o22bo5b2o17b5o6bobo4bo3b4o$10bobo4bobo20bobo4bobo
# 16b2ob3o4bo2bo5bo3b2o$10bobo5b2o20bobo5b2o16b5o5bo6bo2bo14bo2bo$11bo
# 29bo26bo7bo2bo5bo3b2o14bo6b2o$84bo3b4o9bo3bo4b2ob2o$77bo2bo7b2ob2o9b4o
# 4b4o$78bob2o8b2o19b2o$7bo45bo2bo23b2o$6bo50bo8b2o11bo$8b2o30b2o11bo3bo
# 5b3ob2o23bobo12b4o$7b2o33bo11b4o5b5o22b3ob2o11bo2b2o$8bo8b2o18bo7b2o2b
# 3o12b3o17b2o4b3ob3o11bo2b2o$8b2obo5b2o5b2o10bo8b2o2b3o33b2o4b2ob2o12bo
# 2bo$9b3o11b2o12bo7b2o2b3o32bo7b3o3b2o9b2o$9b2o14bo16bo11b4o35bo4b2o$
# 40b2o11bo3bo$7b2o31bo16bo$7b2o30b2o12bo2bo55b2o$38b2o20bo2bo30b2o14b2o
# b2o$4bo35bo23bo28b4o13b4o$4b2o54bo3bo13bo2bo11b2ob2o13b2o$3bobo55b4o
# 17bo12b2o$54b2o22bo3bo$53b2o24b4o$55bo2$75bobo$69b3ob2o3bo$33b2o31b2o
# 4b4obob2o$31b2ob2o28b2o5b5o4bo$31b4o29b2o4bo5bo3bo$32b2o30b5o8b3o$66b
# 2o9bo$44b4o$19bo12bo10bo3bo23b2o5bo2bo$19b2o10bobo4b2o7bo22b4o8bo$18bo
# bo8b2o2bo3b4o2bo2bo23b2ob2o3bo3bo$27b2obo5bo3b2o30b2o5b4o$29b2o2bo3b4o
# 2bo2bo$24bo6bobo4b2o7bo$24b2o6bo10bo3bo12b2o$18bo4bobo18b4o3b4o4b4o$
# 16bo3bo29bo3bo4b2ob2o$21bo32bo6b2o$16bo4bo7bo20bo2bo$17b5o7b2o$28bobo$
# 42b3o13b2o$41b4o13bobo$34bo6bo3bo12bob2o$34b2o6b3o14b2o$33bobo6b3o3b2o
# 9bo$48b2o2$60b2o$59b4o$59b2ob2o$44b2o15b2o$42b2ob2o$42b4o$43b2o!

# gun
# 3b2o$3b2o4$3bo$2b3o$bo3bo$ob3obo$b5o5$6b3o$8bo$7bo7$4b3o$3bo3bo$2bo5bo
# $2b2obob2o3$5bo$4bobo$4bobo$5bo2$5b2o$5b2o!

# gun*3
# 13b2o$11bo2bo2$10bo2$11b2o$13bo3$10b2o3b2o$10b2o3b2o$11b5o$12bobo2$12b
# 3o9$11bo$10b3o$9b5o$8b2o3b2o4$10b3o$10b3o2$9bo$8bobo$7bo3bo$8b3o$6b2o
# 3b2o5$7bo$7bo$7bob3o2$12bo$9bob2o$9b2o3$4b2o3b2o$4b2o3b2o$5b5o$6bobo2$
# 6b3o6$10bo$11bo$9b3o$5bo$4b3o$3b5o$2b2o3b2o4$4b3o$4b3o2$3bo$2bobo$bo3b
# o$2b3o$2o3b2o!

# big_gun
# 39b2o$37bo2bo$36bo15bobo$24bo11bo10b3o2bo3bo$24b4o8bo19bo$8bo16b4o8bo
# 2bo2b2o7bo4bo$7bobo5b2o8bo2bo10b2o2bo2bobo7bo$5b2o3bo14b4o15b3o5bo3bo
# 3b2o$2o3b2o3bo4bobob2o3b4o24bobo5bobo$2o3b2o3bo5b2o3bo2bo37bo$7bobo10b
# o41b2o$8bo8bo2bo16bo$36bo$36b3o2$27bo$28bo$26b3o5$12b2o$13bo$13bobo4bo
# 9b2o$14b2o3bobo7b4o$18bob2o5b3o2bo2bobo$17b2ob2o9b2o2bo2bo$18bob2o6bo
# 9b2o6b2o$19bobo5bo8bo3b2o4b2o$20bo6bo10b2o$35bo2bo$35bobo!

# move_gun
# 2b2o$2ob2o13b2o$4o13b4o$b2o14b2ob2o$19b2o4$16b2o$10b3o3bobo$7b3o6bob2o
# $7bo9b2o$7b3o7bo3$18b2o$9b4o4b4o$8bo3bo4b2ob2o$12bo6b2o$8bo2bo!

# slow_ship
# 7bo$4b5o$bobo5bo$2bob2o2bo$6b2o$bo$2obo$bo2bo$bo2bo$2b2o!

# slower_ship
# bob2o$5o$2o3bo$3b2o$3b2o$6b4o$5bo3bo$4b2o2b2o$o2bo3bo$7o2$7o$o2bo3bo$
# 4b2o2b2o$5bo3bo$6b4o$3b2o$3b2o$2o3bo$5o$bob2o!
