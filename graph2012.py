"""Plot Graph"""

import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.

labels = "Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease", "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes", "Tuberculosis"
sizes = [63272, 33170, 24052, 21142, 16772, 14697, 9409, 6960, 7749, 5354]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'yellow', 'red', 'white', 'blue', 'magenta', 'cyan']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()
