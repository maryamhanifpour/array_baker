import sys


def read_sample(path):
    with open(path) as f:
        sample = f.read()
    if isinstance(sample, list):
        return(sample)
    if isinstance(sample, str):
        return(eval(sample))


# calcuate size of object in mb if object is of string type, if the object is list of strings,
# sums over size of strings in the list
def get_size(object):
    if isinstance(object, str):
        size_mb = sys.getsizeof(object)/1e6
    elif isinstance(object, list):
        result = list(map(sys.getsizeof, object))
        size_mb = sum([res/1e6 for res in result])
    return(size_mb)


# records bigger than 1mb are discarded
def size_filter(sample_list):
    filtered_list = [s for s in sample_list if get_size(s) <=1]
    return(filtered_list)


# starts form index_start, batches up to 500 records in one list unless the 5mb thershold is reached, returns last index
def batch_elements(list_object, index_start):
    for n in range(index_start, index_start + 500):
        if get_size(list_object[index_start:n]) > 5:
            return(n)
        else:
            pass
    return(n)


# returns [(index_start1, index_end2), (index_start3, index_end4)] by mapping batch_elements function to a list of strings
def batch_indexes(filtered):
    index_start = 0
    index_end = 0
    index_list = []
    while index_end <= len(filtered):
        index_end = batch_elements(filtered, index_start)
        if index_end <= len(filtered):
            index_list.append((index_start, index_end-1))
        else:
            index_list.append((index_start, len(filtered)))
        index_start = index_end - 1
    return(index_list)


# returns batches of array of strings using index_list from batch_indexes function
def batch_maker(filtered, index_list):
    batches = [filtered[indx[0]:indx[1]] for indx in index_list]
    return(batches)



class Batch:
    def __init__(self, list_object, batch_size_limit, number_records_limit):
        self.size = 0
        self.batch = []
        self.large_batch = []
        self.batch_size_limit = batch_size_limit
        self.number_records_limit = number_records_limit
        self.iter_object = iter(list_object)
    def batch_records(self):
        size = self.size
        batch = self.batch
        large_batch = self.large_batch
        iter_object = self.iter_object
        batch_size_limit = self.batch_size_limit
        number_records_limit = self.number_records_limit
        while True:
            try:
                item = next(iter_object)
                print(item)
                size = size + get_size(item)
                if size <= batch_size_limit or len(batch) > number_records_limit:
                    batch.append(item)
                else:
                    large_batch.append(batch)
                    batch = [item]
            except StopIteration:
                break
        large_batch.append(batch)
        return(large_batch)
