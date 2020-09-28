====================================================
array_maker: takes an array of strings and covert it to array of arrays
====================================================

Create a virtual environment

>>> python setup.py sdist bdist_wheel

$pip install dist/array_maker-0.0.1.tar.gz


# input and ouput format

input: array of records

output: batches of input records in array format, arrays of input array

spec of output: 

1. each batch is of max size 5mb

2. each record in batch is of max size 1mb, larger should be discarded

3. each batch contains max 500 records



input = ['record1', 'record2', 'record3', ...]

output = [['record1', 'record2'], ['record3'], ['record4',... 'record{n}']]


if sample.txt contains ['a','b']

>>> import array_maker

>>> array_maker.bake_batch('${path_to_sample}/sample.txt')
[['a', 'b']]

more test samples located in /samples

>>> import array_maker
>>> path = '${path_to_sample}/sample.txt'
>>> sample = array_maker.sample_reader(path)
>>> sample_bacthes = array_maker.bake_batch(path)

>>> len(sample)
100
>>> len(sample_bacthes)
9



To test final batch meet the specs, provide the path of samples to be tested in test files in tests/unit/ by updating the path list

and run pytest

$pytest -v

platform darwin -- Python 3.7.1, pytest-6.0.2, py-1.9.0, pluggy-0.13.1

collected 10 items                                                                                                                                                                  

|tests/unit/test_batch_size.py ..                           [ 20%]

|tests/unit/test_record_intact.py ....                      [ 60%]

|tests/unit/test_record_order.py ..                         [ 80%]

|tests/unit/test_record_size.py ..                          [100%]

================ 10 passed in 15.42s ================

