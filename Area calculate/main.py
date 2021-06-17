import xlsxwriter
import pandas as pd
import regex

global cleaner                                                  # Variable for regular expression
global dd, ee                                                   # Internal calculations for sum


def make_xlsx():
    open_first = open('square.txt').read()                      # Prepare file for further work
    global cleaner                                              # Use some regular expression
    cleaner = r'\1.\2'                                          #
    fine_txt = regex.sub(r'(\d{0})+[.,]+(\d)', cleaner, open_first)
    f = open("square.txt", 'w')                                 #
    f.write(fine_txt)                                           # Write our file
    f.close()
    data = pd.read_csv("square.txt", encoding='cp1251', header=None, sep=r"\s+", names=None)

    workbook = xlsxwriter.Workbook("Area calculate.xlsx")       # Name of our .xlsx file
    worksheet = workbook.add_worksheet('Area calculate')

    worksheet.set_column('B:C', 16.22)                          # Set the cell width
    worksheet.set_column('D:E', 24.33)                          # Set the cell width

    write_format_hat = workbook.add_format({                    # Make style for table header
        'font': 'Times New Roman',
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format_sum = workbook.add_format({                    # Make style for sum cells
        'bold': 1,
        'border': 1,
        'num_format': "0",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format_for_formula = workbook.add_format({            # Make style for formula cells
        'bold': 0,
        'border': 1,
        'num_format': "0",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format_square = workbook.add_format({                 # Make style for square digit cells
        'bold': 1,
        'border': 1,
        'num_format': '0.00000',
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    write_format = workbook.add_format({                        # Make style for other information
        'bold': 0,
        'border': 1,
        'num_format': "0.000",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    worksheet.write('A1', '№№', write_format_hat)               #
    worksheet.write('B1', 'X', write_format_hat)                #
    worksheet.write('C1', 'Y', write_format_hat)                # Make the header of the table
    worksheet.write('D1', 'Xn*Yn+1', write_format_hat)          #
    worksheet.write('E1', 'Yn*Xn+1', write_format_hat)          #

    a = 0                                                       #
    data_shape = data.shape[0]                                  #
    z = data.shape[0] - 1                                       #
    bcolmn = 'B'                                                #
    b = 0                                                       # Letter
    ccolmn = 'C'                                                # Variables
    c = 0                                                       #
    dcolmn = 'D'                                                #
    d = 0                                                       #
    ecolmn = 'E'                                                #
    e = 0                                                       #
    x = z + 1                                                   #
    form_a = 1                                                  #
    form_b = 1                                                  #

    global dd, ee                                               # Internal calculations for sum

    while a < z:
        vertical = ('A' + str(a + 2))
        bb = (bcolmn + str(b + 2))
        cc = (ccolmn + str(c + 2))
        dd = (dcolmn + str(d + 2))
        ee = (ecolmn + str(e + 2))

        worksheet.write(bb, data.iat[a, 0], write_format)       #
        worksheet.write(cc, data.iat[a, 1], write_format)       #
        form_c = float((data.iat[a, 0]) * (data.iat[form_a, 1]))    # Fill cells with
        form_d = float((data.iat[form_b, 0]) * (data.iat[a, 1]))    # .txt digital value
        worksheet.write(dd, form_c, write_format_for_formula)   #
        worksheet.write(ee, form_d, write_format_for_formula)   #

        a += 1                                                  #
        b += 1                                                  #
        d += 1                                                  #
        c += 1                                                  # Cells
        x -= 1                                                  # Counter
        e += 1                                                  #
        form_a += 1                                             #
        form_b += 1                                             #

        worksheet.write(vertical, a, write_format_hat)          # Number of row

    worksheet.write('A' + str(data_shape + 1), 'Amount', write_format_square)                      # Amount value
    worksheet.write('D' + str(data_shape + 1), ('=SUM(D2:' + str(dd) + ')'), write_format_sum)     # Formula value
    worksheet.write('E' + str(data_shape + 1), ('=SUM(E2:' + str(ee) + ')'), write_format_sum)     # Formula value
    worksheet.write('A' + str(data_shape + 2), 'S (Ha)', write_format_square)                      # Hectare label
    worksheet.write('B' + str(data_shape + 2), '=' + 'ABS' + '(' + '(' +
                    ((dcolmn + str(data_shape + 1) + '-' + ecolmn + str(data_shape + 1)) +       # Square formula value
                     ')' + '*0.5/10000' + ')'), write_format_square)
    workbook.close()


make_xlsx()
