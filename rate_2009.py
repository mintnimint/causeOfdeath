import numpy as np
import matplotlib.pyplot as plt

n = 10
#amount = (56058, 35304, 15648, 18375, 14542, 13191, 8562, 6642, 7019, 4568)
rate = (88.3, 55.6, 24.7, 29, 22.9, 20.8, 13.5, 10.5, 11.1, 7.2)
ind = np.arange(n)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind + width, rate, width, color="r")

ax.set_ylabel("Rates")
ax.set_title("Cause of Death in Year 2009 (Rates)")
ax.set_xticks(ind + width)
ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"))

plt.show()
