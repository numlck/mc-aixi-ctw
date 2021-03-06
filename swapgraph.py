# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

def read(file):
    '''
    read the log file and specify which type of reward to read
    if reward is true, then we read reward,
    otherwise we read average reward.

    '''
    cycles = []
    average_rewards = []
    with open(file) as f:
        last_line = None
        for line in f.readlines():
            line = line.strip()
            if "cycle:" in line:
                cycles.append(int(line[6:]))
                average_rewards.append(float(last_line.split(",")[2]))

            last_line = line
    if len(cycles) != len(average_rewards):
        return cycles, average_rewards[:-1]
    else:
        return cycles, average_rewards
    
def smooth(cycles,average_rewards,num=10):
    '''
    calculate time interval based average reward

    '''
    interval = int(len(cycles)/num)
    smoothed_cycles = [cycles[0]]
    smoothed_average_rewards = [average_rewards[0]]
    index = 1
    for epoch in range(num):
        avg_reward = np.mean(average_rewards[index:index+interval])
        smoothed_cycles.append(cycles[index])
        index+=interval
        smoothed_average_rewards.append(avg_reward)

    return smoothed_cycles,smoothed_average_rewards
    
def draw(cycles,average_rewards,times,labels):
    
    last = 0
    plt.figure(figsize=(9, 6))
    
    for index,time in enumerate(times):
        if last != 0:
            rcy = cycles[last+1:time]
            rav = average_rewards[last+1:time]
        else:
            rcy = cycles[last:time]
            rav = average_rewards[last:time]
        label = labels[index]
        last = time
        smoothed_cycles,smoothed_average_rewards = smooth(rcy,rav) #change number of interval wants at here
        p = plt.plot(smoothed_cycles,smoothed_average_rewards,'-',lw = 2,label = label)
        plt.plot(smoothed_cycles,smoothed_average_rewards,'D',color = p[0].get_color())
        
    plt.legend(loc="upper right")
    plt.title(f"Swap enviroments : Kuhn Poker and Extended Tiger")
    plt.plot()
    plt.show()
    
    
c,r = read("mc_swap_kp.log")
draw(c,r,[1250,3750,5000],["Kuhn Poker","Cheese Maze","Kuhn Poker"])
    
    
    
    