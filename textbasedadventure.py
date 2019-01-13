'''
Created on Jan 11, 2019

@author: Nik
'''
import random 
import time





commands=['w','a','s','d']
def title():
    print("Welcome to the text based adventure game")
    print("Use w, a, s, d to control your character.")
    print("Enter s to start the game")
    
def firstroom(coins,danger):
   
         
    print("welcome to the first room")
    print("there are", coins,"coins")
    print("the danger level is", danger)
def leftroom(coins,danger):
    print("welcome to the left room")
    print("there are", coins, "coins")
    print("the danger level is", danger)
def leftroom2(coins,danger):
    print("welcome to the left room 2")
    print("there are", coins, "coins")
    print("the danger level is", danger)
def rightroom(coins,danger):
    print("welcome to the right room")
    print("there are", coins,"coins")
    print("the danger level is", danger)
def rightroom2(coins,danger):
    print("welcome to the right room 2")
    print("there are", coins,"coins")
    print("the danger level is", danger)
def frontroom(coins,danger):
    print("welcome to the front room")
    print("there are", coins,"coins")
    print("the danger level is", danger)

def frontroom2(coins,danger):
    print("welcome to the front room 2")
    print("there are", coins,"coins")
    print("the danger level is", danger)



def endscreen():
    print("enter y to play again or n to quit: ")
    quituser=str(input())
    if quituser == 'y':
        title()
        game()
    if quituser == 'n':
        exit()
    else:
        print("that was an invalid command")
        endscreen()
title()

def game():

    x = 0
    while x != 2:

        user=str(input())
        if user =='s':
            firstroom(0,'none') 
            x=2 


        else:
            print("that was an invalid command")      

    c=0  
    b=0  
    y=0
    a=0
    while y != 2:
        user2=str(input())

        if user2 == 'w':
            frontroom(8,'medium')   
            while a !=2:
                user3=str(input())
                if user3=='w':
                    frontroom2(0,'too high')
                    time.sleep(2)
                    print("you have died ")
                    y=2
                    a=2
                    endscreen()

 
                if user3=='a':
                    print("you can not go to the left from here")
                    frontroom(8,'medium')
                if user3=='d':
                    print("you can not go to the right from here")
                    frontroom(8,'medium')
                if user3=='s':
                    print("you can not go back to the previous room")
                    frontroom(8,'medium')
                if user3 not in commands:
                    print("that was invalid command")
                    frontroom(8,'medium')   
        if user2 =='s':
            print("you can not go backwards from here")    
            firstroom(0,'none')
            continue 
        
        
  
    
    
    

        
        if user2 == 'a':
            leftroom(6,'high')
            while b != 2:
                user4=str(input())
                if user4=='w':
                    print("you can not go forwards from here")
                    leftroom(6,'high')
                if user4=='a':
                    leftroom2(8,'low')
                    time.sleep(2)
                    print("congratulations you have survived the game")
                    y=2
                    b=2
                    endscreen()
                if user4=='d':
          
                    print("you can not go back to the previous room")
                    leftroom(6,'high')
                if user4=='s':
        
                    print("you can not go backwards from here")
                    leftroom(6,'high')
       
                if user4 not in commands:
                    print("that was invalid command")
                    leftroom(6,'high')



        if user2 =='d':
            rightroom(2,'low')
            while c != 2:
                
                user5=str(input())
                if user5=='w':
                    print("you can not go forwards from here")
                    rightroom(2,'low')
                if user5=='a':
                    print("you can not go back to the previous room")
                    rightroom(2,'low')
                if user5=='d':
                    rightroom2(0,'too high')
                    time.sleep(2)
                    print("you have died")
                    y=2
                    endscreen()
                if user5=='s':
                    print("you can not go backwards from here")
                    rightroom(2,'low')
            
                if user5 not in commands:
                    print("that was invalid command")
                    rightroom(2,'low')
        if user2 =='s':
            print("you can not go backwards from here")
   
        if user2 not in commands:
            print("that was an invalid command")
            
            
game()
           
        
           


