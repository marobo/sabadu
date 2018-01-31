

```python
def find_rotation(test_string, k):
    # take k characters from the front of test string, append them to test_string, and return the result
    first_k_characters = test_string[0:k]
    string_without_first_k_characters = test_string[k:]
    return string_without_first_k_characters + first_k_characters

find_rotation('hello', 2)
```



```python
def is_palindrome(string):
    # return true if the string is a palindrome, and false if not
    # true if the string is the same left to right, as it is right to left
    return string == string[::-1]

print(is_palindrome("hello"))
print(is_palindrome("anna"))
```



```python
def all_possible_substrings(string):
    # return a list of all possible substrings of our string
    # 'hello' -> 'h', 'he', 'hel', 'hell', 'hello', 
    #             'e', 'el', 'ell', 'ello'
    #             'l', 'll', 'llo'
    #              'l', 'lo'
    #              'o'
    for start_index in range(0, len(string)):
        for end_index in range(start_index + 1, len(string) + 1):
            print(string[start_index:end_index])
        

all_possible_substrings('mariano')
```



