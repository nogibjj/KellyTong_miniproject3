import matplotlib.pyplot as plt
import seaborn as sns
import polars as pl

def age():
    df=pl.read_csv("gss.csv")
    print(df.shape)
    print(df.describe())
    plot = sns.histplot(df["age"], kde=True, color="blue", label="Age")
    plot.legend()
    plt.show()
    
def desrcibe_dataframe():
    data = {'height': [170,175,160,180,190]
    }
    dataframe = pd.DataFrame(data)
    return dataframe.describe()
