import openpyxl


book = openpyxl.open('test.xlsx', read_only=True)
sheet = book.active

i = open('new.txt','w')

for row in range (2,sheet.max_row+1):
    coord_line = str(
        sheet[row][0].value)+'; '+str(
            sheet[row][1].value)+'; '+str(
                sheet[row][2].value)+';\n'
    print(coord_line)

    i.write(coord_line)
i.close()