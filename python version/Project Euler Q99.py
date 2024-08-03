# Project Euler Question 99
# Comparing two numbers written in index form like 2^(11) and 3^(7) is not difficult, as any calculator would confirm
# that 2^11 = 2048 < 3^7 = 2187.
# However, confirming that 632382^(518061) > 519432^(525806) would be much more difficult, as both numbers contain over
# three million digits.
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
# base/exponent pair on each line, determine which line number has the greatest numerical value.
import pandas as pd  # Get pandas for data frame and numpy for log
import numpy as np

data1 = pd.read_table("Project Euler Q99 Base Exp.txt",names=["Input","Base","Exponent","Result"])

df1 = pd.DataFrame(data1)

for i in range(1000):
    switch = df1.at[i,"Input"].find(",")
    base = df1.at[i,"Input"][:switch]
    exponent = df1.at[i,"Input"][switch+1:]
    df1.at[i,"Base"] = base
    df1.at[i,"Exponent"] = exponent
    df1.at[i,"Result"] = int(exponent) * np.log(int(base))

max_index = df1["Result"].idxmax()
print(df1)
print(max_index+1)  # +1 because indexing starts at 0 rather than at 1

# Answer = 709
