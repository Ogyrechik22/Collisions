a = 25
b = 575
def collide1(x,y,w,h,x2,y2,diameter):
    testX = x2
    testY = y2
    if x2 < x:
        testX = x
    elif x2 > x + w:
        testX = x + w
    if y2 < y:
        testY = y
    elif y2 > y + h:
        testY = y + h
    distance = dist(x2,y2,testX,testY)
    if distance <= diameter/2:
        return True
    else:
        return False
def collide2(x2,y2,w2,h2,x22,y22,diameter2):
    testX2 = x22
    testY2 = y22
    if x22 < x2:
        testX2 = x2
    elif x22 > x2 + w2:
        testX2 = x2 + w2
    if y22 < y2:
        testY2 = y2
    elif y22 > y2 + h2:
        testY2 = y2 + h2
    distance2 = dist(x22,y22,testX2,testY2)
    if distance2 <= diameter2/2:
        return True
    else:
        return False
def collide3(x22,y22,w22,h22,x222,y222,diameter22):
    testX22 = x222
    testY22 = y222
    if x222 < x22:
        testX22 = x22
    elif x222 > x22 + w22:
        testX22 = x22 + w22
    if y222 < y22:
        testY22 = y22
    elif y222 > y22 + h22:
        testY22 = y22 + h22
    distance22 = dist(x222,y222,testX22,testY22)
    if distance22 <= diameter22/2:
        return True
    else:
        return False
def collide4(x222,y222,w222,h222,x2222,y2222,diameter222):
    testX222 = x2222
    testY222 = y2222
    if x2222 < x222:
        testX222 = x222
    elif x2222 > x222 + w222:
        testX222 = x222 + w222
    if y2222 < y222:
        testY222 = y222
    elif y2222 > y222 + h222:
        testY222 = y222 + h222
    distance222 = dist(x2222,y2222,testX222,testY222)
    if distance222 <= diameter222/2:
        return True
    else:
        return False
def setup():
    size(600,600)
    textSize(30)
def draw():
    global a,b
    background(100)
    ellipse(a,b,40,40)
    if keyPressed == True:
        if key == 'w' or key == 'W' or key == 'ц' or key == 'Ц':
            b -= 2
        if key == 's' or key == 'S' or key == 'ы' or key == 'Ы':
            b += 2
        if key == 'a' or key == 'A' or key == 'ф' or key == 'Ф':
            a -= 2
        if key == 'd' or key == 'D' or key == 'в' or key == 'В':
            a += 2
    if collide1(100,100,50,500,a,b,40):
        noLoop()
        clear()
        background(1)
        stroke(255,0,0)
        text('Lose!',250,300)
    else:
        fill(255)
        rect(100,100,50,500)
    if collide2(300,0,50,500,a,b,40):
        background(1)
        stroke(255,0,0)
        noLoop()
        clear()
        text('Lose!',250,300)
    else:
        fill(255)
        rect(300,0,50,500)
    if collide3(500,100,50,500,a,b,40):
        background(1)
        stroke(255,0,0)
        noLoop()
        clear()
        text('Lose!',250,300)
    else:
        fill(255)
        rect(500,100,50,500)
    if collide4(600,0,-30,30,a,b,40):
        background(1)
        fill(255,0,0)
        noLoop()
        clear()
        text('Win!',250,300)
    else:
        fill(255)
        rect(600,0,-30,30)
            
