import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd


def main():
##    pie_chart()
    """Main Programe if user input number from
    select year ecch 2009, 2010, 2011, 2012, 2013
    """
    select = int(input("Please input year (2009 - 2013): "))
    if select == 2009:
        year_2009()
    elif select == 2010:
        year_2010()
    elif select == 2011:
        year_2011()
    elif select == 2012:
        year_2012()
    elif select == 2013:
        year_2013()
    else:
        print("ERROR")
    
def year_2009():
    """Show bar chart """
    path = 'C:\Python34\ProjectPython\data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
    data = (float(data_set[3][2]), float(data_set[4][2]), float(data_set[5][2]),\
                 float(data_set[6][2]), float(data_set[7][2]),float(data_set[8][2]),\
                 float(data_set[9][2]), float(data_set[10][2]),\
                 float(data_set[11][2]), float(data_set[12][2]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, data, bar_width,\
                     alpha=opacity,
                     color='#3300FF',
                     error_kw=error_config,
                     label='2009')
 
    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year 2009 (Rates)')
    plt.xticks(index + bar_width, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend()
    plt.tight_layout() 
    plt.show()

def year_2010():
    """Show bar chart """
    path = 'C:\Python34\ProjectPython\data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
    data = (float(data_set[3][4]), float(data_set[4][4]), float(data_set[5][4]),\
                 float(data_set[6][4]), float(data_set[7][4]),float(data_set[8][4]),\
                 float(data_set[9][4]), float(data_set[10][4]),\
                 float(data_set[11][4]), float(data_set[12][4]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, data, bar_width,\
                     alpha=opacity,
                     color='#FF9966',
                     error_kw=error_config,
                     label='2010')
 
    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year 2010 (Rates)')
    plt.xticks(index + bar_width, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend()
    plt.tight_layout() 
    plt.show()

def year_2011():
    """Show bar chart """
    path = 'C:\Python34\ProjectPython\data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
    data = (float(data_set[3][6]), float(data_set[4][6]), float(data_set[5][6]),\
                 float(data_set[6][6]), float(data_set[7][6]),float(data_set[8][6]),\
                 float(data_set[9][6]), float(data_set[10][6]),\
                 float(data_set[11][6]), float(data_set[12][6]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, data, bar_width,\
                     alpha=opacity,
                     color='#FF9900',
                     error_kw=error_config,
                     label='2011')
 
    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year 2011 (Rates)')
    plt.xticks(index + bar_width, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend()
    plt.tight_layout() 
    plt.show()

def year_2012():
    """Show bar chart """
    path = 'C:\Python34\ProjectPython\data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
    data = (float(data_set[3][8]), float(data_set[4][8]), float(data_set[5][8]),\
                 float(data_set[6][8]), float(data_set[7][8]),float(data_set[8][8]),\
                 float(data_set[9][8]), float(data_set[10][8]),\
                 float(data_set[11][8]), float(data_set[12][8]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, data, bar_width,\
                     alpha=opacity,
                     color='#66CC00',
                     error_kw=error_config,
                     label='2012')
 
    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year 2012 (Rates)')
    plt.xticks(index + bar_width, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend()
    plt.tight_layout() 
    plt.show()

def year_2013():
    """Show bar chart """
    path = 'C:\Python34\ProjectPython\data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
    data = (float(data_set[3][10]), float(data_set[4][10]), float(data_set[5][10]),\
                 float(data_set[6][10]), float(data_set[7][10]),float(data_set[8][10]),\
                 float(data_set[9][10]), float(data_set[10][10]),\
                 float(data_set[11][10]), float(data_set[12][10]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, data, bar_width,\
                     alpha=opacity,
                     color='#3366CC',
                     error_kw=error_config,
                     label='2013')
 
    plt.ylabel('Rates')
    plt.xlabel('Cause of Death')
    plt.title('Cause of Death in Year 2013 (Rates)')
    plt.xticks(index + bar_width, ("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                                   "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                                   "Tuberculosis"), rotation="vertical")
    plt.legend()
    plt.tight_layout() 
    plt.show()


def pie_chart():
    """show graph that Plot total of cause death year 2009 - 2013"""
    path = 'C:\Python34\ProjectPython\data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    
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
            float(), float(liver_ds), float(commit_sc),float(diabetes), float(tubercul))

    labels = "Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
             "Lung Disease","Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
             "Tuberculosis"
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightgrey',\
              'tomato', 'seagreen', 'royalblue', 'sienna', 'tan']
    explode = (0.1, 0, 0, 0,0,0.1, 0, 0, 0,0) 
    plt.pie(data, explode=explode, labels=labels, colors=colors,\
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.legend()
    plt.show()
    
main()
