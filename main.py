import pandas as pd
import matplotlib.pyplot as plt

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

print(df.groupby('n')['ms'].count())
print("Total data:", len(df))

plt.plot(df_mean['n'], df_mean['bfs mean'], label='BFS', marker='o')
plt.plot(df_mean['n'], df_mean['dfs mean'], label='DFS', marker='o')
plt.xlabel('Number of Nodes (n)')
plt.ylabel('Average Time (ms)')
plt.title('Average Time for BFS and DFS Algorithms')
plt.legend()
plt.show()