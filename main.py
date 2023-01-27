import pandas as pd
import matplotlib.pyplot as plt

ms = pd.read_csv('microsoft.csv')
ms['MA10'] = ms['Close'].rolling(10).mean()
ms['MA60'] = ms['Close'].rolling(60).mean()
ms = ms.dropna()
ms['Share'] = [1 if ms.loc[i, 'MA10'] > ms.loc[i, 'MA60'] else 0 for i in ms.index]
ms['Close1'] = ms['Close'].shift(-1)
ms['Profit'] = [ms.loc[i, 'Close1'] - ms.loc[i, 'Close'] if ms.loc[i, 'Share'] > 0 else 0 for i in ms.index]
ms['Profit'].plot()
plt.axhline(y = 0, color = 'red')
ms['wealth'] = ms['Profit'].cumsum()
ms = ms.dropna()
print(ms.tail())