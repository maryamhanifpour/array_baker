import pytest
import itertools
import array_maker


path = ['/Users/maryam/Desktop/sample/sample_string.txt', '/Users/maryam/Desktop/sample/sample_string3.txt']

@pytest.mark.parametrize("path", path)
def test_record_intact(path):
    sample = array_maker.sample_reader(path)
    sample_bacthes = array_maker.bake_batch(path)
    records = list(itertools.chain(*sample_bacthes))
    distorted_records = len([r for r in records if r not in sample])
    assert distorted_records==0



@pytest.mark.parametrize("path", path)
def test_record_number_intactxY(path):
    sample = array_maker.sample_reader(path)
    sample_bacthes = array_maker.bake_batch(path)
    records = list(itertools.chain(*sample_bacthes))
    filtered = array_maker.process.size_filter(sample)
    assert len(filtered) == len(records)


