# Txt to Xlsx

Here we make an empty table for export coordinates

Using a module for creating Excel XLSX files

[XlsxWriter](https://pypi.org/project/XlsxWriter/) - link to pypi.

Add some GUI using PyQt5 and QT Designer

[PyQt5](https://pypi.org/project/PyQt5/) - link to pypi.

---



It can be useful when you need copy this table to Word (doc or docx) file or AutoCAD dwg file

------

If you need - you can replace English to Russian use comments in source

```python
worksheet.merge_range('A1:A2', '№№', merge_format)
worksheet.merge_range('B1:D1', 'North Latitude', merge_format)   # 'Северная Широта'
worksheet.merge_range('E1:G1', 'East Longitude', merge_format)   # 'Восточная Долгота'
```



