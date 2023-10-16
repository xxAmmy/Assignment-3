# assignment 2

from asyncio import create_subprocess_shell
from robot_world import *

def show_duo_names():
    print()
    print('┌─────────────────────┬───────────────────────┐')
    print('│ 0HV120 assignment 2 │ Robot World           │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 1       │ Ammy Prohkrathok      │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 2       │ Rosalie Benvelsen     │')
    print('└─────────────────────┴───────────────────────┘')


def script_0_demo(robot):
    # demo script to show the capabilities of the robot
    # read the assignment instructions for details
        
    # demo of scans
    direction = robot.scan_direction()
    print("current robot direction:", direction)
    obstacle = robot.scan_object_ahead()
    print("first obstacle ahead:", obstacle)
    steps = robot.scan_steps_ahead()
    print("steps to the first obstacle:", steps)
    energy = robot.scan_energy()
    print("remaining energy for steps:", energy)

    # demo of stepping and turning
    for _ in range(3):
        robot.step_forward()
    robot.turn_left()
    robot.turn_right()
    robot.turn_right()
    for _ in range(4):
        robot.step_forward()
    for _ in range(4):
        robot.step_back()
    robot.turn_left()
    robot.step_back()
    robot.step_back()
    robot.turn_right()

    # demo of scans
    print()
    direction = robot.scan_direction()
    print("current robot direction:", direction)
    obstacle = robot.scan_object_ahead()
    print("first obstacle ahead:", obstacle)
    steps = robot.scan_steps_ahead()
    print("steps to the first obstacle:", steps)
    energy = robot.scan_energy()
    print("remaining energy for steps:", energy)

    # demo of grabbing, pushing forward, dragging backward and releasing of a block
    robot.step_forward() # when the robot faces and touches the block it can grab it
    robot.grab_release_block()

    # moving the block
    for _ in range(5):
        robot.step_forward()
    for _ in range(3):
        robot.step_back()

    robot.grab_release_block()  # releasing the block

    robot.step_back()
    robot.turn_right()
    robot.turn_right()
    robot.turn_right()
    for _ in range(3): # finally, crash robot into the wall
        robot.step_back()

    return # end of demo

################################################
#   helper functions defined by you can go here:
#   start of helper function part
#wall: touch
# block: 1. touch
#            grab
#           push/drag (after grab)

def find_corner(robot):
    for i in range(2): #naar hoek lopen
        steps = robot.scan_steps_ahead()
        for n in range(steps):
            robot.step_forward()
        robot.turn_right()

def face_down(robot):
    direction = robot.scan_direction()
    robot.scan_direction()
    if direction == 'UP':
        robot.turn_left()
        robot.turn_left()
    elif direction == 'RIGHT':
        robot.turn_right()
    elif direction == 'LEFT':
        robot.turn_left()

def face_up(robot):  
    direction = robot.scan_direction()  
    robot.scan_direction()  
    if direction == 'DOWN':  
        robot.turn_left()  
        robot.turn_left()  
    elif direction == 'RIGHT':  
        robot.turn_left()  
    elif direction == 'LEFT':  
        robot.turn_right() 
    
def face_right(robot):  
    direction = robot.scan_direction()  
    robot.scan_direction()  
    if direction == 'UP':  
        robot.turn_right()  
    elif direction == 'DOWN':  
        robot.turn_left()  
    elif direction == 'LEFT':  
        robot.turn_left() 
        robot.turn_left() 

def face_left(robot):
    direction = robot.scan_direction()
    if direction == 'UP':
        robot.turn_left()
    elif direction == 'RIGHT':
        robot.turn_right()
        robot.turn_right()
    elif direction == 'DOWN':
        robot.turn_right()


def downleft_corner(robot): #ga naar links onder hoek
    face_down(robot)
    steps = robot.scan_steps_ahead()
    for n in range(steps):
        robot.step_forward()
    robot.turn_right()
    steps = robot.scan_steps_ahead()
    for i in range(steps):
        robot.step_forward()
    robot.turn_right()

def grab_block_other_side(robot): 
    robot.grab_release_block() 
    robot.turn_left() 
    robot.step_forward() 
    robot.turn_right() 
    robot.step_forward() 
    robot.step_forward() 
    robot.turn_right() 
    robot.step_forward() 
    robot.turn_right() 
    robot.grab_release_block() 

def grab_block_down(robot): 
    robot.grab_release_block() 
    direction = robot.scan_direction()  
    if direction == 'LEFT':  
        robot.turn_left()  
        robot.step_forward() 
        robot.turn_right() 
        robot.step_forward() 
        robot.turn_right() 
    elif direction == 'RIGHT':  
        robot.turn_right() 
        robot.step_forward()  
        robot.turn_left() 
        robot.step_forward() 
        robot.turn_left()  
    robot.grab_release_block() 

