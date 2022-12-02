import laspy
import numpy as np
import rasterio as rio
from tqdm import tqdm
from os.path import basename

path = r"C:\Users\pnytko\Desktop\5068_127858_M-34-78-D-c-2-1-2.laz"
las = laspy.read(path)
raster = rio.open(r"C:\Users\pnytko\Desktop\67491_717546_M-34-78-D-c-2-1-2.tif")
coords = np.dstack((las.x, las.y, las.z))[0]
las = laspy.convert(las, point_format_id=2)

points_to_write = []

r_colors = []
g_colors = []
b_colors = []

with tqdm(total=len(coords)) as pbar:
    for i, point in enumerate(coords):
        for val in raster.sample([(point[0], point[1])]):  
            r_colors.append(val[0])
            g_colors.append(val[1])
            b_colors.append(val[2])
        pbar.update(1)

las.red = r_colors
las.green = g_colors
las.blue = b_colors

las.write('test.las')