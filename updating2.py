import pandas as pd
data ={
    "Name":['rubina','amit', 'saroj','bhawana','bindu','apekshya','binod','ashika'],
    "Age":[30,25,40,60,28,50,33,22],
    "Salary":[50000, 20000,30000,70000,100000,60000,400000,45000],
    "Performance score":[79,80,45,34,56,32,88,76]
}

df=pd.DataFrame(data)
print(df)

#increasing by 5%

df["Salary"]=df['Salary']*1.05
print(df)