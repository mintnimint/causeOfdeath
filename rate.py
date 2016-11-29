"""plot Rate graph by matplotlib"""
import numpy as np
import matplotlib.pyplot as plt

def rate():
    """Show Total Rate graph"""

    # data
    n = 10
    rate_2009 = (88.3, 55.6, 24.7, 29, 22.9, 20.8, 13.5, 10.5, 11.1, 7.2)
    rate_2010 = (91.2, 51.6, 31.4, 28.9, 25.7, 21.6, 13.8, 11.1, 10.8, 7)
    rate_2011 = (95.2, 52.8, 35.8, 31.4, 26.3, 23, 14, 10.6, 11.9, 7.5)
    rate_2012 = (98.5, 51.6, 37.4, 32.9, 26.1, 22.9, 14.6, 10.8, 12.1, 8.3)
    rate_2013 = (104.8, 50.2, 44, 38.1, 33.5, 23.5, 16.6, 10.8, 15, 8.5)

    ind = np.arange(n)
    width = 0.15

    # plot
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, rate_2009, width, color="r")
    rects2 = ax.bar(ind + width*2, rate_2010, width, color="g")
    rects3 = ax.bar((ind + width*3), rate_2011, width, color="b")
    rects4 = ax.bar((ind + width*4), rate_2012, width, color="y")
    rects5 = ax.bar((ind + width*5), rate_2013, width, color="m")

    ax.set_ylabel("Rates")
    ax.set_title("Cause of Death (Rates)")
    ax.set_xticks(ind + width + 0.4)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"), rotation="vertical")

    ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]),("Year 2009", "Year 2010", "Year 2011", "Year 2012", "Year 2013"))

    plt.show()

rate()
