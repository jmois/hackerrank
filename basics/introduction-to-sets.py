from __future__ import division

def average(array):
    # your code goes here
    number = sum(set(array))/len(set(array))
    return number
if __name__ == '__main__':
