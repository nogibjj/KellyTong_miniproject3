import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt

#def summary():
  #  df=pl.read_csv("gss.csv")
   # df.dropna()
   # print(df.median())
   # print(df.describe())
    
def age():
    df = pl.read_csv("gss2.csv", infer_schema_length=10000)
    print(df.median())
    print(df.describe())
    plot = sns.histplot(df["age"], kde=True, color="blue", label="Age")
    plot.legend()
    plt.show()
    
#def desrcibe_dataframe():
  #  data = {'height': [170,175,160,180,190]
 #   }
  #  dataframe = pl.DataFrame(data)
  #  return dataframe.describe()
