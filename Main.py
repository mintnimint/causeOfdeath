import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import xlrd


def main():
"""Main Programe if user input number from
    select year ecch 2009, 2010, 2011, 2012
    """

    """ import data section """
    year = int(input("Please input year (2009 - 2013): "))

    while (year < 2009 or year >2013):
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
    
def year_2009():
    """Show bar chart """
    path = 'C:\Python34\ProjectPython\data1.xls'
    workbook = xlrd.open_workbook(path) 
    worksheet = workbook.sheet_by_index(0) 
    data_set = [[worksheet.cell_value(row,col) for col in range(worksheet.ncols)] for
                row in range(worksheet.nrows)]
    n_groups = 10
    means_men = (float(data_set[3][2]), float(data_set[4][2]), float(data_set[5][2]),\
                 float(data_set[6][2]), float(data_set[7][2]),float(data_set[8][2]),\
                 float(data_set[9][2]), float(data_set[10][2]),\
                 float(data_set[11][2]), float(data_set[12][2]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, means_men, bar_width,\
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
    means_men = (float(data_set[3][4]), float(data_set[4][4]), float(data_set[5][4]),\
                 float(data_set[6][4]), float(data_set[7][4]),float(data_set[8][4]),\
                 float(data_set[9][4]), float(data_set[10][4]),\
                 float(data_set[11][4]), float(data_set[12][4]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, means_men, bar_width,\
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
    means_men = (float(data_set[3][6]), float(data_set[4][6]), float(data_set[5][6]),\
                 float(data_set[6][6]), float(data_set[7][6]),float(data_set[8][6]),\
                 float(data_set[9][6]), float(data_set[10][6]),\
                 float(data_set[11][6]), float(data_set[12][6]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, means_men, bar_width,\
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
    means_men = (float(data_set[3][8]), float(data_set[4][8]), float(data_set[5][8]),\
                 float(data_set[6][8]), float(data_set[7][8]),float(data_set[8][8]),\
                 float(data_set[9][8]), float(data_set[10][8]),\
                 float(data_set[11][8]), float(data_set[12][8]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, means_men, bar_width,\
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
    means_men = (float(data_set[3][10]), float(data_set[4][10]), float(data_set[5][10]),\
                 float(data_set[6][10]), float(data_set[7][10]),float(data_set[8][10]),\
                 float(data_set[9][10]), float(data_set[10][10]),\
                 float(data_set[11][10]), float(data_set[12][10]))
 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, means_men, bar_width,\
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

main()
