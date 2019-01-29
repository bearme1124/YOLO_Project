# KMJ
# Created on Thu Jan 10 16:13:02 2019
# use Image Module - Pillow
import PIL.Image as pilimg
import PIL.ImageDraw as imdraw
import random
import math

Repeat = 30 # number of jpg
Obj = 5 # number of object
arr = [0, 0, 0, 0]
cnt = 0


# make_random number from a to b    
def ran(a, b):
    return random.randint(a, b)

# Rotate Rectangle by angle 'theta'
def rot(li, t):
    # rotate angle
    theta = ran(0, t)
    
    the = math.radians(int(theta))
    co = math.cos(the)
    si = math.sin(the)

    # (x, y) is standard of rotating
    rotxy = [[0,0],[0,0],[0,0],[0,0]]
    rotxy[0][0] = li[0][0]
    x = li[0][0]
    
    rotxy[0][1] = li[0][1]
    y = li[0][1]
    
    # 2D Rotation by (x, y)
    for p in range(1, 4):
        rotxy[p][0] = li[p][0] * co - li[p][1] * si + x * (1 - co) + y * si
        rotxy[p][1] = li[p][0] * si + li[p][1] * co + y * (1 - co) - x * si
    return rotxy

#    So We don't need rotation of picture itself    
#    ex) image = image.rotate(45)

def get_center(a, b):
    return a + (b-a)/2
def get_len(a, b):
    return b - a
def trans(x):
    return int(x*1000000)/1000000

def make_txt_C(x, y, w, h):
    x = trans(x)
    y = trans(y)
    w = trans(w)
    h = trans(h)
    
    text = open('/home/a/python_MakeExample/txtfiles/C/t%s.txt' %cnt, 'a')
    text.write('0 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/Q/t%s.txt' %cnt, 'a')
    text.write('1 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/T/t%s.txt' %cnt, 'a')
    text.write('1 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/CQT/t%s.txt' %cnt, 'a')
    text.write('0 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')
    
    text.close()
def make_txt_R(x, y, w, h):
    x = trans(x)
    y = trans(y)
    w = trans(w)
    h = trans(h)
    
    text = open('/home/a/python_MakeExample/txtfiles/C/t%s.txt' %cnt, 'a')
    text.write('1 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/Q/t%s.txt' %cnt, 'a')
    text.write('0 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/T/t%s.txt' %cnt, 'a')
    text.write('1 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/CQT/t%s.txt' %cnt, 'a')
    text.write('1 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')
    
    text.close()
def make_txt_T(x, y, w, h):
    x = trans(x)
    y = trans(y)
    w = trans(w)
    h = trans(h)
    
    text = open('/home/a/python_MakeExample/txtfiles/C/t%s.txt' %cnt, 'a')
    text.write('1 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/Q/t%s.txt' %cnt, 'a')
    text.write('1 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/T/t%s.txt' %cnt, 'a')
    text.write('0 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')

    text = open('/home/a/python_MakeExample/txtfiles/CQT/t%s.txt' %cnt, 'a')
    text.write('2 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n')
    
    text.close()
    
def get_txt(x1, x2, x3, x4, y1, y2, y3, y4):
        mina = min(x1, x2, x3, x4)
        maxa = max(x1, x2, x3, x4)
        minb = min(y1, y2, y3, y4)
        maxb = max(y1, y2, y3, y4)
        arr =  box(get_center(mina, maxa), get_center(minb, maxb),\
                   get_len(mina, maxa), get_len(minb, maxb))
        make_txt_R(arr[0],arr[1],arr[2],arr[3]) 
    
def box(x, y, w, h):
    s = [0, 0, 0, 0]
    s[0] = x / 900
    s[1] = y / 532
    s[2] = (w+5) / 900 
    s[3] = (h+5) / 532
    return s

def check_size(x1, x2, x3, x4, y1, y2, y3, y4):
    if(x1 > 900 or x2 > 900 or x3 > 900 or x4 > 900\
       or y1 > 532 or y2 > 532 or y3 > 532 or y4 > 532\
       or x1 < 0 or x2 < 0 or x3 < 0 or x4 < 0\
       or y1 < 0 or y2 < 0 or y3 < 0 or y4 < 0):
        return 0
    else:
        return 1
    
def circle(n):
    for i in range(n):
        center_x = random.randint(30, 870)
        center_y = random.randint(30, 500)
        comparexy = [900-center_x, center_x, 532-center_y, center_y]
        r = random.randint(25, min(comparexy))
        
        draw.ellipse((center_x, center_y, center_x+r, center_y+r), outline='black')
        
        arr = box(center_x+r/2, center_y+r/2, r, r)
        make_txt_C(arr[0],arr[1],arr[2],arr[3])
        

