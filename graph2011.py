"""Plot Graph by matplotlib"""

import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.

def graph2011():
    """Show graph that Plot total of cause death year 2011"""
    labels = "Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease", "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes", "Tuberculosis"
    sizes = [61082, 33868, 22947, 20130, 16884, 14753, 9009, 6814, 7625, 4784]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'yellow', 'red', 'white', 'blue', 'magenta', 'cyan']
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()
graph2011()
