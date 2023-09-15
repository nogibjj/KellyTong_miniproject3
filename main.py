import matplotlib.pyplot as plt
import seaborn as sns
import polars as pl

#def summary():
  #  df=pl.read_csv("gss.csv")
   # df.dropna()
   # print(df.median())
   # print(df.describe())
    
def age():
    df=pl.read_csv("gss.csv")
    ignore_errors=TRUE
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
