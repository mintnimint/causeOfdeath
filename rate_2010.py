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
ax.set_xticks(ind + width)
ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"))

plt.show()
