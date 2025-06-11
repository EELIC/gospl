# gen_uplift.py
import numpy as np
import xarray as xr

nx, ny = 200, 100
dx, dy = 500, 500

x = np.arange(nx) * dx
y = np.arange(ny) * dy
uplift = np.zeros((nx, ny))  # 海侵环境中地壳稳定为主

ds = xr.Dataset(
    {"uplift": (("x", "y"), uplift)},
    coords={"x": x, "y": y}
)
ds.to_netcdf("uplift.nc")
