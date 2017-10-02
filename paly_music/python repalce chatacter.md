
# Modified string with index replaced with char
Example:
    Modofied string "coffee" return to "cotfee"


```python
def replace_char(my_string, my_index, my_char):
    # returns modified string with index replaced with char
    
    print(my_string[:my_index])
    print(my_string[:my_index] + my_char)
    print(my_string[my_index + 1:])
    print(my_string[:my_index] + my_char + my_string[my_index + 1:])
    
replace_char('coffee', 2, 't')  # returns 'cotfee'

```

    co
    cot
    fee
    cotfee


## Why show up the result like this?
