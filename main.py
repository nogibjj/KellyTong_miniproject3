import polars as pl
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def summary_pandas():
    df=pd.read_csv("gss2.csv")
    print(df.shape)
    print(df.describe())
  
def age_pandas():
    df=pd.read_csv("gss2.csv")
    plot = sns.histplot(df["age"], kde=True, color="blue", label="Age")
    plot.legend()
    plt.show()
  
def summary_polars():
    df = pl.read_csv("gss2.csv", infer_schema_length=10000)
    print(df.median())
    print(df.describe())
    
def age_polars():
    df = pl.read_csv("gss2.csv", infer_schema_length=10000)
    plot = sns.histplot(df["age"], kde=True, color="blue", label="Age")
    plot.legend()
    plt.show()
