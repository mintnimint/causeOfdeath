import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd

def total_year():
    """Show bar chart """
    path = 'C:/Users/Baimint/Desktop/causeOfdeath/data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
    cancer = sum((float(data_set[3][2]), float(data_set[3][4]), float(data_set[3][6]),\
                 float(data_set[3][8]),float(data_set[3][10])))
    accident = sum((float(data_set[4][2]), float(data_set[4][4]), float(data_set[4][6]),\
                 float(data_set[4][8]),float(data_set[4][10])))
    high_bd = sum((float(data_set[5][2]), float(data_set[5][4]), float(data_set[5][6]),\
                 float(data_set[5][8]),float(data_set[5][10])))
    heart_ds = sum((float(data_set[6][2]), float(data_set[6][4]), float(data_set[6][6]),\
                 float(data_set[6][8]),float(data_set[6][10])))
    lung_ds = sum((float(data_set[7][2]), float(data_set[7][4]), float(data_set[7][6]),\
                 float(data_set[7][8]),float(data_set[7][10])))
    nephrit = sum((float(data_set[8][2]), float(data_set[8][4]), float(data_set[8][6]),\
                 float(data_set[8][8]),float(data_set[8][10])))
    liver_ds = sum((float(data_set[9][2]), float(data_set[9][4]), float(data_set[9][6]),\
                 float(data_set[9][8]),float(data_set[9][10])))
    commit_sc = sum((float(data_set[10][2]), float(data_set[10][4]), float(data_set[10][6]),\
                 float(data_set[10][8]),float(data_set[10][10])))
    diabetes = sum((float(data_set[11][2]), float(data_set[11][4]), float(data_set[11][6]),\
                 float(data_set[11][8]),float(data_set[11][10])))
    tubercul = sum((float(data_set[12][2]), float(data_set[12][4]), float(data_set[12][6]),\
                 float(data_set[12][8]),float(data_set[12][10])))
    data = (float(cancer), float(accident), float(high_bd),float(heart_ds), float(lung_ds),\
            float(nephrit), float(liver_ds), float(commit_sc),float(diabetes), float(tubercul))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.4
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index+0.2, data, bar_width,\
                     alpha=opacity,
                     error_kw=error_config,
                     label='2009 - 2013')
    
    rects1[0].set_color('yellowgreen')
    rects1[1].set_color('gold')
    rects1[2].set_color('lightskyblue')
    rects1[3].set_color('lightcoral')
    rects1[4].set_color('lightgrey')
    rects1[5].set_color('tomato')
    rects1[6].set_color('seagreen')
    rects1[7].set_color('royalblue')
    rects1[8].set_color('sienna')
    rects1[9].set_color('tan')

    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year 2009-2013 (Rates)')
    plt.xticks(index + bar_width, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend()
    plt.tight_layout() 
    plt.show()
    
total_year()
