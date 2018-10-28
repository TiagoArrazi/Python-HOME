'''

   IN THIS LITTLE GAME YOU CONTROL A ROBOT SEEKING TREASURES

   RULES:

   1 - YOU CAN USE THE COMMANDS "UP", "DOWN", "LEFT", "RIGHT" ONE AT A TIME TO CONTROL YOUR ROBOT;
   2 - BEWARE, YOU CAN ONLY MOVE YOUR ROBOT 10 TIMES;
   3 - INVALID COMMANDS WILL COUNT AS A MOVEMENT ATTEMPT
   
'''

# ------------------------------------------------# HEADER

from random import randint as r


class Point:  # MOTHER CLASS

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Reward(Point):  # REWARD CLASS

    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name

    def __str__(self):
        return '<%s,%s>: %s' % (self.x, self.y, self.name)

    def __repr__(self):
        return '<Reward> %s' % str(self)


class Robot(Point):  # ROBOT CLASS

    def __init__(self, name, x=1, y=1):

        super(Robot, self).__init__(x, y)
        self.name = name

    def __str__(self):

        return '<%s,%s>: %s' % (self.x, self.y, self.name)

    def __repr__(self):

        return '<Robot> %s' % str(self)

    def show_position(self):

        print('The robot\'s current position is <%i,%i>' % (self.x, self.y))

    def move_up(self):

        if self.y < 10:
            self.y += 1
            print('Your robot moved up')
        else:
            print('The robot %s hit the uppermost bound' % self.name)

    def move_down(self):

        if self.y > 1:
            self.y -= 1
            print('Your robot moved down')
        else:
            print('The robot %s hit the lowermost bound' % self.name)

    def move_right(self):

        if self.x < 10:
            self.x += 1
        else:
            print('The robot %s hit the rightmost bound' % self.name)

    def move_left(self):

        if self.x > 1:
            self.x -= 1
        else:
            print('The robot %s hit the leftmost bound' % self.name)


# ----------------------------------------------------------------# MAIN

def check_reward(robot, rewards):  # CHECKS IF THE ROBOT HAS FOUND ANY TREASURES

    i = 0
    total = 10

    for reward in rewards:

        if reward.x == robot.x and reward.y == robot.y:
            print('Your robot has found %s' % reward.name)
            i += 1
            total -= 1
            print('%i treasures left')

    return i


reward_1 = Reward(r(1, 10), r(1, 10), 'Coin 1') #r(1, 10) = random.randint(1, 10)
reward_2 = Reward(r(1, 10), r(1, 10), 'Coin 2')
reward_3 = Reward(r(1, 10), r(1, 10), 'Coin 3')
reward_4 = Reward(r(1, 10), r(1, 10), 'Coin 4')
reward_5 = Reward(r(1, 10), r(1, 10), 'Coin 5')
reward_6 = Reward(r(1, 10), r(1, 10), 'Coin 6')
reward_7 = Reward(r(1, 10), r(1, 10), 'Coin 7')
reward_8 = Reward(r(1, 10), r(1, 10), 'Coin 8')
reward_9 = Reward(r(1, 10), r(1, 10), 'Coin 9')
reward_10 = Reward(r(1, 10), r(1, 10), 'Coin 10')

rewards = [reward_1, reward_2, reward_3, reward_4, reward_5,
           reward_6, reward_7, reward_8, reward_9, reward_10]

print('''
IN THIS LITTLE GAME YOU CONTROL A ROBOT SEEKING TREASURES IN A 10x10 MATRIX

RULES:
   
1 - YOU CAN USE THE COMMANDS "UP", "DOWN", "LEFT", "RIGHT" ONE AT A TIME TO CONTROL YOUR ROBOT; 
2 - BEWARE, YOU CAN ONLY MOVE YOUR ROBOT 30 TIMES;
3 - INVALID COMMANDS WILL COUNT AS A MOVEMENT ATTEMPT

HAVE FUN :)
   
   ''')

robot_1 = Robot('Rob-1', r(1, 10), r(1, 10))
robot_1.show_position()

# print(rewards)

for i in range(30):

    movement = input("Type UP, LEFT, DOWN or RIGHT to move your robot: ")

    if movement == 'up' or movement == 'UP':

        robot_1.move_up()
        robot_1.show_position()

    elif movement == 'down' or movement == 'DOWN':

        robot_1.move_down()
        robot_1.show_position()

    elif movement == 'left' or movement == 'LEFT':

        robot_1.move_left()
        robot_1.show_position()

    elif movement == 'right' or movement == 'RIGHT':

        robot_1.move_right()
        robot_1.show_position()

    else:

        print('INVALID COMMAND!')
        continue

    check_reward(robot_1, rewards)

treasures = check_reward(robot_1, rewards)

print('GAME OVER!', end='\n')

if treasures == 0:
    print('NO TREASURES WERE FOUND')

elif treasures == 1:
    print('%i TREASURE WAS FOUND' % i)

elif treasures > 1:
    print('%i TREASURES WERE FOUND' % i)
