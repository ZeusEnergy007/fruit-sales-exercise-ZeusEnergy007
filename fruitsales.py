# add your code here
import pandas as pd

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])
# fruit_sales

fruit_sales.to_csv("fruit.csv")
