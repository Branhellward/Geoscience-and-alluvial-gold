def for_dms():
    counter = 1
    replacements = {'°':'', ' N':';', ' E':';', '\'':'', '\"':''}

    with open('1.txt') as input_file, open('3.txt', 'w') as output_file:
        for line in input_file:
            for src, target in replacements.items():
                line = line.replace(src, target)
            output_file.write( '{}{} {}'.format(counter,';', line))
            counter += 1 

def for_xy():
    counter = 1
    replacements = {'\n':';\n','\t':';\t'}

    with open('4.txt') as input_file, open('5.txt', 'w') as output_file:
        for line in input_file:
            for src, target in replacements.items():
                line = line.replace(src, target)
            output_file.write( '{}{} {}'.format(counter,';', line))
            counter += 1