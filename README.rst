====================================================
array_maker: takes an array and covert it to arrays of arrays
====================================================


input: array of records

output: batches of input records in array format, arrays of input array

spec of output: each batch is of max size 5mb, each record in batch is of max size 1mb, larger should be discarded, each contains max 500 records



input = [record1, record2, record3, ...]

output = [[record1, record2], [record3], [record4,... record{n}]]


if sample.txt contains ['a','b']

>>> import array_maker

>>> array_maker.bake_batch('/Users/maryam/Desktop/dist/sample.txt')
[['a', 'b']]

maryammore test samples located in /samples