def triangle(n):
    for i in range(n):
        a1 = ran(11, 889)
        b1 = ran(11, 521)
        a2 = ran(11, 889)
        b2 = ran(11, 521)
        a3 = ran(11, 889)
        b3 = ran(11, 521)
        draw.polygon(((a1, b1), (a2, b2), (a3, b3)), outline = 'black')
        
        mina = min(a1, a2, a3)
        maxa = max(a1, a2, a3)
        minb = min(b1, b2, b3)
        maxb = max(b1, b2, b3)
        arr =  box(get_center(mina, maxa), get_center(minb, maxb),\
                   get_len(mina, maxa), get_len(minb, maxb))
        make_txt_T(arr[0],arr[1],arr[2],arr[3])        
        
# number of normal is 'n', number of rotated is 'm'
def square(n, m):
    for i in range(n):
        x1 = ran(11, 889)
        y1 = ran(11, 521)
        r = ran(10, min(900-x1, 532-y1))
        draw.polygon(((x1,y1),(x1+r,y1),(x1+r,y1+r),(x1,y1+r)), outline = 'black')
        
        arr = box(x1+r/2, y1+r/2, r, r)
        make_txt_R(arr[0], arr[1], arr[2], arr[3])
        
    j = 0
    while j < m:
        x1 = ran(11, 889)
        y1 = ran(11, 521)
        r = ran(10, min(900-x1, 532-y1))
        xy = [[x1,y1],[x1+r,y1],[x1+r,y1+r],[x1,y1+r]]
        xy = rot(xy, 89)
        if(check_size(xy[0][0],xy[1][0],xy[2][0],xy[3][0],xy[0][1],xy[1][1],xy[2][1],xy[3][1]) == 1):
            draw.polygon(((xy[0][0],xy[0][1]),(xy[1][0],xy[1][1]),\
                          (xy[2][0],xy[2][1]),(xy[3][0],xy[3][1])), outline = 'black')

            get_txt(xy[0][0], xy[1][0], xy[2][0], xy[3][0],\
                    xy[0][1], xy[1][1], xy[2][1], xy[3][1])
            j += 1
        
def rectangle(n, m):
    for i in range(n):
        x1 = ran(11, 879)
        y1 = ran(11, 510)
        x2 = ran(x1+1, 889)
        y2 = ran(y1+1, 521)
        draw.rectangle(((x1, y1), (x2, y2)), outline = 'black')
        
        arr = box(get_center(x1, x2), get_center(y1, y2),\
                  get_len(x1, x2), get_len(y1, y2))
        make_txt_R(arr[0], arr[1], arr[2], arr[3])
        
    j = 0
    while j < m:
        x1 = ran(11, 879)
        y1 = ran(11, 510)
        x2 = ran(x1+1, 889)
        y2 = ran(y1+1, 521)    
        # coordinate 
        xy = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
        #rotate
        xy = rot(xy, 89)
        
        if(check_size(xy[0][0],xy[1][0],xy[2][0],xy[3][0],xy[0][1],xy[1][1],xy[2][1],xy[3][1]) == 1):        
            draw.polygon(((xy[0][0],xy[0][1]),(xy[1][0],xy[1][1]),\
                          (xy[2][0],xy[2][1]),(xy[3][0],xy[3][1])), outline = 'black')
            
            get_txt(xy[0][0], xy[1][0], xy[2][0], xy[3][0],\
                    xy[0][1], xy[1][1], xy[2][1], xy[3][1])
            j += 1
            
def trapezoid(n, m):
    for i in range(n):
        x1 = ran(30, 870)
        y1 = ran(30, 500)
        a = ran(10, 890-x1)
        h = ran(10, 522-y1)
        b = ran(2, int(a/2)-1)
        draw.polygon(((x1,y1),(x1+a,y1),(x1+a-b,y1+h),(x1+b,y1+h)), outline = 'black')
        get_txt(x1, x1+a, x1+a-b, x1+b, y1, y1, y1+h, y1+h)
        
    j = 0
    while j < m:
        x1 = ran(30, 870)
        y1 = ran(30, 500)
        a = ran(10, 890-x1)
        h = ran(10, 522-y1)
        b = ran(2, int(a/2)-2)
        xy = [[x1,y1],[x1+a,y1],[x1+a-b,y1+h],[x1+b,y1+h]]
        xy = rot(xy, 179)
        if(check_size(xy[0][0],xy[1][0],xy[2][0],xy[3][0],xy[0][1],xy[1][1],xy[2][1],xy[3][1]) == 1):
            draw.polygon(((xy[0][0],xy[0][1]),(xy[1][0],xy[1][1]),\
                          (xy[2][0],xy[2][1]),(xy[3][0],xy[3][1])), outline = 'black')
            get_txt(xy[0][0], xy[1][0], xy[2][0], xy[3][0],\
                    xy[0][1], xy[1][1], xy[2][1], xy[3][1])
            j += 1
        
