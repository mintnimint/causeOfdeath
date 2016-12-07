import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd

def total_year():
    """Show bar chart """
    path = 'C:/Users/Baimint/Desktop/causeOfdeath/data1.xls' #currentWorkingdirectory
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
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
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.4

    rects1 = ax.bar(index + bar_width, amount_2009, bar_width, color="gold")
    rects2 = ax.bar(index + bar_width*2, amount_2010, bar_width, color="lightskyblue")
    rects3 = ax.bar((index + bar_width*3), amount_2011, bar_width, color="tomato")
    rects4 = ax.bar((index + bar_width*4), amount_2012, bar_width, color="seagreen")
    rects5 = ax.bar((index + bar_width*5), amount_2013, bar_width, color="tan")

    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year 2009-2013 (Amount)')
    plt.xticks(index + bar_width + 0.4, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]),("Year 2009", "Year 2010", "Year 2011", "Year 2012", "Year 2013"))
    plt.tight_layout() 
    plt.show()
    
total_year()
