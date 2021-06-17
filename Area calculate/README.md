# Area calculate

Here we make an area calculate table 

Using a module for creating Excel XLSX files

[XlsxWriter](https://pypi.org/project/XlsxWriter/) - link to pypi.

Sources:

* [Gauss's area formula](https://en.wikipedia.org/wiki/Shoelace_formula) - link to Wikipedia page

* The requirements of the expertise on making the table of mining allotment (MA), also the calculation of the area of mining allotment attached to the Draft Mining Allotment (DMA).

  Требования экспертизы по составлению таблицы Горного Отвода (ГО), а так же расчет площади горного отвода прикладываемый к Проекту Горного Отвода (ПГО).

---





------

If you need - you can replace English to Russian use comments in source

```python
worksheet.merge_range('A1:A2', '№№', merge_format)
worksheet.merge_range('B1:D1', 'North Latitude', merge_format)   # 'Северная Широта'
worksheet.merge_range('E1:G1', 'East Longitude', merge_format)   # 'Восточная Долгота'
```



