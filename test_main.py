#this is for testing functions in main.py

from main import desrcibe_dataframe, summary, age

def test_summary():
    summary()
    
def test_age():
   age()

def test_describe():
   # "testing the desrcibe_dataframe function in main.py"
    describe = desrcibe_dataframe()
    assert describe.loc['count'][0]== 5.0
    assert describe.loc['mean'][0] == 175.0
    assert describe.loc['min'][0] == 160.0
    assert describe.loc['max'][0] == 190.0
