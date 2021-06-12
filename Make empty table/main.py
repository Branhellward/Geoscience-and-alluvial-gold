# If you need -> you can replace english to russian use comments

import xlsxwriter

workbook = xlsxwriter.Workbook("Сoordinates.xlsx")   # Name of xlsx file/ Название файла
worksheet = workbook.add_worksheet('Сoordinates')    # Name of xlsx worksheet/ Название листа

merge_format = workbook.add_format({
    'bold': 0,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'white'})

worksheet.merge_range('A1:A2', '№№', merge_format)
worksheet.merge_range('B1:D1', 'North latitude', merge_format)   # 'Северная широта'
worksheet.merge_range('E1:G1', 'East longitude', merge_format)   # 'Восточная долгота'

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

workbook.close()
