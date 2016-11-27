import numpy as np
import matplotlib.pyplot as plt

n = 10
rate = (104.8, 50.2, 44, 38.1, 33.5, 23.5, 16.6, 10.8, 15, 8.5)
ind = np.arange(n)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind + width, rate, width, color="r")

ax.set_ylabel("Rates")
ax.set_title("Cause of Death in Year 2013 (Rates)")
ax.set_xticks(ind + width)
ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"))
