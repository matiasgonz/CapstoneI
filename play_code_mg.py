import pandas as pd

df = pd.read_csv('Data/US_Temps_final.csv', low_memory=False)
#pd.set_option("display.max_rows", None, "display.max_columns", None)

print(df.head())


