====================================================
array_maker: takes an array of strings and covert it to array of arrays
====================================================


-------------------
install the package:
-------------------

Create a virtual environment

$ python setup.py develop


-------------------
input and ouput format: 
-------------------

input: array of records

output: batches of input records in array format, arrays of input array

spec of output: 

1. each batch is of max size 5mb

2. each record in batch is of max size 1mb, larger should be discarded

3. each batch contains max 500 records



input = ['record1', 'record2', 'record3', ...]

output = [['record1', 'record2'], ['record3'], ['record4',... 'record{n}']]


if sample.txt contains ['a','b']

$ batch --path ${path to sample text}