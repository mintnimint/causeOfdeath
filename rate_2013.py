"""Plot rate graph in year 2013"""
import numpy as np
import matplotlib.pyplot as plt

def rate_2013():
    """show rate graph cause of death in year 2013"""
    n = 10
    rate = (104.8, 50.2, 44, 38.1, 33.5, 23.5, 16.6, 10.8, 15, 8.5)
    ind = np.arange(n)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, rate, width, color="r")

    ax.set_ylabel("Rates")
    ax.set_title("Cause of Death in Year 2013 (Rates)")
    ax.set_xticks(ind + width + 0.2)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"), rotation="vertical")

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.1f' % height,
                ha='center', va='bottom')
    plt.show()
rate_2013()
