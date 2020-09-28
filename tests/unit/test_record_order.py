import pytest
import itertools
import array_maker


path = ['/Users/maryam/Desktop/sample/sample_string.txt', '/Users/maryam/Desktop/sample/sample_string3.txt']



@pytest.mark.parametrize("path", path)
def test_record_order(path):
    sample = array_maker.sample_reader(path)
    sample_bacthes = array_maker.bake_batch(path)
    records = list(itertools.chain(*sample_bacthes))
    filtered = array_maker.process.size_filter(sample)
    assert filtered == records


