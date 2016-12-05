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
