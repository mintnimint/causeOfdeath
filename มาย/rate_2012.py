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
ax.set_xticks(ind + width)
ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"))

plt.show()
