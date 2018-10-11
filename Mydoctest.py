import subprocess

def test(n):
    """
    This is the "example" module.
    The example module supplies one function, factorial().  For example,
    >>> test(3)
    9
    >>> test(5)
    25
    """
    n = n * n
    return n  
    
# We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()