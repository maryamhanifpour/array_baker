import pytest
import array_maker


path = ['/Users/maryam/Desktop/sample/sample_string.txt', '/Users/maryam/Desktop/sample/sample_string3.txt']

@pytest.mark.parametrize("path", path)
def test_bacth_size(path):
    sample = array_maker.sample_reader(path)
    sample_bacthes = array_maker.bake_batch(path)
    batch_size = [array_maker.process.get_size(s) for s in sample_bacthes]
    wrong_batch_size = len([bz for bz in batch_size if bz >5])
    assert wrong_batch_size==0
