import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2_maze_data.csv")
df_mean = pd.read_csv("2_maze_data_mean.csv")

for i in range(2, 11):
    df_n = df[df['n'] == i]
    df_mean.iloc[i - 2] = [i, df_n['ms'].mean(), df_n['bfs'].mean(), df_n['dfs'].mean(), df_n['bfs2'].mean(), df_n['dfs2'].mean()]
    print("n =", i)
    print("BFS:", df_n['bfs'].mean())
    print("DFS:", df_n['dfs'].mean())
    print("BFS2:", df_n['bfs2'].mean())
    print("DFS2:", df_n['dfs2'].mean())
    print("BFS → DFS:", df_n['bfs'].mean() + df_n['dfs2'].mean())
    print("DFS → BFS:", df_n['dfs'].mean() + df_n['bfs2'].mean())
    print()

df_mean.to_csv("2_maze_data_mean.csv", index=False)

print(df.groupby('n')['ms'].count())
print("Total data:", len(df))

plt.plot(df_mean['n'], df_mean['bfs mean'], label='BFS 1st', marker='o')
plt.plot(df_mean['n'], df_mean['dfs mean'], label='DFS 1st', marker='o')
plt.plot(df_mean['n'], df_mean['bfs2 mean'], label='BFS 2nd', marker='x')
plt.plot(df_mean['n'], df_mean['dfs2 mean'], label='DFS 2nd', marker='x')
plt.xlabel('N')
plt.ylabel('Average Time (ms)')
plt.title('Average Time')
plt.legend()
plt.show()

plt.plot(df_mean['n'], df_mean['bfs mean'] + df_mean['dfs2 mean'], label='BFS → DFS', marker='o')
plt.plot(df_mean['n'], df_mean['dfs mean'] + df_mean['bfs2 mean'], label='DFS → BFS', marker='x')
plt.plot(df_mean['n'], df_mean['bfs mean'] * 2, label='BFS → BFS', marker='s')
plt.plot(df_mean['n'], df_mean['dfs mean'] * 2, label='DFS → DFS', marker='^')
plt.xlabel('N')
plt.ylabel('Average Time Sum(ms)')
plt.title('Average Time Sum')
plt.legend()
plt.show()