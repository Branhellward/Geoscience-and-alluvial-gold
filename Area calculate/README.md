# Area calculate

Here we make an area calculate table 

Using these modules

[XlsxWriter](https://pypi.org/project/XlsxWriter/) - link to pypi.

[Pandas](https://pypi.org/project/pandas/) - link to pypi.

[Regex](https://pypi.org/project/regex/) - link to pypi.

Sources:

* [Gauss's area formula](https://en.wikipedia.org/wiki/Shoelace_formula) - link to Wikipedia page

* The requirements of the expertise on making the table of mining allotment (MA), also the calculation of the area of mining allotment attached to the Draft Mining Allotment (DMA).

  Требования экспертизы по составлению таблицы Горного Отвода (ГО), а так же расчет площади горного отвода прикладываемый к Проекту Горного Отвода (ПГО).

---

At first this script was originally for [Global Mapper](https://www.bluemarblegeo.com/global-mapper/) export file, but if you want - you can create your own .txt with data. Lets see.

1. Take the area for export:

![square_ex.png](\img\square_ex.png)

2. Export vector/lidar as .txt use this options (example):

![pref_ex.png](\img\pref_ex.png)

3. Take our export file and put it with main.py together, rename .txt file as 'square' than run the script (example).

![vector_ex.png](\img\vector_ex.png)

4. And here we have a result (example).

![result_ex.png](\img\result_ex.png)

​         

It can be useful when you need copy this table to Word (doc or docx) file or AutoCAD dwg file

------

If you need - you can replace English to Russian use comments in source

```python
worksheet.write('A' + str(data_shape + 1), 'Amount', write_format_square)                      # Amount value - Сумма
worksheet.write('D' + str(data_shape + 1), ('=SUM(D2:' + str(dd) + ')'), write_format_sum)     # Formula value
worksheet.write('E' + str(data_shape + 1), ('=SUM(E2:' + str(ee) + ')'), write_format_sum)     # Formula value
worksheet.write('A' + str(data_shape + 2), 'S (Ha)', write_format_square)                      # Hectare label - S (Га)
```



