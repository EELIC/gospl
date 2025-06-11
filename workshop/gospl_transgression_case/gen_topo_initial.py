# gen_topo_initial.py
import numpy as np
import xarray as xr

nx, ny = 200, 100
dx, dy = 500, 500

x = np.arange(nx) * dx
y = np.arange(ny) * dy
X, Y = np.meshgrid(x, y, indexing='ij')

# 简单倾斜地形（模拟大陆到海盆过渡）
Z = 100 - (X / (nx * dx)) * 150  # 从 +100m 降至 -50m

ds = xr.Dataset(
    {"topography": (("x", "y"), Z)},
    coords={"x": x, "y": y}
)
ds.to_netcdf("topo_initial.nc")
