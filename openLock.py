'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around.
For example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6

Input: deadends = ["8888"], target = "0009"
Output: 1

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1

Input: deadends = ["0000"], target = "8888"
Output: -1

'''

def openLock(deadends):    
    return -1