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
    plt.savefig("plot_age_pandas.png")
  
def summary_polars():
    df = pl.read_csv("gss2.csv", infer_schema_length=10000)
    print(df.median())
    print(df.describe())
    
def age_polars():
    df = pl.read_csv("gss2.csv", infer_schema_length=10000)
    plot = sns.histplot(df["age"], kde=True, color="blue", label="Age")
    plot.legend()
    plt.show()
    plt.savefig("plot_age_polars.png")

def generate_general_markdown():
    """generate an md file with outputs"""
    markdown_table1 = summary_pandas()
    markdown_table1 = str(markdown_table1)
    markdown_table2 = summary_polars()
    markdown_table2 = str(markdown_table2)

    # Write the markdown table to a file
    with open("output.md", "w", encoding="utf-8") as file:
        file.write("Describe_pandas:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("Describe_polars:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line
        file.write("![age](plot_age_pandas.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![age](plot_age_polars.png)\n")
