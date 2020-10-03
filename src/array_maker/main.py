import os
import sys
import logging
import argparse
from array_maker.modules.process import read_sample, size_filter, Batch

logging.basicConfig(level=logging.INFO)


def sample_reader(path):
    try:
        sample = read_sample(path)
        logging.info('initial list length:{} '.format(len(sample)))
    except IOError:
        logging.error('make sure full path plus file name is provided and the file exists in the path')
        return()
    return(sample)



def bake_batch(sample, batch_size_limit, number_records_limit):
    filtered = size_filter(sample)
    b = Batch(filtered, batch_size_limit, number_records_limit)
    batches = b.batch_records()
    return(batches)

def batch():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, type=str)
    parser.add_argument('--batch_size_limit', required=False, type=int)
    parser.add_argument('--number_records_limit', required=False, type=int)
    args = parser.parse_args()
    path = args.path
    batch_size_limit = args.batch_size_limit
    number_records_limit = args.number_records_limit

    sample = sample_reader(path)
    batches = bake_batch(sample, batch_size_limit or 5, number_records_limit or 500)
    logging.info('final batch length:{} '.format(len(batches)))


if __name__ == '__main__':
    batch()
























