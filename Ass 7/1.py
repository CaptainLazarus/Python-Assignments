#BAR CHART

import numpy as np
import matplotlib.pyplot as plt

students = [103 , 97 , 77 , 60 ]

ind = np.arange(len(students))
width = 0.50
fig , ax = plt.subplots() 
bar = ax.bar(ind , students , width , color = 'r' , label = 'boys')

ax.set_ylabel('strength')
ax.set_xlabel('Batch')
ax.set_xticks(ind)
ax.set_xticklabels(( '1st_Year' , '2nd_Year' , '3rd_Year' , '4^th_Year' ))
ax.legend()


def autolabel(rects, xpos='center'):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(bar, "left")


plt.show()



#PIE CHART


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '1st_Year' , '2nd_Year' , '3rd_Year' , '4^th_Year'
sizes = [103, 97, 77, 60]
explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()