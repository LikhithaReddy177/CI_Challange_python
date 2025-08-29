import pandas as pd


PANDAS_VERSION = "2.3.1,1.3.5"


def test_pandas_version():
    ''' Use an assertion to check the output of pd.__version__ '''
    assert pd.__version__ in [PANDAS_VERSION]


if __name__ == "__main__":
    test_pandas_version()
    print("Pandas version is correct!")
