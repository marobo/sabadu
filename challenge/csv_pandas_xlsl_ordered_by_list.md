
# Challenge # 1
User input name, and then print them sort by name in list


```python
user = input('Enter names: ')
user = user.split(',')
user.sort()
print (user)
```


# Challenge # 2
Read CSV file and then ordered by list


```python
import csv
with open('names.csv') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(sorted(row))
```

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

# Python connections database with posgresql


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
