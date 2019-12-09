# Ashley He (ach238), Amelia Myers (arm298)
# Final Project, Monday
# 2019

import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import time
import os
import sys

# set up display things
os.putenv('SDL_VIDEORIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')
os.putenv('SDL_MOUSEDRV','TSLIB')
os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

# for debugging touchscreen touches
global touches
touches = []
global oneOZ
global twoOZ
global threeOZ
global dash
threeOZ = 4.5
twoOZ = 3
oneOZ = 1.5 # delay for one oz to be served
dash = 0.75

# ======================= PWM Servo things =======================
# set up GPIO pins for PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
# extra pins for 6 servo design
# GPIO.setup(20, GPIO.OUT)
# GPIO.setup(21, GPIO.OUT)

# set up buttons to test PWM
# GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# bail out button
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dc = 0 # change to zero?

p1 = GPIO.PWM(5, 1000/21.5) # Whisky
p2 = GPIO.PWM(6, 1000/21.5) # Bitters
p3 = GPIO.PWM(19, 1000/21.5) # Vermouth
p4 = GPIO.PWM(26, 1000/21.5) # Gin
 
p1.start(dc) # duty cycle 50%
p2.start(dc) # duty cycle 50%
p3.start(dc) # duty cycle 50%
p4.start(dc) # duty cycle 50%

# servo control
# def GPIO17_callback(channel): 
#     print(" ")
#     print"Servo, clockwise"
#     p1.ChangeFrequency(1000/(20+0.75))
#     p1.ChangeDutyCycle(75/(20+0.75))
    
# def GPIO22_callback(channel): 
#     print(" ")
#     print"Servo, counter-clockwise"
#     p1.ChangeFrequency(1000/(20+2.25))
#     p1.ChangeDutyCycle(225/(20+2.25))

# def GPIO23_callback(channel): 
#     print(" ")
#     print"Servo Stop."
#     p1.ChangeDutyCycle(0) 

# Bail out button
def GPIO27_callback(channel): 
    GPIO.cleanup()
    sys.exit("Bailed Out")

# GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)
# GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
# GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=300)

GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)

# Spigot-Servo Control
def addDrink1(amount): #Whisky
    # turn spigot on
    p1.ChangeFrequency(1000/(20+0.75))
    p1.ChangeDutyCycle(75/(20+0.75))
    time.sleep(amount)
    # turn spigot off
    p1.ChangeFrequency(1000/(20+2.25))
    p1.ChangeDutyCycle(225/(20+2.25))
    time.sleep(1)
    p1.ChangeDutyCycle(0)

def addDrink2(amount): #Bitters
    # turn spigot on
    p2.ChangeFrequency(1000/(20+0.75))
    p2.ChangeDutyCycle(75/(20+0.75))
    time.sleep(amount)
    # turn spigot off
    p2.ChangeFrequency(1000/(20+2.25))
    p2.ChangeDutyCycle(225/(20+2.25))
    time.sleep(1)
    p2.ChangeDutyCycle(0)

def addDrink3(amount): #Vermouth
     # turn spigot on
    p3.ChangeFrequency(1000/(20+0.75))
    p3.ChangeDutyCycle(75/(20+0.75))
    time.sleep(amount)
     # turn spigot off
    p3.ChangeFrequency(1000/(20+2.25))
    p3.ChangeDutyCycle(225/(20+2.25))
    time.sleep(1)
    p3.ChangeDutyCycle(0)
    drink_3 = False

def addDrink4(amount): #Gin
     # turn spigot on
    p4.ChangeFrequency(1000/(20+0.75))
    p4.ChangeDutyCycle(75/(20+0.75))
    time.sleep(amount)
     # turn spigot off
    p4.ChangeFrequency(1000/(20+2.25))
    p4.ChangeDutyCycle(225/(20+2.25))
    time.sleep(1)
    p4.ChangeDutyCycle(0)
    drink_4 = False

