"""Plot Graph"""

import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def graph2010():
    labels = "Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease", "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes", "Tuberculosis"
    sizes = [58076, 32861, 20018, 18399, 16369, 13763, 8788, 7062, 6855, 4467]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'yellow', 'red', 'white', 'blue', 'magenta', 'cyan']
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    plt.show()
graph2010()
