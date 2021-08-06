import pandas as pd
import xlsxwriter
import regex

# open_file = ('phm_export_geo.txt')
open_file = open('phm_export_geo.txt').read()
regular_ka = r'\1.\2'
fine_text = regex.sub(r'(\d{0})+[.,]+(\d{0})',regular_ka ,open_file)
# print(fine_text)


wr = open('phm_export_geo.txt','w')
wr.write(fine_text)                                           # Write our file
wr.close()



data = pd.read_csv('phm_export_geo.txt', encoding='cp1251', header=None, sep=r"\s+", names=None, )
data=data.replace({';': ''}, regex=True)
# data.replace(';', '')
print(data)

workbook = xlsxwriter.Workbook('3.xlsx')  # Name of xlsx file/ Название файла
worksheet = workbook.add_worksheet('Coordinates')


# currency_format = workbook.add_format({'num_format': '$#,##0.00'})
# worksheet.write('A1', 1234.56, currency_format)


merge_format = workbook.add_format({
        'bold': 0,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

write_format = workbook.add_format({
        'bold': 0,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

write_format1 = workbook.add_format({
        'bold': 0,
        'border': 1,
        'num_format': "00.000000",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

worksheet.merge_range('A1:A2', '№№', merge_format)
worksheet.merge_range('B1:D1', 'North Latitude', merge_format)  # 'Северная Широта'
worksheet.merge_range('E1:G1', 'East Longitude', merge_format)  # 'Восточная Долгота'
worksheet.write('B2', 'Degrees', write_format)  # 'Градусы'
worksheet.write('C2', 'Minutes', write_format)  # 'Минуты'
worksheet.write('D2', 'Seconds', write_format)  # 'Секунды'
worksheet.write('E2', 'Degrees', write_format)  # 'Градусы'
worksheet.write('F2', 'Minutes', write_format)  # 'Минуты'
worksheet.write('G2', 'Seconds', write_format)  # 'Секунды'
worksheet.write('A1', '№№', write_format1)

a = 0
data_shape = data.shape[0]
bcolmn = 'B'
b = 0
ccolmn = 'C'
c = 0
dcolmn = 'D'
d = 0
ecolmn = 'E'
e = 0
fcolmn = 'F'
f = 0
gcolmn = 'G'
g = 0
yy = -1

while a < data_shape:
    a += 1
    b += 1
    c += 1
    d += 1
    e += 1
    f += 1
    g += 1
    yy += 1
    vertical_2 = ('A' + str(a + 2))
    bb = (bcolmn + str(b + 2))
    cc = (ccolmn + str(c + 2))
    dd = (dcolmn + str(d + 2))
    ee = (ecolmn + str(e + 2))
    ff = (fcolmn + str(f + 2))
    gg = (gcolmn + str(g + 2))

    worksheet.write(vertical_2, a, write_format)
    
    float_iat_3 = float(data.iat[yy, 3])

    worksheet.write(bb, data.iat[yy, 1], write_format)
    worksheet.write(cc, data.iat[yy, 2], write_format)
    worksheet.write(dd, float_iat_3, write_format1)
    worksheet.write(ee, data.iat[yy, 4], write_format)
    worksheet.write(ff, data.iat[yy, 5], write_format)
    worksheet.write(gg, data.iat[yy, 6], write_format1)

workbook.close()