def paralleogram(n,m):
    for i in range(n):
        x1 = ran(40, 860)
        y1 = ran(40, 490)
        a = ran(10, 880-x1)
        b = ran(2, 890-(x1+a))
        h = ran(10, 511-y1)
        draw.polygon(((x1,y1),(x1+a,y1),(x1+a+b,y1+h),(x1+b,y1+h)), outline = 'black')
        get_txt(x1, x1+a, x1+a+b, x1+b, y1, y1, y1+h, y1+h)
        
    j = 0
    while j < m:
        x1 = ran(40, 860)
        y1 = ran(40, 490)
        a = ran(10, 880-x1)
        b = ran(2, 890-(x1+a))
        h = ran(10, 511-y1)
        xy = [[x1,y1],[x1+a,y1],[x1+a+b,y1+h],[x1+b,y1+h]]
        xy = rot(xy, 180)
        if(check_size(xy[0][0],xy[1][0],xy[2][0],xy[3][0],xy[0][1],xy[1][1],xy[2][1],xy[3][1]) == 1):
            draw.polygon(((xy[0][0],xy[0][1]),(xy[1][0],xy[1][1]),\
                          (xy[2][0],xy[2][1]),(xy[3][0],xy[3][1])), outline = 'black')    
            get_txt(xy[0][0], xy[1][0], xy[2][0], xy[3][0],\
                    xy[0][1], xy[1][1], xy[2][1], xy[3][1])
            j += 1

def rhombus(n,m):
    for i in range(n):
        x1 = ran(100, 800)
        y1 = ran(50, 480)
        a = ran(50, 880-x1)
        b = ran(20, min(510-y1, y1))
        draw.polygon(((x1,y1),(x1+a/2,y1-b),(x1+a,y1),(x1+a/2,y1+b)), outline = 'black')
        get_txt(x1, x1+a/2, x1+a, x1+a/2, y1, y1-b, y1, y1+b)
        
        
    j = 0
    while j < m:
        x1 = ran(100, 800)
        y1 = ran(50, 480)
        a = ran(50, 880-x1)
        b = ran(20, min(510-y1, y1))
        xy = [[x1,y1],[x1+a/2,y1-b],[x1+a,y1],[x1+a/2,y1+b]]    
        xy = rot(xy, 79)
        if(check_size(xy[0][0],xy[1][0],xy[2][0],xy[3][0],xy[0][1],xy[1][1],xy[2][1],xy[3][1]) == 1):
            draw.polygon(((xy[0][0],xy[0][1]),(xy[1][0],xy[1][1]),\
                          (xy[2][0],xy[2][1]),(xy[3][0],xy[3][1])), outline = 'black')    
            get_txt(xy[0][0], xy[1][0], xy[2][0], xy[3][0],\
                    xy[0][1], xy[1][1], xy[2][1], xy[3][1])
            j += 1
        
### circle        
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    circle(2)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    circle(4)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
        
### triangle
for k in range(500):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(2)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1    

### square
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(1,0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(0,1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1    
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(1, 0)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(0, 1)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(1, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1    

### rectangle
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(1,0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(0,1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(1, 0)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(0, 1)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(1, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
    
### trapezoid
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(1,0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(0,1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(1, 0)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(0, 1)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(1, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1

###paralleogram
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    paralleogram(1,0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    paralleogram(0,1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1  
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    paralleogram(1, 0)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    paralleogram(0, 1)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    paralleogram(1, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
    
###rhombus
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rhombus(1,0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rhombus(0,1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rhombus(1, 0)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(100):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rhombus(0, 1)
    circle(1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rhombus(1, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
    
#### triangle
    
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    square(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    rectangle(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    trapezoid(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    paralleogram(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    rhombus(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1

#### triangle rotate 
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    square(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    rectangle(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    trapezoid(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    paralleogram(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    triangle(1)
    circle(1)
    rhombus(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1  
    
#### square 
    
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(1, 0)
    circle(1)
    rectangle(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(1, 0)
    circle(1)
    trapezoid(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(1, 0)
    circle(1)
    paralleogram(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(1, 0)
    circle(1)
    rhombus(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1

#### square rotate
    
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(0, 1)
    circle(1)
    rectangle(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(0, 1)
    circle(1)
    trapezoid(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(0, 1)
    circle(1)
    paralleogram(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    square(0, 1)
    circle(1)
    rhombus(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1        
    
#### rectangle
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(1, 0)
    circle(1)
    trapezoid(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(1, 0)
    circle(1)
    paralleogram(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(1, 0)
    circle(1)
    rhombus(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
#### rectangle rotate
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(0, 1)
    circle(1)
    trapezoid(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(0, 1)
    circle(1)
    paralleogram(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    rectangle(0, 1)
    circle(1)
    rhombus(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1      
    
#### trapezoid
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(1, 0)
    circle(1)
    paralleogram(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(1, 0)
    circle(1)
    rhombus(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1

#### trapezoid rotate
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(0, 1)
    circle(1)
    paralleogram(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    trapezoid(0, 1)
    circle(1)
    rhombus(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
    
#### paralleogram
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    paralleogram(1, 0)
    circle(1)
    rhombus(1, 0)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1
#### paralleogram rotate
for k in range(200):
    image = pilimg.new('RGB', (900, 532), (255, 255, 255))
    draw = imdraw.Draw(image)
    paralleogram(0, 1)
    circle(1)
    rhombus(0, 1)
    image.save("/home/a/python_MakeExample/jpgfiles/t%s.jpg" %cnt)      
    cnt += 1


