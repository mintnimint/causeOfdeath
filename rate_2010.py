"""Plot rate graph in year 2010"""
import numpy as np
import matplotlib.pyplot as plt

n = 10
rate = (91.2, 51.6, 31.4, 28.9, 25.7, 21.6, 13.8, 11.1, 10.8, 7)
ind = np.arange(n)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind + width, rate, width, color="r")

ax.set_ylabel("Rates")
ax.set_title("Cause of Death in Year 2010 (Rates)")
ax.set_xticks(ind + width + 0.2)
ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"), rotation="vertical")

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.1f' % height,
                ha='center', va='bottom')

autolabel(rects1)
plt.show()
