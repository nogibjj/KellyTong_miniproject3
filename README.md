# IDS 706 Mini Project 3

This repository is for IDS706 mini project week 3. 



## Purpose 
    This repository is created from the template established in week 1. 
    It is set up based on the template's environment. This repository incorporates "pandas" to develop statistical 
    functions. Specifically, the author uses pd.dataframe() to set up a dataset. 
    Then it is tested on the count, mean, max, and min. Moreover, the author loads the dataset gss.csv. Summary of
    the dataset and a histogram is developed to visualized the densty of the "age" variable in the dataset.

## Important Things included are:
    * Makefile
    * Dockerfile
    * Main
    * test_main
    * README
    * requiremets
    * gss.csv (the dataset)
    * output.pdf (showing the output)

[![CI](https://github.com/nogibjj/KellyTong_miniproject2/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/KellyTong_miniproject2/actions/workflows/CI.yml)

## The Building Process

`make install`

The building process starts with installing the packages. 
**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt

`make link`

**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="457" alt="make lint" src="https://github.com/Kelly0604/miniproject2/assets/142815940/39a19764-a6cc-4eaa-977f-7433b8915dad">

`make test`

**Make test** calls the command python -m pytest -vv --cov=main test_*.py
<img width="609" alt="Make Test" src="https://github.com/nogibjj/KellyTong_miniproject2/assets/142815940/1d5eb1de-c0f7-4459-97bb-cae51ea621aa">


`make format`

**Make format** calls the command black *.py


<img width="299" alt="make format" src="https://github.com/Kelly0604/miniproject2/assets/142815940/41df08ca-d8f7-4b62-b88b-1f39f1a7d858">

## Visualization
### A Density Graph on Age
<img width="614" alt="截屏2023-09-13 16 21 26" src="https://github.com/nogibjj/KellyTong_miniproject2/assets/142815940/bf314b8b-19ec-461a-9faa-f532fb254102">

## Conclusion
The dataset includes mostly age group from 25 to 35. The mean age is approximately 46. 
(Please find more detailed steps in the output.pdf)

