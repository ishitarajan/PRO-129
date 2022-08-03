import pandas as pd 
# merging two csv files 
df = pd.concat(map(pd.read_csv, ['MOVIE_RATING.csv', 'scrapper3.csv']), ignore_index=True) 
print(df) 
df.to_csv('file1.csv')