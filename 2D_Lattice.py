import matplotlib.pyplot as plt     # main framework for graphing
from matplotlib.ticker import MultipleLocator   # support for custom spaced grid lines 
import numpy as np  # various mathematical functions 
import random  # random numbers obviously

def make_grid(figure_size, x_limit, y_limit):

    plt.figure(figsize =(figure_size, figure_size))     # make figure square 
    plt.xlim(0, x_limit)    # define xlim to go from 0 to positive x_limit 
    plt.ylim(0, y_limit)    # define ylim to go from 0 to positive y_limit 
    
    plt.grid(True, which = 'both')  # show both major and minor grid lines 
    plt.gca().set_aspect('equal', adjustable = 'box')   # make the aspect ratio a perfect square 
    
    plt.gca().xaxis.set_minor_locator(MultipleLocator(1))   # minor grid lines on x axis are spaced 1 unit apart 
    plt.gca().yaxis.set_minor_locator(MultipleLocator(1))   # minor grid lines on y axis are spaced 1 unit apart 
        

def make_point(x_value, y_value):
    
    plt.plot(x_value, y_value, 'ro')    # make a red dot at (x_value, y_value)
    
    
def connect_points(x_values, y_values):
    
    plt.plot(x_values, y_values, linestyle = '-', color = 'red', linewidth = 1)     # makes a red line from one point to another
    
    
if __name__ == "__main__":

    figure_size = 6
    x_limit = 12 
    y_limit = 12
    
    make_grid(figure_size, x_limit, y_limit)
    
    visited_array = np.full((x_limit - 1, y_limit - 1), False, dtype = bool)    
    
    current_X = random.randint(0,10)
    current_Y = random.randint(0,10)
    
    count = 0
    
    while True:
    
        make_point(current_Y + 1, current_X + 1)
        
        if count > 0:
            connect_points([current_Y + 1, last_Y + 1], [current_X + 1, last_X + 1])
        
        plt.pause(0.1)
    
        visited_array[current_X][current_Y] = True 
        
        available_directions = [] 
        
        if current_X > 0 and visited_array[current_X - 1][current_Y] == False: 
            available_directions.append('Minus X') 
            
        if current_Y > 0 and visited_array[current_X][current_Y - 1] == False: 
            available_directions.append('Minus Y') 
            
        if current_X < x_limit - 2 and visited_array[current_X + 1][current_Y] == False: 
            available_directions.append('Plus X') 
            
        if current_Y < y_limit - 2 and visited_array[current_X][current_Y + 1] == False:
            available_directions.append('Plus Y') 
            
            
        if len(available_directions) == 0:
            print('Done')
            break
            
        direction = random.choice(available_directions) 
        
        last_X = current_X
        last_Y = current_Y 
        
        if direction == 'Minus X': 
            current_X = current_X - 1
            
        if direction == 'Minus Y': 
            current_Y = current_Y - 1
            
        if direction == 'Plus X': 
            current_X = current_X + 1 
            
        if direction == 'Plus Y': 
            current_Y = current_Y + 1 
            
        count = count + 1
            
    plt.show()