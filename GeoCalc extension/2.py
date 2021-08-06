import xlsxwriter
import pandas as pd
import regex


open_file = open('gm_export.txt').read()

cleaner = r'\1.\2'
fine_text = regex.sub(r'(\d{0})+[.,]+(\d)', cleaner, open_file)


wr = open('gm_export.txt','w')
wr.write(fine_text)
wr.close()

data = pd.read_csv('gm_export.txt', encoding='cp1251', header=None, sep=r"\s+", names=None)
print(data)

workbook = xlsxwriter.Workbook('exexexexe.xlsx')
worksheet = workbook.add_worksheet('Coordinates')

worksheet.set_column('B:C', 16.22)
worksheet.set_column('D:E', 24.33)

write_format_hat = workbook.add_format({
        'font': 'Times New Roman',
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

write_format = workbook.add_format({
        'bold': 0,
        'border': 1,
        'num_format': "0.000",
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})


worksheet.write('A1', '№№', write_format_hat)
worksheet.write('B1', 'X', write_format_hat)
worksheet.write('C1', 'Y', write_format_hat)

a = 0
data_shape = data.shape[0]
data_shape_2 = data.shape[0] - 1
bcolmn = 'B'
b = 0
ccolmn = 'C'
c = 0

while a < data_shape_2:
    vertical = ('A' + str(a + 2))
    bb = (bcolmn + str(b + 2))
    cc = (ccolmn + str(c + 2))

    worksheet.write(bb, data.iat[a, 0], write_format)
    worksheet.write(cc, data.iat[a, 1], write_format) 

    a += 1
    b += 1 
    c += 1

    worksheet.write(vertical, a, write_format_hat)

workbook.close()