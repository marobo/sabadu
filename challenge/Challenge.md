
# Challenge # 1
User input name, and then print them sort by name in list


```python
user = input('Enter names: ')
user = user.split(',')
user.sort()
print (user)
```

    Enter names: ony, one, an, as
    [' an', ' as', ' one', 'ony']


# Challenge # 2
Read CSV file and then ordered by list


```python
import csv
with open('names.csv') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(sorted(row))
```

    ['', 'Anders', 'Ano', 'Mario', 'Nando', 'Niko', 'Ony', 'Peter']


# Challenge # 3
Python read file CSV and then export to XLSX file


```python
import pandas 
import csv
data = pandas.read_csv('names.csv') 
data.to_excel('names.xlsx')
```

# Python connection data in XLSX an ordered by District and Dubdistrict using pandas


```python
import pandas 
data = pandas.read_excel('Places.xlsx') 
places = []
for row in data[1:].iterrows():
    places.append((row[1][0], row[1][1]))
    print (places)
    

data = pandas.read_excel('Places_well_formatted.xlsx')
data.sort_values(['District', 'Subdistrict'], inplace=True) # like calling data.sort()
# sorted_data = data.sort_values(['District', 'Subdistrict'], inplace=False) # like calling sorted(data)
print(data)
data.to_excel('Places_ordered.xlsx')
print (data)
```

    [('Ainaro', 'Ainaro')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa ')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren'), ('Baucau', 'Bauguia')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren'), ('Baucau', 'Bauguia'), ('Covalima', 'Zumalai')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren'), ('Baucau', 'Bauguia'), ('Covalima', 'Zumalai'), ('Baucau', 'Baucau Vila')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren'), ('Baucau', 'Bauguia'), ('Covalima', 'Zumalai'), ('Baucau', 'Baucau Vila'), ('Covalima', 'Tilomar')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren'), ('Baucau', 'Bauguia'), ('Covalima', 'Zumalai'), ('Baucau', 'Baucau Vila'), ('Covalima', 'Tilomar'), ('Baucau', 'Quelicai')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren'), ('Baucau', 'Bauguia'), ('Covalima', 'Zumalai'), ('Baucau', 'Baucau Vila'), ('Covalima', 'Tilomar'), ('Baucau', 'Quelicai'), ('Baucau', 'Vemasse')]
    [('Ainaro', 'Ainaro'), ('Aileiu', 'Remexio'), ('Manatuto', 'Laclo'), ('Aileiu', 'Laulara'), ('Ermera', 'Hatolia'), ('Liquica', 'Bazartete'), ('Liquica', 'Liquica'), ('Ermera', 'Lete Foho'), ('Ermera', 'Railaco'), ('Liquica', 'Maubara'), ('Manufahi', 'Same'), ('Manatuto', 'Barique'), ('Manatuto', 'Laclubar'), ('Manufahi', 'Alas'), ('Covalima', 'Fatumea'), ('Manatuto', 'Manatuto'), ('Covalima', 'Mau katar'), ('Manatuto', 'Soibada'), ('Manufahi', 'Fatuberliu'), ('Manufahi', 'Turiscal'), ('Covalima', 'Fatululik'), ('Ainaro', 'Hatu Udo'), ('Ainaro', 'Maubisse'), ('Ermera', 'Ermera Villa'), ('Covalima', 'Suai Villa '), ('Aileiu', 'Aileu Villa'), ('Aileiu', 'Liquidoe'), ('Ermera', 'Atsabe'), ('Ainaro', 'Hatu Builico'), ('Baucau', 'Laga'), ('Covalima', 'Fohoren'), ('Baucau', 'Bauguia'), ('Covalima', 'Zumalai'), ('Baucau', 'Baucau Vila'), ('Covalima', 'Tilomar'), ('Baucau', 'Quelicai'), ('Baucau', 'Vemasse'), ('Baucau', 'Venilale')]
        District   Subdistrict
    25    Aileiu   Aileu Villa
    3     Aileiu       Laulara
    26    Aileiu      Liquidoe
    1     Aileiu       Remexio
    0     Ainaro        Ainaro
    28    Ainaro  Hatu Builico
    21    Ainaro      Hatu Udo
    22    Ainaro      Maubisse
    33    Baucau   Baucau Vila
    31    Baucau       Bauguia
    29    Baucau          Laga
    35    Baucau      Quelicai
    36    Baucau       Vemasse
    37    Baucau      Venilale
    20  Covalima     Fatululik
    14  Covalima       Fatumea
    30  Covalima       Fohoren
    16  Covalima     Mau katar
    24  Covalima   Suai Villa 
    34  Covalima       Tilomar
    32  Covalima       Zumalai
    27    Ermera        Atsabe
    23    Ermera  Ermera Villa
    4     Ermera       Hatolia
    7     Ermera     Lete Foho
    8     Ermera       Railaco
    5    Liquica     Bazartete
    6    Liquica       Liquica
    9    Liquica       Maubara
    11  Manatuto       Barique
    2   Manatuto         Laclo
    12  Manatuto      Laclubar
    15  Manatuto      Manatuto
    17  Manatuto       Soibada
    13  Manufahi          Alas
    18  Manufahi    Fatuberliu
    10  Manufahi          Same
    19  Manufahi      Turiscal
        District   Subdistrict
    25    Aileiu   Aileu Villa
    3     Aileiu       Laulara
    26    Aileiu      Liquidoe
    1     Aileiu       Remexio
    0     Ainaro        Ainaro
    28    Ainaro  Hatu Builico
    21    Ainaro      Hatu Udo
    22    Ainaro      Maubisse
    33    Baucau   Baucau Vila
    31    Baucau       Bauguia
    29    Baucau          Laga
    35    Baucau      Quelicai
    36    Baucau       Vemasse
    37    Baucau      Venilale
    20  Covalima     Fatululik
    14  Covalima       Fatumea
    30  Covalima       Fohoren
    16  Covalima     Mau katar
    24  Covalima   Suai Villa 
    34  Covalima       Tilomar
    32  Covalima       Zumalai
    27    Ermera        Atsabe
    23    Ermera  Ermera Villa
    4     Ermera       Hatolia
    7     Ermera     Lete Foho
    8     Ermera       Railaco
    5    Liquica     Bazartete
    6    Liquica       Liquica
    9    Liquica       Maubara
    11  Manatuto       Barique
    2   Manatuto         Laclo
    12  Manatuto      Laclubar
    15  Manatuto      Manatuto
    17  Manatuto       Soibada
    13  Manufahi          Alas
    18  Manufahi    Fatuberliu
    10  Manufahi          Same
    19  Manufahi      Turiscal


# Python create CSV file


```python
import csv

with open('eggs.csv', 'w') as csvfile:
    rows = csv.reader(csvfile)
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam', 'Hello', 'World'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
```


```python
# Python connections database with posgresql
```


```python
import csv
import psycopg2

try:
    conn = psycopg2.connect("dbname='issues_db'")
except:
    print("I am unable to connect to the database.")
    
cur = conn.cursor()
try:
    cur.execute("""SELECT * from auth_user""")

except:
    print("I can't SELECT from auth_user")


with open('auth.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in cur.fetchall():
        spamwriter.writerow(row)

conn.close()
```


```python
conn = psycopg2.connect("dbname='issues_db'")
data = pandas.read_sql("""SELECT * from auth_user""", conn)
data.to_excel('names.xlsx')
conn.close() 
```
