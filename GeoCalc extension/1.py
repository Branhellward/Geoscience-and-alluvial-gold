import openpyxl


book = openpyxl.open('tt.xlsx', read_only=True)
sheet = book.active
# reverse_export_file = open(export_reverse_file, 'w')
i = open('new.txt','w')


for row in range (3,sheet.max_row+1):
    coord_line = str(
        sheet[row][0].value)+'; '+str(
            sheet[row][1].value)+' '+str(
                sheet[row][2].value)+' '+str(
                    sheet[row][3].value)+'; '+str(
                        sheet[row][4].value)+' '+str(
                            sheet[row][5].value)+' '+str(
                                sheet[row][6].value)+';\n'



    i.write(coord_line)
i.close()
# print(coord_line)
    # print(sheet.max_row-2)