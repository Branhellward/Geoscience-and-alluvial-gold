# Txt to Xlsx

Here we make an empty table for export coordinates

Using a module for creating Excel XLSX files

[XlsxWriter](https://pypi.org/project/XlsxWriter/) - link to pypi.

[Pandas](https://pypi.org/project/pandas/) - link to pypi.

[Regex](https://pypi.org/project/regex/) - link to pypi.

Add some GUI using PyQt5 and QT Designer

[PyQt5](https://pypi.org/project/PyQt5/) - link to pypi.

---

At first this script was originally for [Global Mapper](https://www.bluemarblegeo.com/global-mapper/) export file, but if you want - you can create your own .txt with data. Lets see.

1. Take the area for export:

![area_ex](C:\Users\Lenforia\Desktop\GIT\Geoscience-and-coordinates\Txt to Xlsx\img\area_ex.png)

2. Export vector/lidar as .txt use this options (example):

![export_ex](C:\Users\Lenforia\Desktop\GIT\Geoscience-and-coordinates\Txt to Xlsx\img\export_ex.png)

3. This is Global Mapper export (example).

![export_ex_2](C:\Users\Lenforia\Desktop\GIT\Geoscience-and-coordinates\Txt to Xlsx\img\export_ex_2.png)

4. Run the program we have an interface.

![gui_ex](C:\Users\Lenforia\Desktop\GIT\Geoscience-and-coordinates\Txt to Xlsx\img\txt_to_xlsx_gui.png)

* At first select file
* Select "Number of decimal"
* Then click "Convert" button
* Choose path and name of new .xlsx file

5. And here we have a result (example).

![finish_ex](C:\Users\Lenforia\Desktop\GIT\Geoscience-and-coordinates\Txt to Xlsx\img\finish_ex.png)


It can be useful when you need copy this table to Word (doc or docx) file or AutoCAD dwg file

------

If you need - you can replace English to Russian use comments in source

```python
worksheet.merge_range('A1:A2', '№№', merge_format)
worksheet.merge_range('B1:D1', 'North Latitude', merge_format)   # 'Северная Широта'
worksheet.merge_range('E1:G1', 'East Longitude', merge_format)   # 'Восточная Долгота'
```



