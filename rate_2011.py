import numpy as np
import matplotlib.pyplot as plt

n = 10
rate = (95.2, 52.8, 35.8, 31.4, 26.3, 23, 14, 10.6, 11.9, 7.5)
ind = np.arange(n)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind + width, rate, width, color="r")

ax.set_ylabel("Rates")
ax.set_title("Cause of Death in Year 2011 (Rates)")
ax.set_xticks(ind + width)
ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"))

plt.show()
