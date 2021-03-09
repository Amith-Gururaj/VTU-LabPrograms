import pandas as pd
df=pd.read_csv("lab2.csv")
spe_df=df.loc[df["enjoy sport"].str.upper()=="YES"]
gene_df=df.loc[df["enjoy sport"].str.upper()=="NO"]
spe_df=spe_df.iloc[:,:-1]
gene_df=gene_df.iloc[:,:-1]
base=spe_df.iloc[0]
for x in range (1,len(spe_df)):
    base=base.where(spe_df.iloc[x]==base,other="???")
print("Specific:-\n",base.values)
for x in range (len(gene_df)):
    base=base.where(base!=gene_df.iloc[x],other="???")
print("general")
for i,x in enumerate(base):
    if x!="???":
        l=["???"]*len(base)
        l[i] =x
        print(l)
​