import pandas as pd
import numpy as np
df = pd.DataFrame({'Name': ['Ravi', 'Veena', 'Meena', 'Rupali'], 'subject': [92, 97, 85, 74]})
q75, q25 = np.percentile(df['subject'], [75, 25])
iqr = q75 - q25
print(iqr)
