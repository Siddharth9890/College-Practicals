from scipy.spatial.distance import cityblock
import pandas as pd

# define DataFrame
df = pd.DataFrame({'A': [2, 4, 4, 6],
                   'B': [5, 5, 7, 8],
                   'C': [9, 12, 12, 13]})

# calculate Manhattan distance between columns A and B
print(cityblock(df.A, df.B))
