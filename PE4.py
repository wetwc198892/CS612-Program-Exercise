import numpy as np
import pandas as pd
np.random.seed(1234)
column = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
indexs = ['A', 'B', 'C', 'D', 'E', 'F']
data1 = pd.DataFrame(np.random.randint(49, size=(6, 8)), columns=column,index=indexs)
IQR = data1.quantile(0.75,axis=1)-data1.quantile(0.25,axis=1)
CV = data1.std(axis=1)/data1.mean(axis=1)
data1['IQR'] = IQR
data1['CV'] = CV
new_row = pd.Series(data= data1.mean(), name='mean')
data1 = data1.append(new_row, ignore_index=False)
print(data1)