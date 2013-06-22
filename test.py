import nose.tools as n
from png2led import grid

def test_grid():
    'The mapping between LED number to pixel location should be correct.'
    n.assert_equal(grid()[26], ( 1, 23))
    n.assert_equal(grid()[0],  ( 0,  0))
    n.assert_equal(grid()[624],(24, 24))

