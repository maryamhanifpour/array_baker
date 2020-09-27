import os
import sys
import logging
from array_maker.process import read_sample, size_filter,batch_indexes, batch_maker




def sample_reader(path):
    try:
        sample = read_sample(path)
    except IOError:
        logging.error('make sure full path plus file name is provided and the file exists in the path')
        return()
    return(sample)



def bake_batch(path):
    sample = sample_reader(path)
    if not sample:
        return()
    filtered = size_filter(sample)
    index_list = batch_indexes(filtered)
    batches = batch_maker(filtered, index_list)
    return(batches)
























