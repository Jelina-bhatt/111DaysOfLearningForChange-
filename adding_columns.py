import pandas as pd
data ={
    "Name":['rubina','amit', 'saroj','bhawana','bindu','apekshya','binod','ashika'],
    "Age":[30,25,40,60,28,50,33,22],
    "Salary":[50000, 20000,30000,70000,100000,60000,400000,45000],
    "Performance score":[79,80,45,34,56,32,88,76]
}

df=pd.DataFrame(data)
print(df)

#square bracket[] df["column_name"]=data

df["bonus"] = df["Salary"] * 0.1
print(df)

#using insert()
#df.insert(loc, "column name", somedata)
df.insert(0, "employee Id", [10,20,30,40,50,60,70,80] )
print(df)