# control servos for custom drink
def openSpigot(x,y):
    if y > 70 and y < 110:
        if x > 40 and x < 140:
            print "ingredient 1"
            p1.ChangeFrequency(1000/(20+0.75))
            p1.ChangeDutyCycle(75/(20+0.75))
                                            
    # Ingredient 2 Bitters
    if y > 140 and y < 180:
        if x > 40 and x < 140:
            print "ingredient 2"
            p2.ChangeFrequency(1000/(20+0.75))
            p2.ChangeDutyCycle(75/(20+0.75))

    # Ingredient 3 Vermouth
    if y > 70 and y < 110:
        if x > 190 and x < 290:
            print "ingredient 3"
            p3.ChangeFrequency(1000/(20+0.75))
            p3.ChangeDutyCycle(75/(20+0.75))

    # Ingredient 4 Gin
    if y > 140 and y < 180:
        if x > 190 and x < 290:
            print "ingredient 4"
            p4.ChangeFrequency(1000/(20+0.75))
            p4.ChangeDutyCycle(75/(20+0.75))
            
def closeSpigot(x,y):
    # Ingredient 1 Whisky
    if y > 70 and y < 110:
        if x > 40 and x < 140:
            p1.ChangeFrequency(1000/(20+2.25))
            p1.ChangeDutyCycle(225/(20+2.25))
            time.sleep(1)
            p1.ChangeDutyCycle(0)
            
    # Ingredient 2 Bitters
    if y > 140 and y < 180:
        if x > 40 and x < 140:
            print "ingredient 2"
            p2.ChangeFrequency(1000/(20+2.25))
            p2.ChangeDutyCycle(225/(20+2.25))
            time.sleep(1)
            p2.ChangeDutyCycle(0)

    # Ingredient 3 Vermouth
    if y > 70 and y < 110:
        if x > 190 and x < 290:
            print "ingredient 3"
            p3.ChangeFrequency(1000/(20+2.25))
            p3.ChangeDutyCycle(225/(20+2.25))
            time.sleep(1)
            p3.ChangeDutyCycle(0)

    # Ingredient 4 Gin
    if y > 140 and y < 180:
        if x > 190 and x < 290:
            print "ingredient 4"
            p4.ChangeFrequency(1000/(20+2.25))
            p4.ChangeDutyCycle(225/(20+2.25))
            time.sleep(1)
            p4.ChangeDutyCycle(0)
                
# ======================= END PWM Servo things ======================

# ======================= PyGame setup ==============================

pygame.init()
# set color
BLACK=0,0,0
WHITE=255,255,255
RED=255,0,0
GREEN=0,255,0
BLUE=0,68,255
ORANGE = 255,173,3
OLDFASH = 252,184,116
MARTINI = 116,221,252
MANHATTAN = 252,125,116
size=width,height=320,240
screen=pygame.display.set_mode(size)
my_font=pygame.font.SysFont("quicksand",16)
pygame.mouse.set_visible(False)

# ========================= End PyGame setup ========================


# ======================= BUTTONS FOR GUI ===========================
welcome_msg={(160,40):'WELCOME!',(160,90):'Please select an option below:'}
start_buttons= {(80,150):'Drink Menu',(240,150):'Custom Drink',(160,210):"QUIT"}
control_buttons={(40,30):'Menu:', (280,30):'Back'}
custom_control_buttons={(80,30):'Custom Drink:', (280,30):'Back'}
menu_buttons={(160,100):'Old-Fashioned',(240,180):'Manhattan',(90,180):'Martini'}
drink_progress_disp={(160,40):'Your drink is being prepared!',(160,80):'Drink Ingredients:'}
custom_ing={(90,90):'Whisky', (90,160):'Bitters', (240,90):'Vermouth', (240,160):'Gin'}
# my_buttons1={(160,120):'STOP',(270,220):'QUIT',(60,30):'Left History',(260,30):'Right History'}
# my_buttons1={(160,120):'STOP',(270,220):'QUIT',(60,30):'Left History',(260,30):'Right History'}

# ===================== END BUTTONS FOR GUI =======================

