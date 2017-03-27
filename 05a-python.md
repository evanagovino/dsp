# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are lists of values. Tuples are immutable while lists are mutable, meaning that you can redefine the values in lists while you can't redefine the values in tuples. Only tuples can work as keys in dictionaries, not lists. This is because tuples are immutable. If you are using a list as a key in the dictionary and then change it, it can come up with an error. Because you can't change the value of a tuple, this issue won't happen if it's a key in a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are an unordered collection of unique elements, while lists are an ordered collection of elements. I usually use sets when I want the list of unique values in a list. Lists have worse performance than sets because they are ordered.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a way of executing a function without defining a function by name.  
>> objects = [('test1', 'A', 10), ('test2', 'B', 5), ('test3', 'C', 15)]  
>> A function example: sorted(objects, key=lambda object: object[2])


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way to construct lists via mathematical functions, such as printing the multiples or exponents of a number.  
>> An example:   
>>S = [2** i for i in range(5)]  
>>def exponent(y):  
>>    return(2**y)  
>>Map Function:  
>>list(map(exponent, range(5)))  
>>Filter Function:
>>def exponent2(y):  
>>	l = []  
>>	i = 0  
>>	while i < 5:  
>>		x = 2** i  
>>		l.append(x)  
>>		i = i + 1  
>>	if y in l:  
>>		return True  
>>	else:  
>>		return False  
>>list(filter(exponent2, range(5)))  


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





