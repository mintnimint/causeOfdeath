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
        return (float(data_set[3][2]), float(data_set[4][2]), float(data_set[5][2]),\
                 float(data_set[6][2]), float(data_set[7][2]),float(data_set[8][2]),\
                 float(data_set[9][2]), float(data_set[10][2]),\
                 float(data_set[11][2]), float(data_set[12][2]))
    elif (year == 2010):
        return (float(data_set[3][4]), float(data_set[4][4]), float(data_set[5][4]),\
                 float(data_set[6][4]), float(data_set[7][4]),float(data_set[8][4]),\
                 float(data_set[9][4]), float(data_set[10][4]),\
                 float(data_set[11][4]), float(data_set[12][4]))
    elif (year == 2011):
        return (float(data_set[3][6]), float(data_set[4][6]), float(data_set[5][6]),\
                 float(data_set[6][6]), float(data_set[7][6]),float(data_set[8][6]),\
                 float(data_set[9][6]), float(data_set[10][6]),\
                 float(data_set[11][6]), float(data_set[12][6]))
    elif (year == 2012):
        return (float(data_set[3][8]), float(data_set[4][8]), float(data_set[5][8]),\
                 float(data_set[6][8]), float(data_set[7][8]),float(data_set[8][8]),\
                 float(data_set[9][8]), float(data_set[10][8]),\
                 float(data_set[11][8]), float(data_set[12][8]))
    elif (year == 2013):
        return (float(data_set[3][10]), float(data_set[4][10]), float(data_set[5][10]),\
                 float(data_set[6][10]), float(data_set[7][10]),float(data_set[8][10]),\
                 float(data_set[9][10]), float(data_set[10][10]),\
                 float(data_set[11][10]), float(data_set[12][10]))
    else:
        print ("Error")

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

def main():
    """Main Programe if user input number from
    select year ecch 2009, 2010, 2011, 2012
    """

    """ import data section """
    year = int(input("Please input year (2009 - 2013): "))

    while (year < 2009 or year > 2013):
        print ("Error: year out of scope, Please fill again.")
        year = int(input("Please input year (2009 - 2013): "))

    """ Prepare data for display """
    workbook = get_workbook()
    worksheet = get_worksheet(workbook)
    data_set = get_dataset(worksheet)
    means_men = get_means_men(data_set, year)
    n_groups = 10

    """ Display """
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, means_men, bar_width,\
                     alpha=opacity,
                     color=get_color(year),
                     error_kw=error_config,
                     label=year)
 
    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year ' + str(year) + ' (Rates)')
    plt.xticks(index + bar_width, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend()
    plt.tight_layout() 
    plt.show()
    
main()
