import pandas as pd
import numpy as np

data = pd.read_csv("FuelConsumption.csv")

print(type(data))
print(data.head()) 
print(data.tail())
print(data)
 
print(data.shape)
print(data.columns)
print(data.dtypes)
print(data.info())

print(data['FUELCONSUMPTION_COMB_MPG'] [0:5])
print(data[['FUELCONSUMPTION_COMB_MPG','ENGINESIZE']] [10:25])

print(data['FUELCONSUMPTION_COMB_MPG'].value_counts()) 
print(data['FUELCONSUMPTION_COMB_MPG'].value_counts(normalize=True)*100)

print(pd.crosstab(data.MODELYEAR , data.MODEL)) 

print(pd.crosstab(data.MODELYEAR , data.MODEL, normalize= "index"))
print()
print(pd.crosstab(data.MODELYEAR , data.MODEL , normalize= "columns"))


below_3 = data[ data.FUELCONSUMPTION_COMB_MPG <= 27] 
print(below_3)

below_3 = data[ data.FUELCONSUMPTION_COMB_MPG <= 27] [['MODELYEAR' , 'MODEL']]
print(below_3)

print(data[data.MAKE.str.contains("BMW")]) 


print(data.MAKE.unique()) 


#git Hub = QueenAhllam
#visit my page on GIT-HUB i have many projects if you need 
