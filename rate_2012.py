"""Plot rate graph in year 2012"""
import numpy as np
import matplotlib.pyplot as plt

n = 10
rate = (98.5, 51.6, 37.4, 32.9, 26.1, 22.9, 14.6, 10.8, 12.1, 8.3)
ind = np.arange(n)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind + width, rate, width, color="r")

ax.set_ylabel("Rates")
ax.set_title("Cause of Death in Year 2012 (Rates)")
ax.set_xticks(ind + width+0.2)
ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"),rotation="vertical")

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.1f' % height,
                ha='center', va='bottom')

autolabel(rects1)
plt.show()

