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

def get_means_men(data_set, _input):
    if (_input == 2009):
        return (float(data_set[3][1]), float(data_set[4][1]), float(data_set[5][1]),\
                 float(data_set[6][1]), float(data_set[7][1]),float(data_set[8][1]),\
                 float(data_set[9][1]), float(data_set[10][1]),\
                 float(data_set[11][1]), float(data_set[12][1]))
    elif (_input == 2010):
        return (float(data_set[3][3]), float(data_set[4][3]), float(data_set[5][3]),\
                 float(data_set[6][3]), float(data_set[7][3]),float(data_set[8][3]),\
                 float(data_set[9][3]), float(data_set[10][3]),\
                 float(data_set[11][3]), float(data_set[12][3]))
    elif (_input == 2011):
        return (float(data_set[3][5]), float(data_set[4][5]), float(data_set[5][5]),\
                 float(data_set[6][5]), float(data_set[7][5]),float(data_set[8][5]),\
                 float(data_set[9][5]), float(data_set[10][5]),\
                 float(data_set[11][5]), float(data_set[12][5]))
    elif (_input == 2012):
        return (float(data_set[3][7]), float(data_set[4][7]), float(data_set[5][7]),\
                 float(data_set[6][7]), float(data_set[7][7]),float(data_set[8][7]),\
                 float(data_set[9][7]), float(data_set[10][7]),\
                 float(data_set[11][7]), float(data_set[12][7]))
    elif (_input == 2013):
        return (float(data_set[3][9]), float(data_set[4][9]), float(data_set[5][9]),\
                 float(data_set[6][9]), float(data_set[7][9]),float(data_set[8][9]),\
                 float(data_set[9][9]), float(data_set[10][9]),\
                 float(data_set[11][9]), float(data_set[12][9]))
    elif (_input == 'accident'):
        return (float(data_set[4][1]), float(data_set[4][3]), float(data_set[4][5]),\
                 float(data_set[4][7]), float(data_set[4][9]))
    elif (_input == 'cancer'):
        return (float(data_set[3][1]), float(data_set[3][3]), float(data_set[3][5]),\
                 float(data_set[3][7]), float(data_set[3][9]))
    elif (_input == 'commit'):
        return (float(data_set[10][1]), float(data_set[10][3]), float(data_set[10][5]),\
                 float(data_set[10][7]), float(data_set[10][9]))
    elif (_input == 'diabetes'):
        return (float(data_set[11][1]), float(data_set[11][3]), float(data_set[11][5]),\
                 float(data_set[11][7]), float(data_set[11][9]))
    elif (_input == 'heart'):
        return (float(data_set[6][1]), float(data_set[6][3]), float(data_set[6][5]),\
                 float(data_set[6][7]), float(data_set[6][9]))
    elif (_input == 'highblood'):
        return (float(data_set[5][1]), float(data_set[5][3]), float(data_set[5][5]),\
                 float(data_set[5][7]), float(data_set[5][9]))
    elif (_input == 'liver'):
        return (float(data_set[9][1]), float(data_set[9][3]), float(data_set[9][5]),\
                 float(data_set[9][7]), float(data_set[9][9]))
    elif (_input == 'lung'):
        return (float(data_set[7][1]), float(data_set[7][3]), float(data_set[7][5]),\
                 float(data_set[7][7]), float(data_set[7][9]))
    elif (_input == 'nephritis'):
        return (float(data_set[8][1]), float(data_set[8][3]), float(data_set[8][5]),\
                 float(data_set[8][7]), float(data_set[8][9]))
    elif (_input == 'tuber'):
        return (float(data_set[12][1]), float(data_set[12][3]), float(data_set[12][5]),\
                 float(data_set[12][7]), float(data_set[12][9]))
    else:
        print ("Error")

def get_color(_input):
    if (_input == 2009):
        return '#3300FF'
    elif (_input == 2010):
        return '#FF9966'
    elif (_input == 2011):
        return '#FF9900'
    elif (_input == 2012):
        return '#66CC00'
    elif (_input == 2013):
        return '#3366CC'
    else:
        print ("red")