def grab_block_up(robot): 
    robot.grab_release_block() 
    direction = robot.scan_direction()  
    if direction == 'RIGHT':  
        robot.turn_left()  
        robot.step_forward() 
        robot.turn_right() 
        robot.step_forward() 
        robot.turn_right() 
    elif direction == 'LEFT':  
        robot.turn_right() 
        robot.step_forward()  
        robot.turn_left() 
        robot.step_forward() 
        robot.turn_left()  
    robot.grab_release_block() 

#   end of helper function part
################################################

def script_1(robot):   # Walk around the World
    # your solution here:
    
    for i in range(2): #naar hoek lopen
        steps = robot.scan_steps_ahead()
        for n in range(steps):
            robot.step_forward()
        robot.turn_right()

    total_steps = 0
    for i in range(4): #rondje lopen
        steps = robot.scan_steps_ahead()
        for n in range(steps):
            robot.step_forward()
        robot.turn_right()
        total_steps = total_steps + steps  #tellen van rondje

    print(f"It takes {total_steps} steps to walk around the world.") 

    return # end of script_1

def script_2(robot):  # Switch Rooms
    # your solution here:
    
    face_up(robot)
    steps = robot.scan_steps_ahead()
    for n in range(steps):
        robot.step_forward()
    face_down(robot)

    left_list = []
    left_steps = 0 
    right_list = []
    right_steps = 0
    
    steps = robot.scan_steps_ahead()
    for n in range(steps+1): #scan left and right
        face_left(robot)
        left_steps = robot.scan_steps_ahead()
        left_list.append(left_steps)
        face_right(robot)
        right_steps = robot.scan_steps_ahead()
        right_list.append(right_steps)
        face_down(robot)
        if n != steps:
            robot.step_forward()

    max_left = max(left_list)
    max_right = max(right_list)
    min_left = min(left_list)
    min_right = min(right_list)

    if max_left != min_left: #decide which list and how many steps back
        for i in range(steps-left_list.index(max_left)):
            robot.step_back()
        robot.turn_right()
    elif max_right != min_right:
        for i in range(steps-right_list.index(max_right)):
            robot.step_back()
        robot.turn_left()

    steps = robot.scan_steps_ahead()
    for n in range(steps):
        robot.step_forward()

    return # end of script_2


def script_3(robot): # Where is the Tile
    # your solution here:
    face_down(robot)
    obstacle = robot.scan_object_ahead()
    if obstacle == 'Tile':  #dit is voor als de robot boven tile spawnt gaat hij gelijk naar de tile
        steps = robot.scan_steps_ahead()         
        for i in range(steps+1): 
            robot.step_forward()

        face_left(robot)
        x = robot.scan_steps_ahead() +1
        face_down(robot)
        y = robot.scan_steps_ahead() +1
        print(f"The tile is at a position (x, y) = ({x}, {y})")
   
    steps = robot.scan_steps_ahead() 
    for n in range(steps): #walk down
        robot.step_forward()
    robot.turn_right() # tile is on y=1 left side robot
    steps = robot.scan_steps_ahead()
    obstacle = robot.scan_object_ahead()
    if obstacle == 'Tile': 
        for i in range(steps+1): 
            robot.step_forward()
    else:
        downleft_corner(robot)
        obstacle = robot.scan_object_ahead()
        while obstacle != 'Tile': 
            robot.turn_right() 
            obstacle = robot.scan_object_ahead() 
            if obstacle == 'Tile': 
                steps = robot.scan_steps_ahead()  
                for i in range(steps+1): 
                    robot.step_forward()
                break
            else:
                robot.turn_left()
                robot.step_forward()
                obstacle = robot.scan_object_ahead()
        obstacle = robot.scan_object_ahead()        
        if obstacle == 'Tile': 
            steps = robot.scan_steps_ahead()  
            for i in range(steps+1): 
                robot.step_forward()
        
    face_left(robot)
    x = robot.scan_steps_ahead() +1
    face_down(robot)
    y = robot.scan_steps_ahead() +1
    print(f"The tile is at a position (x, y) = ({x}, {y})")

    return # end of script_3


def script_4(robot):  # Walk around the Block
    # your solution here:

    face_down(robot)
    obstacle = robot.scan_object_ahead()
    if obstacle == 'Block':
        steps = robot.scan_steps_ahead()
        for n in range(steps):
            robot.step_forward()
    else:
        downleft_corner(robot)
          
    while obstacle != 'Block':
        robot.turn_right()
        obstacle = robot.scan_object_ahead()
        if obstacle == 'Block':
            steps = robot.scan_steps_ahead()
            for walk in range(steps):
                robot.step_forward()
        else:
            robot.turn_left()
            robot.step_forward()

    robot.turn_left()
    robot.step_forward()
    for o in range(3): #walk around block
        robot.turn_right()
        robot.step_forward()
        robot.step_forward()
    robot.turn_right()
    robot.step_forward()
    

    return # end of script_4


