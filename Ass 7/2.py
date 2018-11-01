#BAR CHART

import numpy as np
import matplotlib.pyplot as plt

city1 = [500 , 700 , 1500 , 890 ]
city2 = [485 , 730 , 1600 , 950 ]
ind = np.arange(len(city1))
width = 0.30
fig , ax = plt.subplots() 
pcity1 = ax.bar(ind - width/2, city1 , width , color = 'black' , label = 'city1')
pcity2 = ax.bar(ind + width/2, city2 , width , color = 'blue' , label = 'city2')
ax.set_ylabel('Population')
ax.set_xlabel('City')
ax.set_xticks(ind)
ax.set_xticklabels(( 'Year-1' , 'Year-2' , 'Year-3' , 'Year-4' ))
ax.legend()


def autolabel(rects, xpos='center'):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(pcity1, "left")
autolabel(pcity2, "right")

plt.show()