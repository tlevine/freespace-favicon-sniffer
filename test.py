import nose.tools as n
from png2led import grid, _grid_column

def test_grid_column():
    'The mapping between LED number within column should be correct.'
    n.assert_list_equal(_grid_column(3), [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75])

def test_grid():
    'The mapping between LED number to pixel location should be correct.'
    n.assert_equal(grid()[0],  ( 0,  0))
    n.assert_equal(grid()[624],(24, 24))
    n.assert_equal(grid()[26], ( 1, 23))

def test_grid_type():
    n.assert_is_instance(grid(), list)
