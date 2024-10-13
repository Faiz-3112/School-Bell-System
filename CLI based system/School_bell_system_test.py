import pygame 
import time
import datetime
def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("PERIOD BELL.mp3")
    n=1
    while n<5:
        pygame.mixer.music.play()
        time.sleep(0)
        n+=1
sec=0
hr=0
print('WELCOME')
print('ENTER WHETHER TODAY IS')
print("1-FULL DAY     2-HALF DAY ")
user=int(input(''))
min=int(input('please set the time of a period(in min)'))
print("NOW THE TIME IS FOR ASSEMBLY...EVERYONE ARE REQUESTED TO ASSEMBLE IN ASSEMBLY GROUND")
pygame.mixer.init()
pygame.mixer.music.load("assembly call.mp3")
z=1
while z<5:
    pygame.mixer.music.play()
    time.sleep(0)
    z+=1
if user==1:
    for j in range(1,6):
        for i in range(min):
            print('now the time is:-',end=' ')
            print(time.ctime())
            time.sleep(60)
        if j==5:
            print("NOW ITS RECESS TIME...STUDENTS ARE REQUESTED TO HAVE THEIR LUNCH IN CLASSROOM")
            pygame.mixer.init()
            pygame.mixer.music.load("assembly call.mp3")
            d=1
            while d<5:
                pygame.mixer.music.play()
                time.sleep(0)
                d+=1
        elif j<8 or j==8:
            print("NOW THE PERIOD IS ",j)
            sound()
        else:
            pass
    for k in range(5,10):
        for m in range(min):
            print('now the time is:-',end=' ')
            print(time.ctime())
            time.sleep(60)
        if k<8 or k==8:
            print("NOW THE PERIOD IS ",k)
            sound()
    
elif user==2:
    for g in range(1,6):
        for i in range(min):
            print('now the time is:-',end=' ')
            print(time.ctime())
            time.sleep(60)
        if g<4 or g==4:
            print("NOW THE PERIOD IS ",g)
            sound()
else:
    print("INVALID ENTRY")
    
print("NOW THE TIME IS TO GO HOME...MAKE LINE AND GET BACK TO HOME SAFELY")
print('now the time is:-',end=' ')
print(time.ctime())
pygame.mixer.init()
pygame.mixer.music.load("PERIOD BELL.mp3")
x=1
while x<5:
    pygame.mixer.music.play()
    time.sleep(0)
    x+=1
