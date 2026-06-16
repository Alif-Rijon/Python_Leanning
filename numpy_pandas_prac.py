import numpy as np
numbers = np.array([1,2,34])
print(type(numbers))
print(numbers)

#2D array
arr = np.array([[1,2,3],
               [44,5,22]
               ])
print(arr) #array print
print(arr.shape) #row x column
print(arr.ndim) #array dimension

#Basic operation 

#vectorized operation
a= np.array([1,2,3])
print(a+5)
print(a*2)

#statistical operations
import numpy as np

data=np.array([10,20,30,40,50])
print(np.mean(data))
print(np.max(data))
print(np.min(data))
print(np.std(data))
print(np.sum(data))

#Pandas

#Series

import pandas as pd
s = pd.Series([10,30,20])
print(s)

#DataFrame

data = {
    "Name": ["rijon","alif"],
    "marks":[90,80]
}
df = pd.DataFrame(data)
print(df)

#read csv file
import pandas as pd 

df = pd.read_csv("student-data.csv")
print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df["school"])
print(df[["school","sex","age"]])
print("Age above 20")
print(df[df["age"] > 18])
print(df[(df["age"]>18) & (df["age"]<20)])
print(df.isnull().sum())
#print(df.dropna())
print(df.fillna(5))

#statistical
print(df["age"].mean())
print(df["age"].max())
print(df["age"].min())
print(df.describe())

df.to_csv(
    "cleaned_data.csv",
    index=False
)