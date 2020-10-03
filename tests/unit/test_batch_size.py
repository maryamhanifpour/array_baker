import sys
import pytest

sys.path.append('../../src')
from array_maker.main import sample_reader, bake_batch
from array_maker.modules.process import get_size
path = ['/Users/maryam/Desktop/sample/sample_string.txt']

@pytest.mark.parametrize("path", path)
def test_bacth_size(path):
    sample = sample_reader(path)
    sample_bacthes = bake_batch(sample, batch_size_limit=5, number_records_limit=500)
    batch_size = [get_size(s) for s in sample_bacthes]
    wrong_batch_size = len([bz for bz in batch_size if bz >5])
    assert wrong_batch_size==0
