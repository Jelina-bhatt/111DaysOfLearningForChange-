import pandas as pd

data ={
    "Name":['Ram', 'Shyam', 'hari', 'shiva'],
    "Age":[10,20,30,40],
    "city":['ayodhya', 'goloka', 'vrindaban','kailash']
}
df= pd.DataFrame(data)



print("displaying the info of the data set")
print(df.info())
