import sys
import pytest
import itertools
sys.path.append('../../src')
from array_maker.main import sample_reader, bake_batch
from array_maker.modules.process import get_size, size_filter
path = ['/Users/maryam/Desktop/sample/sample_string.txt', '/Users/maryam/Desktop/sample/sample_string3.txt']


@pytest.mark.parametrize("path", path)
def test_record_intact(path):
    sample = sample_reader(path)
    sample_bacthes = bake_batch(sample, batch_size_limit=5, number_records_limit=500)
    records = list(itertools.chain(*sample_bacthes))
    distorted_records = len([r for r in records if r not in sample])
    assert distorted_records==0



@pytest.mark.parametrize("path", path)
def test_record_number_intact(path):
    sample = sample_reader(path)
    sample_bacthes = bake_batch(sample, batch_size_limit=5, number_records_limit=500)
    records = list(itertools.chain(*sample_bacthes))
    filtered = size_filter(sample)
    assert len(filtered) == len(records)


