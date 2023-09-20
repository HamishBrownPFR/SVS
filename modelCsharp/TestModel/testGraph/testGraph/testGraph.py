import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

data = pd.read_csv(r"C:\Users\1989s\source\repos\svs\modelCsharp\TestModel\testGraph\OutputFiles\test 1.csv",index_col=0)
observed_data = pd.read_csv(r"C:\Users\1989s\source\repos\svs\modelCsharp\TestModel\testGraph\OutputFiles\observed.csv",index_col=0)

observed_data.sort_index(axis=0,inplace=True)

tests = ['test 1','test 2','test 3']

Alltests =[]
for t in tests[:]:
    Alltests.append(pd.read_csv(r"C:/Users/1989s/source/repos/svs/modelCsharp/TestModel/testGraph/OutputFiles/"+t+".csv",index_col=0))
    
AllData = pd.concat(Alltests,axis=1,keys=tests)
AllData.index = pd.to_datetime(AllData.index,format = "%d/%m/%Y %H:%M:%S %p")

observed_data.index=pd.to_datetime(observed_data.index,format="%d/%m/%Y %H:%M")

observed_test = observed_data.columns.get_level_values(0).drop_duplicates()
AllData.sort_index(axis=0,inplace=True)

AllData.index = pd.to_datetime(AllData.index)

tests = AllData.columns.get_level_values(0).drop_duplicates()
colors = pd.Series(['r','b','g'])

start = dt.datetime.date(AllData['test 1'].dropna().index.min())
end = dt.datetime.date(AllData['test 1'].dropna().index.max())

def makeplot(Data,color):
    plt.plot(Data,color=color)
    
def make_observed(observed):
    plt.plot(observed.index,observed.loc[:,'Nitrogen'],'*',color='g')     
        
Graph = plt.figure(figsize=(10,10))
pos = 1
for t in tests:
    start = dt.datetime.date(AllData[t].dropna().index.min())
    end = dt.datetime.date(AllData[t].dropna().index.max())
    datefilter = []
    for d in observed_data.index:
        ret = False
        if ((d >= pd.Timestamp(start)) and (d<=pd.Timestamp(end))):
            ret = True
        datefilter.append(ret)
        
    color = colors[pos-1]
    Graph.add_subplot(2,2,pos)
    Data = AllData.loc[:,(t,'SoilMineralN')].sort_index()
    plt.xticks(rotation = 45)
    makeplot(Data,color)
    make_observed(observed_data[datefilter])
    pos+=1

plt.show()