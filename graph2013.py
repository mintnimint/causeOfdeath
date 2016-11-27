"""Plot Graph by mathplotlib"""

import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
def graph2013():
    """show graph that Plot total of cause death year 2013"""
    labels = "Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease", "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes", "Tuberculosis"
    sizes = [67692, 32422, 28408, 24597, 21676, 15162, 10747, 6986, 9703, 5496]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'yellow', 'red', 'white', 'blue', 'magenta', 'cyan']
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()
graph2013()
