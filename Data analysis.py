import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import seaborn as se
df=pd.read_csv("/Users/siribasani/Downloads/StudentsPerformance.csv")
print(df.head)
a=df.groupby("parental level of education")["math score"].mean().reset_index()
print("Avg marks:\n",a)
se.barplot(x="parental level of education",y="math score",data=a)
plt.title("Student data")
plt.xlabel("parental level of education")
plt.ylabel("math score")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
for i, r in df.iterrows():
    print(f"Student math score is {r['math score']}")