# ===================== Start GUI code ========================
# 320 x 240 Screen
code_running = True
# Loop tracking variables
start_screen = True
drink_menu = False
drink_progress = False
custom_drink = False
drink_1 = False
drink_2 = False
drink_3 = False

# loop until user quits
while code_running:
    # add in quit button?
    # Start Screen ============================================================================
    while start_screen:
        time.sleep(0.2) 
        # design button functions
        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONDOWN):
                pos=pygame.mouse.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                pos=pygame.mouse.get_pos()
                touches.append(pos)
                x,y = pos
                #print touches

                # put all button/touch locations here (change x,y as necessary):
                # Drink Menu button
                if y > 130 and y < 170:
                    if x > 30 and x < 130:
                        print "drink menu pressed"
                        drink_menu = True
                        start_screen = False

                # Create drink button
                if y > 130 and y < 170:
                    if x > 180 and x < 300:
                        print "custom drink pressed"
                        custom_drink = True
                        start_screen = False
                # quit button
                if y > 190 and y < 230:
                    if x > 130 and x < 190:
                        sys.exit("Quit Bartending")                        
        # DRAW and FLIP on the screen after every loop
        # THIS CODE needs to go in every while loop for each menu
        screen.fill(BLACK)

        # need to change coordinates for circles/rectangles
        #pygame.draw.circle(screen,RED,[160,120],30)
        #pygame.draw.circle(screen,ORANGE,[120,120],30)
        # rect [x,y,height,width] x,y centers
        pygame.draw.rect(screen, ORANGE, [30,130,100, 40],0)
        pygame.draw.rect(screen, ORANGE, [180,130,120, 40],0)
        pygame.draw.rect(screen, RED, [130,190,60, 40],0)

        for text_pos, my_text in welcome_msg.items():
            text_surface=my_font.render(my_text, True, WHITE)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        for text_pos, my_text in start_buttons.items():
            text_surface=my_font.render(my_text, True, BLACK)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        pygame.display.flip()
    # END Start Screen  ========================================================================   
    
    # Drink Menu (with Drink Options) ============================================================
    while drink_menu:
        time.sleep(0.2) 
        # design button functions
        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONDOWN):
                pos=pygame.mouse.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                pos=pygame.mouse.get_pos()
                touches.append(pos)
                x,y = pos
                #print touches

                # put all button/touch locations here (change x,y as necessary):
                # Drink 1 button (old-fashioned)
                if y > 80 and y < 120:
                    if x > 90 and x < 230:
                        print "old-fashioned pressed"
                        drink_progress = True
                        drink_1 = True
                        drink_menu = False
                        start_time = time.time()


                # Drink 2 button (martini)
                if y > 160 and y < 200:
                    if x > 50 and x < 130:
                        print "martini pressed"
                        drink_progress = True
                        drink_2 = True
                        drink_menu = False
                        start_time = time.time()

                        
                # Drink 3 button (manhattan)
                if y > 160 and y < 200:
                    if x > 190 and x < 290:
                        print "manhattan pressed"
                        drink_progress = True
                        drink_3 = True
                        drink_menu = False
                        start_time = time.time()
                        
                # Back button
                if y > 10 and y < 50:
                    if x > 250 and x < 310:
                        print "back pressed"
                        start_screen = True
                        drink_menu = False

        # DRAW and FLIP on the screen after every loop
        # THIS CODE needs to go in every while loop for each menu
        screen.fill(BLACK)

        # need to change coordinates for circles/rectangles
        # rect [x,y,height,width] x,y centers
        pygame.draw.rect(screen, OLDFASH, [90,80,140, 40],0)
        pygame.draw.rect(screen, MARTINI, [50,160,80, 40],0)
        pygame.draw.rect(screen, MANHATTAN, [190,160,100, 40],0)
        #pygame.draw.rect(screen, BLUE, [250,10,60,40], 0)
        
        for text_pos, my_text in control_buttons.items():
            text_surface=my_font.render(my_text, True, WHITE)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
            
        for text_pos, my_text in menu_buttons.items():
            text_surface=my_font.render(my_text, True, BLACK)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        pygame.display.flip()
    # END drink menu ==================================================================================================

    # Determine when to time out for drink progress
    mix_time = 8
    # Drink Progress (check for drink being made here, change display based on that)
    while drink_progress:
        time.sleep(0.2)
        if drink_1: # old fashioned
            drink_ing={(160,200):'Old Fashioned',(160,120):'1 oz - Whisky',(160,140):'3 dash - Bitters'}
        elif drink_2:
            drink_ing={(160,200):'Martini',(160,120):'3 oz - Gin',(160,140):'1 oz - Vermouth'}
        elif drink_3:
            drink_ing={(160,200):'Manhattan',(160,120):'2 oz - Whisky',(160,140):'1 oz - Vermouth',(160,160):'2 dash - Bitters'}

        # draw to screen
        screen.fill(BLACK)
        for text_pos, my_text in drink_ing.items():
            text_surface=my_font.render(my_text, True, WHITE)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        for text_pos, my_text in drink_progress_disp.items():
            text_surface=my_font.render(my_text, True, WHITE)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        pygame.display.flip()
        
        if drink_1: # old fashioned
            #drink_ing={(160,200):'Old Fashioned',(160,120):'1 oz - Whisky',(160,140):'3 dash - Bitters'}
            mix_time = 6
            addDrink1(oneOZ) #Whisky
            addDrink2(dash) #Bitters x3
            addDrink2(dash) 
            addDrink2(dash) 
            drink_1 = False

        elif drink_2: # martini
            #drink_ing={(160,200):'Martini',(160,120):'3 oz - Gin',(160,140):'1 oz - Vermouth'}
            mix_time = 8
            addDrink3(oneOZ) #Vermouth
            addDrink4(threeOZ) #Gin
            drink_2 = False

        elif drink_3: # manhattan 
            #drink_ing={(160,200):'Manhattan',(160,120):'2 oz - Whisky',(160,140):'1 oz - Vermouth',(160,160):'2 dash - Bitters'}
            mix_time = 8
            addDrink1(twoOZ) #Whisky
            addDrink3(oneOZ) #Vermouth
            addDrink2(dash) #Bitters x2
            addDrink2(dash)
            drink_3 = False
        
            
        if time.time() - start_time >= mix_time: # change to accomodate for drink prep
            start_screen = True
            drink_progress = False
        

