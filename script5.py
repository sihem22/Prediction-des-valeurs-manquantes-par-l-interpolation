import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt




df = pd.read_csv('iris.RVms_pandas.csv', sep = ' ')
print(df)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter([x[1] for x in df.itertuples()], [y[2]for y in df.itertuples()], [z[3] for z in df.itertuples()], c=[w[4] for w in df.itertuples()], cmap=plt.hot())
fig.colorbar(img)
plt.show()

out = df.interpolate(method='polynomial', order=5 )
print(out)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
img1 = ax1.scatter([x[1] for x in out.itertuples()], [y[2]for y in out.itertuples()], [z[3] for z in out.itertuples()], c=[w[4] for w in out.itertuples()], cmap=plt.hot())
fig1.colorbar(img1)
plt.show()
out.to_csv('myFile.csv', index=False,sep = ' ', na_rep="NaN")

