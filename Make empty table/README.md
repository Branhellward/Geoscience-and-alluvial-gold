# Empty table

Here we make an empty table for a coordinates

Using a module for creating Excel XLSX files

[XlsxWriter](https://pypi.org/project/XlsxWriter/) - link to pypi.

---

After run we have a console question:

>Input number of rows:

Input 15 (example)

Then you have a Сoordinates.xlsx file with a full table you want:

![Your output table](img/Table_ex.png)

It can help you to save some time in future

------

If you need - you can replace English to Russian use comments in source

```python
worksheet.merge_range('A1:A2', '№№', merge_format)
worksheet.merge_range('B1:D1', 'North Latitude', merge_format)   # 'Северная Широта'
worksheet.merge_range('E1:G1', 'East Longitude', merge_format)   # 'Восточная Долгота'
```



