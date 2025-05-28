from src.math_operations import add, subtract
def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(10, 5) == 5
def test_subtract_negative():
    """Test the subtract function with negative numbers."""
    assert subtract(-5, -3) == -2
    assert subtract(-3, -5) == 2
    assert subtract(-10, -10) == 0
    assert subtract(0, -5) == 5
    assert subtract(-5, 0) == -5
def test_subtract_zero():
    """Test the subtract function with zero."""
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5
    assert subtract(0, -10) == 10
    assert subtract(-10, 0) == -10
    assert subtract(0, 0) == 0
def test_add_negative():
    """Test the add function with negative numbers."""
    assert add(-5, -3) == -8
    assert add(-3, -5) == -8
    assert add(-10, -10) == -20
    assert add(0, -5) == -5
    assert add(-5, 0) == -5
def test_add_zero():
    """Test the add function with zero."""
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, -10) == -10
    assert add(-10, 0) == -10
    assert add(0, 0) == 0