import pygame
import random




display_width=600
display_height=300
high_pot=display_height*0.80
low_pot=display_height*0.20
half_pot_gap=50

#object image
birdimg=pygame.image.load('1.png')


#bird
bird_height=80
bird_width=80



#color
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
skyblue=(135,206,235)
orange=(255,69,0)


def bird(x,y):
    gameDisplay.blit(birdimg,(x,y))

def  pot(pot1x,pot1y,pot1h,pot2x,pot2y,pot2h,potw,potcolor):
  pygame.draw.rect(gameDisplay,potcolor,[pot1x,pot1y,potw,pot1h])
  pygame.draw.rect(gameDisplay,black,[pot1x,pot1y,potw,pot1h],2)

  pygame.draw.rect(gameDisplay,potcolor,[pot2x,pot2y,potw,pot2h])
  pygame.draw.rect(gameDisplay,black,[pot2x,pot2y,potw,pot2h],2)


  pot_head_1x=pot1x-10
  pot_head_1y=pot1h
  pot_head_2x=pot2x-10
  pot_head_2y=pot2y
  pot_heade_width=50
  pot_head_height=20

  pygame.draw.rect(gameDisplay,orange,[pot_head_1x,pot_head_1y,pot_heade_width,pot_head_height])
  pygame.draw.rect(gameDisplay,black,[pot_head_1x,pot_head_1y,pot_heade_width,pot_head_height],2)


  pygame.draw.rect(gameDisplay,orange,[pot_head_2x,pot_head_2y,pot_heade_width,pot_head_height])
  pygame.draw.rect(gameDisplay,black,[pot_head_2x,pot_head_2y,pot_heade_width,pot_head_height],2)


def new_pot(factor):
  new_random=random.randrange(low_pot,high_pot)

  pot1h=new_random-half_pot_gap
  pot1x=display_width+100*factor
  pot1y=0

  pot2h=display_height-(new_random+half_pot_gap)
  pot2x=display_width+100*factor
  pot2y=new_random+half_pot_gap


  return pot1x,pot1y,pot1h,pot2x,pot2y,pot2h


def display_message(textmessage,tColor,position_x,position_y):
  textmessage=str(textmessage)
  font_and_size=pygame.font.Font("freesansbold.ttf",22)
  text_surface=font_and_size.render(textmessage,True,tColor)
  text_rect=text_surface.get_rect()
  text_rect.center=((position_x),(position_y))
  gameDisplay.blit(text_surface,text_rect)
  


#window
pygame.init()    
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Racey")
clock=pygame.time.Clock()


def gameloop():
  #bird starting location
  x=0
  y=(display_height*0.5)-(bird_height/2)
  
  #pot
  
  potw=30
  potcolor=green
  gamespeed=3



  pot1x=[0,0,0,0]
  pot1y=[0,0,0,0]
  pot1h=[0,0,0,0]
  pot2x=[0,0,0,0]
  pot2y=[0,0,0,0]
  pot2h=[0,0,0,0]
  
  pot1x[0],pot1y[0],pot1h[0],pot2x[0],pot2y[0],pot2h[0]=new_pot(1)
  pot1x[1],pot1y[1],pot1h[1],pot2x[1],pot2y[1],pot2h[1]=new_pot(3)
  pot1x[2],pot1y[2],pot1h[2],pot2x[2],pot2y[2],pot2h[2]=new_pot(5)
  pot1x[3],pot1y[3],pot1h[3],pot2x[3],pot2y[3],pot2h[3]=new_pot(6.5)

  score=0
  score_counter=0

  tasadof=False
  space_flag=False
  y_change=0
  down=True
  space_flag=0

  while not tasadof:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        tasadof=True
      if event.type==pygame.KEYDOWN and event.key== pygame.K_SPACE and space_flag==0:
        y_change= -10
        down=False
        space_flag=1
    gameDisplay.fill(white)
    if not down:
      if y_change < 0:
        if y-1>-0.2:
          y-=1
        else:
          y=-0.2
        y_change+=1
        space_flag=0
      else:
        down=True
        space_flag=0
    else:
      y+=2
      if y>(display_height-(bird_height-45)):
        y=display_height-(bird_height-45)

            
    y +=y_change
    bird(x,y) 


    for i in range(4):
          pot(pot1x[i],pot1y[i],pot1h[i],pot2x[i],pot2y[i],pot2h[i],potw,potcolor)   
          pot1x[i]-=  gamespeed
          pot2x[i]-=  gamespeed
          if pot1x[i]<-50:
             pot1x[i],pot1y[i],pot1h[i],pot2x[i],pot2y[i],pot2h[i]=new_pot(1)
             score+=5
    
    display_message(score,black,display_width-50,15)
    if score_counter>=60:
      score+=1
      score_counter=0
    else:
      score_counter+=1  

    pygame.display.update()
    clock.tick(60)
gameloop()
pygame.quit() 
quit()
