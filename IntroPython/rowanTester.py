#!/usr/bin/python3

# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and 
# (3)  you provide clear attribution to RowanRobots: http://www.rowan.edu/robots
# 
# Attribution Information: This file is a supplement to the UC Berkeley Pacman projects
# written by 
# by Jennifer Kay kay@rowan.edu
#

from autograder import runAutoTests, readCommand


def easyGo():
    options = readCommand(["GoProfs!"])
    runAutoTests(options)

if __name__ == '__main__':
    easyGo()
    
    
