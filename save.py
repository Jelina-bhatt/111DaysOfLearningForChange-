import pandas as pd

data ={
    "Name":['Ram', 'Shyam', 'hari', 'shiva'],
    "Age":[10,20,30,40],
    "city":['ayodhya', 'goloka', 'vrindaban','kailash']
}
df= pd.DataFrame(data)
print(df)

#To save csv file
#df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)