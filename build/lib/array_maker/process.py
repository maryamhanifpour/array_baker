import sys


def read_sample(path):
    with open(path) as f:
        sample = f.read()
    if isinstance(sample, list):
        return(sample)
    if isinstance(sample, str):
        return(eval(sample))


def get_size(object):
    if isinstance(object, str):
        size_mb = sys.getsizeof(object)/1e6
    elif isinstance(object, list):
        result = list(map(sys.getsizeof, object))
        size_mb = sum([res/1e6 for res in result])
    return(size_mb)


def size_filter(sample_list):
    filtered_list = [s for s in sample_list if get_size(s) <=1]
    return(filtered_list)



def batch_elements(list_object, index_start):
    for n in range(index_start, index_start + 500):
        if get_size(list_object[index_start:n]) > 5:
            return(n)
        else:
            pass
    return(n)



def batch_indexes(filtered):
    index_start = 0
    index_list = []
    while index_start < len(filtered):
        index_end = batch_elements(filtered, index_start)
        if index_end < len(filtered):
            index_list.append((index_start, index_end-1))
        else:
            index_list.append((index_start, len(filtered)))
        index_start = index_end
    return(index_list)



def batch_maker(filtered, index_list):
    batches = [filtered[indx[0]:indx[1]] for indx in index_list]
    return(batches)


def encode_64(element):
    element_bytes = element.encode('ascii')
    element_base64_bytes = base64.b64encode(element_bytes)
    return(element_base64_bytes)


def encode_list(filtered):
    encoded = [encode_64(s) for s in filtered]
    return(encoded)

