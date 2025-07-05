import pandas as pd

df = pd.read_csv("maze_data.csv")
df_mean = pd.read_csv("maze_data_mean.csv")

for i in range(2, 11):
    df_n = df[df['n'] == i]
    df_mean.iloc[i - 2] = [i, df_n['ms'].mean(), df_n['bfs'].mean(), df_n['dfs'].mean()]
    print("n =", i)
    print("BFS:", df_n['bfs'].mean())
    print("DFS:", df_n['dfs'].mean())
    print()

df_mean.to_csv("maze_data_mean.csv", index=False)

print(df.groupby('n').count())
print("Total data:", len(df))