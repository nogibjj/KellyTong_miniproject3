#this is for testing functions in main.py

from main import summary_pandas, summary_polars, age_pandas, age_polars, desrcibe_dataframe

def test_summary_pd():
    summary_pandas()

def test_summary_pl():
    summary_polars()
    
def test_age_pd():
    age_pandas()

def test_age_pl():
    age_polars()

def test_describe():
    "testing the desrcibe_dataframe function in main.py"
    describe = desrcibe_dataframe()
    assert describe['count'][0]== 5.0
    assert describe['mean'][0] == 175.0
    assert describe['min'][0] == 160.0
    assert describe['max'][0] == 190.0