#    # END drink progress ============================================================================
#    
    # Custom dispense (how do we track how long we press/ just set for a fixed time?)
    while custom_drink:
        time.sleep(0.2) 
        # design button functions
        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONDOWN):
                pos=pygame.mouse.get_pos()
                x,y = pos
                openSpigot(x,y)
                           
            elif(event.type is MOUSEBUTTONUP):
                pos=pygame.mouse.get_pos()
                touches.append(pos)
                x,y = pos
                #print touches
                closeSpigot(x,y)
                        
                # Back button
                if y > 10 and y < 50:
                    if x > 250 and x < 310:
                        print "back pressed"
                        start_screen = True
                        custom_drink = False

        # DRAW and FLIP on the screen after every loop
        # THIS CODE needs to go in every while loop for each menu
        screen.fill(BLACK)

        # need to change coordinates for circles/rectangles
        pygame.draw.rect(screen, ORANGE, [40,70,100, 40],0)
        pygame.draw.rect(screen, ORANGE, [40,140,100, 40],0)
        pygame.draw.rect(screen, ORANGE, [190,70,100, 40],0)
        pygame.draw.rect(screen, ORANGE, [190,140,100, 40],0)

        for text_pos, my_text in custom_control_buttons.items():
            text_surface=my_font.render(my_text, True, WHITE)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        for text_pos, my_text in custom_ing.items():
            text_surface=my_font.render(my_text, True, BLACK)
            rect=text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        pygame.display.flip()

    # END custom drink

# ====================== End GUI code ========================


p1.stop()
p2.stop()    
p3.stop() 
p4.stop()     
GPIO.cleanup()
