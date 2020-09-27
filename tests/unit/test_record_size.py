import pytest
import itertools
import array_maker


path = ['/Users/maryam/Desktop/sample/sample_string.txt', '/Users/maryam/Desktop/sample/sample_string3.txt']

@pytest.mark.parametrize("path", path)
def test_record_size(path):
    sample = array_maker.sample_reader(path)
    sample_bacthes = array_maker.bake_batch(path)
    records = list(itertools.chain(*sample_bacthes))
    record_size = [array_maker.process.get_size(r) for r in records]
    wrong_record_size = len([rz for rz in record_size if rz > 1])
    assert wrong_record_size==0
