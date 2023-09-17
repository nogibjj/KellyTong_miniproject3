#this is for testing functions in main.py

from main import summary_pandas, summary_polars, age_pandas, age_polars

def test_summary_pd():
    summary_pandas()

def test_summary_pl():
    summary_polars()
    
def test_age_pd():
    age_pandas()

def test_age_pl():
    age_polars()
