# If you need - you can replace English to Russian use comments in source
# При необходимости вы можете заменить английский язык на русский в соответствии с комментариями

import xlsxwriter

number_of_cells = int(input('Input number of rows: '))  # 'Введи колличество угловых точек'
height = 1
dig = 3       # Digit
let = 'A'     # Letter
z = 1         # Counter

workbook = xlsxwriter.Workbook("Сoordinates.xlsx")   # Name of xlsx file/ Название файла
worksheet = workbook.add_worksheet('Сoordinates')    # Name of xlsx worksheet/ Название листа

merge_format = workbook.add_format({
    'bold': 0,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'white'})

worksheet.merge_range('A1:A2', '№№', merge_format)
worksheet.merge_range('B1:D1', 'North Latitude', merge_format)   # 'Северная Широта'
worksheet.merge_range('E1:G1', 'East Longitude', merge_format)   # 'Восточная Долгота'

write_format = workbook.add_format({
    'bold': 0,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'white'})

worksheet.write('B2', 'Degrees', write_format)  # 'Градусы'
worksheet.write('C2', 'Minutes', write_format)  # 'Минуты'
worksheet.write('D2', 'Seconds', write_format)  # 'Секунды'
worksheet.write('E2', 'Degrees', write_format)  # 'Градусы'
worksheet.write('F2', 'Minutes', write_format)  # 'Минуты'
worksheet.write('G2', 'Seconds', write_format)  # 'Секунды'


def number_of_rows():
    return let + str(dig)


while height <= number_of_cells:
    table = number_of_rows()
    worksheet.write(table, int(z), write_format)
    worksheet.write('B' + str(dig), None, write_format)
    worksheet.write('C' + str(dig), None, write_format)
    worksheet.write('D' + str(dig), None, write_format)
    worksheet.write('E' + str(dig), None, write_format)
    worksheet.write('F' + str(dig), None, write_format)
    worksheet.write('G' + str(dig), None, write_format)
    height += 1
    dig += 1
    z += 1

workbook.close()