def get_barWidth(_input):
    if (_input == 'all'):
        return 0.15
    else:
        return 0.35

def get_xlabel(_input):
    if ((type(_input) is int) or _input == 'all'):
        return 'Cause of Death'
    else:
        return 'Year'

def get_ylabel(_input):
    if (type(_input) is str):
        return 'Amount'
    else:
        return 'Rates'

def receive_input():
    _input = input("Please input (2009 - 2013, all, type of Cause of Death(accident, cancer, commit, diabetes, heart, highblood, liver, lung, nephritis, tuber)): ")

    if (_input == 'all' or _input == 'accident' or _input == 'cancer' or _input == 'commit' 
        or _input == 'diabetes' or _input == 'heart' or _input == 'highblood' or _input == 'liver' 
        or _input == 'lung' or _input == 'nephritis' or _input == 'tuber'):
        return _input
    else:
        return int(_input)

def get_nGroup(_input):
    if (type(_input) is int):
        return 10
    elif (_input == 'all'):
        return 10
    else:
        return 5

def get_index(_input, n_groups):
    if ((type(_input) is int) or _input == 'all'):
        return np.arange(n_groups)
    else:
        return np.arange(n_groups)+4

def get_title(_input):
    if (type(_input) is int):
        return 'Cause of Death'
    elif(_input == 'all'):
        return 'Cause of Death in Year 2009-2013 (Amount)'
    else:
        return _input + ' in Year 2009-2013 (Amount)'

def get_xticksSize(_input, index, bar_width):
    if (type(_input) is int):
        return index + bar_width
    elif(_input == 'all'):
        return index + bar_width + 0.4
    else:
        return index + bar_width + 0.2

def get_xticksData(_input):
    if ((type(_input) is int) or _input == 'all'):
        return ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis")
    else:
        return ("2009", "2010", "2011", "2012", "2013")

def main():
    """Main Programe if user input number from
    select year ecch 2009, 2010, 2011, 2012
    """

    """ receive an input """
    _input = receive_input()

    """ Prepare data for display """
    workbook = get_workbook()
    worksheet = get_worksheet(workbook)
    data_set = get_dataset(worksheet)
    means_men = get_means_men(data_set, _input)

    if (_input != 'all'):
        means_men = get_means_men(data_set, _input)
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

    n_groups = get_nGroup(_input)

    """ Display """
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = get_barWidth(_input)
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    if(type(_input) is int):
        rects1 = plt.bar(index+0.4, means_men, bar_width,\
                         alpha=opacity,
                         color=get_color(_input),
                         error_kw=error_config,
                         label=int(_input)
                         )
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                int(height),
                ha='center', va='bottom')
    elif(_input == 'all'):
        rects1 = ax.bar(index+0.2 + bar_width, amount_2009, bar_width, color="gold")
        rects2 = ax.bar(index+0.2 + bar_width*2, amount_2010, bar_width, color="lightskyblue")
        rects3 = ax.bar((index+0.2 + bar_width*3), amount_2011, bar_width, color="tomato")
        rects4 = ax.bar((index+0.2 + bar_width*4), amount_2012, bar_width, color="seagreen")
        rects5 = ax.bar((index+0.2 + bar_width*5), amount_2013, bar_width, color="tan")
        plt.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]),("Year 2009", "Year 2010", "Year 2011", "Year 2012", "Year 2013"))

    else:
        rects1 = plt.bar(index+0.4, means_men, bar_width,\
                         alpha=opacity,
                         color=get_color(_input),
                         error_kw=error_config,
                         # label=int(_input)
                         )
 
    plt.ylabel(get_ylabel(_input))
    plt.xlabel(get_ylabel(_input))
    plt.title(get_title(_input))
    #print (index, bar_width, index + bar_width +0.5)
    plt.xticks(get_xticksSize(_input, index+0.2, bar_width), get_xticksData(_input), rotation="vertical")
    
    plt.legend()
    plt.tight_layout()
        
    plt.show()
    
main()
