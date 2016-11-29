"""plot total graph"""
import numpy as np
import matplotlib.pyplot as plt

def total():
    """Show Total graph"""
    # data
    n = 10
    amount_2009 = (56058, 35304, 15648, 18375, 14542, 13191, 8562, 6642, 7019, 4568)
    amount_2010 = (58076, 32861, 20018, 18399, 16369, 13763, 8788, 7062, 6855, 4467)
    amount_2011 = (61082, 33868, 22947, 20130, 16884, 14753, 9009, 6814, 7625, 4784)
    amount_2012 = (63272, 33170, 24052, 21142, 16772, 14697, 9409, 6960, 7749, 5354)
    amount_2013 = (67692, 32422, 28408, 24597, 21676, 15162, 10747, 6986, 9703, 5496)

    ind = np.arange(n)
    width = 0.15
    # plot
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, amount_2009, width, color="r")
    rects2 = ax.bar(ind + width*2, amount_2010, width, color="g")
    rects3 = ax.bar((ind + width*3), amount_2011, width, color="b")
    rects4 = ax.bar((ind + width*4), amount_2012, width, color="y")
    rects5 = ax.bar((ind + width*5), amount_2013, width, color="m")

    ax.set_ylabel("Amount")
    ax.set_title("Cause of Death (Amount)")
    ax.set_xticks(ind + width + 0.4)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                     "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                     "Tuberculosis"), rotation="vertical")
    ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]),("Year 2009", "Year 2010", "Year 2011", "Year 2012", "Year 2013"))

    plt.show()

total()
