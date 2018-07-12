# -*- coding: utf-8 -*-
"""
@author: Douglas Amante
"""

import random

class Point(object):
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
    
    def __str__(self):
        return '<%s, %s>:, %s' % (self.x, self.y)

class Reward(Point):
    
    def __init__(self,x,y,name):
        super(Reward, self).__init__(x,y)        
        self.name = name
        
    def __str__(self):
        return '<%s, %s>:, %s' % (self.x, self.y, self.name)
        
    def __repr__(self):
        return '<Reward> %s' % str(self)

class  Robot(Point):
        
    def move_up(self): #path in the matrix up
        if(self.y < 10):
            self.y = self.y + 1
        else:
            print "Forbidden Movement"            
            
    def move_down(self): #path in the matrix down
        if(self.y>0):
            self.y = self.y - 1
        else:
            print "Forbidden Movement"
        
    def move_right(self): #path in the matrix right
        if(self.x<10):
            self.x = self.x + 1
        else:
            print "Forbidden Movement"
        
    def move_left(self): #path in the matrix left
        if(self.x>0):
            self.x = self.x - 1
        else:
            print "Forbidden Movement"



def check_reward(robot, rewards): 
    
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print"The robot found the reward: "  
            print reward.x
            print robot.x
            

r1 = Reward(random.randint(0,10), random.randint(0,10), 'Coin')
r2 = Reward(random.randint(0,10), random.randint(0,10), 'Gasoline')
r3 = Reward(random.randint(0,10), random.randint(0,10), 'Weapon')
r4 = Reward(random.randint(0,10), random.randint(0,10), 'Coin')
r5 = Reward(random.randint(0,10), random.randint(0,10), 'Gasoline')
r6 = Reward(random.randint(0,10), random.randint(0,10), 'Coin')
r7 = Reward(random.randint(0,10), random.randint(0,10), 'Coin')
r8 = Reward(random.randint(0,10), random.randint(0,10), 'Gasoline')
r9 = Reward(random.randint(0,10), random.randint(0,10), 'Weapon')

rewards = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

robot = Robot(random.randint(0,10), random.randint(0,10))

for i in range(10):
        moviment = input(" Type 1=up, 2=down, 3=left or 4=right for movement: ")
        if moviment == 1:
            robot.move_up()                    
            check_reward(robot, rewards)        

        elif moviment == 2:
            robot.move_down()                    
            check_reward(robot, rewards)        

        elif moviment == 3:
            robot.move_left()                    
            check_reward(robot, rewards)        

        elif moviment == 4:
            robot.move_right()                    
            check_reward(robot, rewards)        

        else:
            print('Invalid movement')
            
        
