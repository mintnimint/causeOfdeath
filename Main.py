import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os

def get_workbook():
    """ Make sure xls file and this file they are both in the same folder """
    currentWorkingDirectory = os.getcwd()
    path = 'C:/Users/Baimint/Desktop/causeOfdeath/data1.xls' #currentWorkingdirectory

    return xlrd.open_workbook(path)

def get_worksheet(workbook):
    return workbook.sheet_by_index(0) 

def get_dataset(worksheet):
    return [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]

def get_means_men(data_set, year):
    if (year == 2009):
        return (float(data_set[3][1]), float(data_set[4][1]), float(data_set[5][1]),\
                 float(data_set[6][1]), float(data_set[7][1]),float(data_set[8][1]),\
                 float(data_set[9][1]), float(data_set[10][1]),\
                 float(data_set[11][1]), float(data_set[12][1]))
    elif (year == 2010):
        return (float(data_set[3][3]), float(data_set[4][3]), float(data_set[5][3]),\
                 float(data_set[6][3]), float(data_set[7][3]),float(data_set[8][3]),\
                 float(data_set[9][3]), float(data_set[10][3]),\
                 float(data_set[11][3]), float(data_set[12][3]))
    elif (year == 2011):
        return (float(data_set[3][5]), float(data_set[4][5]), float(data_set[5][5]),\
                 float(data_set[6][5]), float(data_set[7][5]),float(data_set[8][5]),\
                 float(data_set[9][5]), float(data_set[10][5]),\
                 float(data_set[11][5]), float(data_set[12][5]))
    elif (year == 2012):
        return (float(data_set[3][7]), float(data_set[4][7]), float(data_set[5][7]),\
                 float(data_set[6][7]), float(data_set[7][7]),float(data_set[8][7]),\
                 float(data_set[9][7]), float(data_set[10][7]),\
                 float(data_set[11][7]), float(data_set[12][7]))
    elif (year == 2013):
        return (float(data_set[3][9]), float(data_set[4][9]), float(data_set[5][9]),\
                 float(data_set[6][9]), float(data_set[7][9]),float(data_set[8][9]),\
                 float(data_set[9][9]), float(data_set[10][9]),\
                 float(data_set[11][9]), float(data_set[12][9]))

def get_color(year):
    if (year == 2009):
        return '#3300FF'
    elif (year == 2010):
        return '#FF9966'
    elif (year == 2011):
        return '#FF9900'
    elif (year == 2012):
        return '#66CC00'
    elif (year == 2013):
        return '#3366CC'
    else:
        print ("Error")

def get_barWidth(year):
    if (year == 'all'):
        return 0.15
    else:
        return 0.35

def get_label(year):
    if (year == 'all'):
        return 'Amount'
    else:
        return 'Rates'

def receive_input():
    year = input("Please input year (2009 - 2013, all): ")

    if (year != "all"):
        while ((int(year) < 2009 or int(year) >2013)):
            print ("Error: year out of scope, Please fill again.")
            year = input("Please input year (2009 - 2013, all): ")

    if (year != 'all'):
        return int(year)
    else:
        return year

def main():
    """Main Programe if user input number from
    select year ecch 2009, 2010, 2011, 2012
    """

    """ receive an input """
    year = receive_input()

    """ Prepare data for display """
    workbook = get_workbook()
    worksheet = get_worksheet(workbook)
    data_set = get_dataset(worksheet)
    means_men = get_means_men(data_set, year)

    if (year != 'all'):
        means_men = get_means_men(data_set, year)
    else:
        amount_2009 = (float(data_set[3][1]), float(data_set[4][1]), float(data_set[5][1]), float(data_set[6][1]), float(data_set[7][1]),\
                   float(data_set[8][1]), float(data_set[9][1]), float(data_set[10][1]), float(data_set[11][1]), float(data_set[12][1]))
        amount_2010 = (float(data_set[3][3]), float(data_set[4][3]), float(data_set[5][3]), float(data_set[6][3]), float(data_set[7][3]),\
                       float(data_set[8][3]), float(data_set[9][3]), float(data_set[10][3]), float(data_set[11][3]), float(data_set[12][3]))
        amount_2011 = (float(data_set[3][5]), float(data_set[4][5]), float(data_set[5][5]), float(data_set[6][5]), float(data_set[7][5]),\
                       float(data_set[8][5]), float(data_set[9][5]), float(data_set[10][5]), float(data_set[11][5]), float(data_set[12][5]))
        amount_2012 = (float(data_set[3][7]), float(data_set[4][7]), float(data_set[5][7]), float(data_set[6][7]), float(data_set[7][7]),\
                       float(data_set[8][7]), float(data_set[9][7]), float(data_set[10][7]), float(data_set[11][7]), float(data_set[12][7]))
        amount_2013 = (float(data_set[3][9]), float(data_set[4][9]), float(data_set[5][9]), float(data_set[6][9]), float(data_set[7][9]),\
                       float(data_set[8][9]), float(data_set[9][9]), float(data_set[10][9]), float(data_set[11][9]), float(data_set[12][9]))

    n_groups = 10

    """ Display """
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = get_barWidth(year)
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    if (year != 'all'):
        rects1 = plt.bar(index+0.4, means_men, bar_width,\
                         alpha=opacity,
                         color=get_color(year),
                         error_kw=error_config,
                         label=year)
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                int(height),
                ha='center', va='bottom')
    else :
        rects1 = ax.bar(index + bar_width, amount_2009, bar_width, color="gold")
        rects2 = ax.bar(index + bar_width*2, amount_2010, bar_width, color="lightskyblue")
        rects3 = ax.bar((index + bar_width*3), amount_2011, bar_width, color="tomato")
        rects4 = ax.bar((index + bar_width*4), amount_2012, bar_width, color="seagreen")
        rects5 = ax.bar((index + bar_width*5), amount_2013, bar_width, color="tan")
        plt.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]),("Year 2009", "Year 2010", "Year 2011", "Year 2012", "Year 2013"))
 
    plt.ylabel(get_label(year))
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year ' + str(year) + ' (Amount)')
    plt.xticks(index + bar_width + 0.2, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    
    plt.legend()
    plt.tight_layout() 
    plt.show()
    
main()
