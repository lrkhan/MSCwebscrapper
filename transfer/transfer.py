from numpy import ediff1d
import pandas as pd
from time import sleep, time

from pandas.core.indexing import is_label_like

allTools = pd.read_csv('tools.csv')
outputto = pd.read_csv('output.csv',index_col=0)

begin=time()

#outputto.drop(outputto.columns[0])
print(outputto)

for i in range(len(outputto.index)-1):
    start = time()

    for j in range(len(allTools.index)-1):
        if str(outputto.iloc[i,0]) == str(allTools.iloc[j,0]):
            end = time()
            
            allTools.iloc[j,1] = outputto.iloc[i,1]
            allTools.iloc[j,2] = outputto.iloc[i,2]
            allTools.iloc[j,3] = outputto.iloc[i,3]
            allTools.iloc[j,4] = outputto.iloc[i,4]
            allTools.iloc[j,5] = outputto.iloc[i,5]
            allTools.iloc[j,6] = outputto.iloc[i,6]
            allTools.iloc[j,7] = outputto.iloc[i,7]
            allTools.iloc[j,8] = outputto.iloc[i,8]

            print('Found '+ outputto.iloc[i,0] + ' and updated item. Found in ' + str(end-start) + "s.")
            
            break

fin = time()
print("Completed in " + str(fin-begin) + "s.")

allTools.to_csv(r'C:\Users\lkhan\Documents\Webscraper\MSC Tools\transfer\compiled.csv', index=False)
