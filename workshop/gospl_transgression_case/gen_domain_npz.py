import numpy as np

nodes = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

triangles = np.array([
    [0, 1, 2],
    [0, 2, 3]
])

active = np.array([True, True])
elevation = np.array([0.0, 0.1, 0.2, 0.1])

np.savez("domain.npz", nodes=nodes, triangles=triangles, active=active, elevation=elevation)
print("✅ domain.npz 生成完成")