def script_5(robot):  # Follow the Tile Path
    # your solution here:
    steps = 1 
    obstacle = 'Wall' 
    direction = 'start' 
    while not (steps == 0 and obstacle == 'Wall' and direction == 'RIGHT'): 
        steps = robot.scan_steps_ahead() 
        direction = robot.scan_direction() 
        obstacle = robot.scan_object_ahead() 
        if steps == 0 and obstacle == 'Tile': 
            robot.step_forward() 
            obstacle = robot.scan_object_ahead() 
            steps = robot.scan_steps_ahead() 
        else: 
            robot.turn_left() 
            steps = robot.scan_steps_ahead() 
            obstacle = robot.scan_object_ahead() 
            direction = robot.scan_direction() 
            if steps == 0 and obstacle == 'Tile': 
                robot.step_forward() 
                obstacle = robot.scan_object_ahead() 
                steps = robot.scan_steps_ahead() 
            else: 
                robot.turn_right() 
                robot.turn_right() 
                steps = robot.scan_steps_ahead() 
                obstacle = robot.scan_object_ahead() 
                direction = robot.scan_direction() 
                if steps == 0 and obstacle == 'Tile': 
                    robot.step_forward() 
                    obstacle = robot.scan_object_ahead() 
                    steps = robot.scan_steps_ahead() 

    return # end of script_5


def script_6(robot):  # Push the Block over the Tile
    # your solution here:  
    #EXEPTIONS: 
    #BLOCK IN CORNER 
    #IF THE ROBOT WALKS AGAINST THE BLOCK/TILE, IT WILL CRASH 
    #IF THE BLOCK AND TILE ARE NEXT TO EACH OTHER, THE ROBOT CAN ONLY SEE ONE AND WILL CRASH 

    face_down(robot)  
    obstacle = robot.scan_object_ahead()  
    if obstacle == 'Tile':  
        steps = robot.scan_steps_ahead()           
        for i in range(steps+1):  
            robot.step_forward()  
        y_count_tile = robot.scan_steps_ahead() +1  
        robot.turn_right()  
        x_count_tile = robot.scan_steps_ahead() +1  
        print(f"The tile is at a position (x, y) = ({x_count_tile}, {y_count_tile})")  
        return  

    downleft_corner(robot)  
    y_count_tile = 1  
    x_count_tile = 1  
    obstacle = robot.scan_object_ahead()   
    while obstacle != 'Tile':   
        robot.turn_right()   
        obstacle = robot.scan_object_ahead()   
        if obstacle == 'Tile':   
            steps = robot.scan_steps_ahead()    
            x_count_tile = steps +2 
        else:  
            robot.turn_left()   
            robot.step_forward()  
            y_count_tile += 1  
 
    print(f"The tile is at a position (x, y) = ({x_count_tile}, {y_count_tile})") 

    face_down(robot)  

    obstacle = robot.scan_object_ahead()  
    if obstacle == 'Block':  
        steps = robot.scan_steps_ahead()  
        for n in range(steps):  
            robot.step_forward() 
        y_block = robot.scan_steps_ahead() +1 
        robot.turn_right() 
        x_block = robot.scan_steps_ahead() +1 
        print(f"the block is at position ({x_block}, {y_block})") 
    else:  
        downleft_corner(robot)      

    y_count_block = 1 
    x_count_block = 1 
    obstacle = robot.scan_object_ahead() 
    while obstacle != 'Block':  
        robot.turn_right()  
        obstacle = robot.scan_object_ahead()  
        if obstacle == 'Block':  
            steps = robot.scan_steps_ahead()  
            for walk in range(steps):  
                robot.step_forward() 
                x_count_block += 1  
        else:  
            robot.turn_left()  
            robot.step_forward() 
            y_count_block += 1 
    x_count_block += 1 #block 1 step further than robot 
    print(f"the block is at ({x_count_block}, {y_count_block})") 

    robot.grab_release_block() 
    x_difference = x_count_tile - x_count_block 
    y_difference = y_count_tile - y_count_block 
    print(x_difference, y_difference) 

    if x_difference > 0: #WAT ALS 0?? 
        for _ in range(x_difference):  
                robot.step_forward() 
    else: 
        grab_block_other_side(robot) 
        for _ in range(-x_difference):  
                robot.step_forward() 
 
    if y_difference > 0: #WAT ALS 0? 
        grab_block_down(robot) 
        for _ in range(y_difference):  
                robot.step_forward() 
    else: 
        grab_block_up(robot)
        for _ in range(-y_difference):  
                robot.step_forward() 


    return # end of script_6
