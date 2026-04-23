import pandas as pd
data ={
    "Name":['rubina','amit', 'saroj','bhawana','bindu','apekshya','binod','ashika'],
    "Age":[30,25,40,60,28,50,33,22],
    "Salary":[50000, 20000,30000,70000,100000,60000,400000,45000],
    "Performance score":[79,80,45,34,56,92,88,76]
}

df=pd.DataFrame(data)
print(df)

#filtering with salary>50000
high_salary = df[df['Salary']>50000]
print('Employees with salary>50000')
print(high_salary)

#filtering with age>30 & salary>50000
combine = df[(df['Salary']>50000) & (df['Age']>30)]
print('Employees with salary>50000 & Age>50')
print(combine)

print("employees having or condition")
filtered_or = df[(df['Age']>35) | (df["Performance score"]>90)]
print(filtered_or)