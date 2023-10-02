import pandas as pd
import numpy as np

data = np.array([[2, 3], [3, 5], [9, 2]])

df = pd.DataFrame(data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2'])
print(df)
