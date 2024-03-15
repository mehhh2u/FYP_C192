import numpy as np
from noise import pnoise2
from PIL import Image
import os

# Heightmap dimensions
width = 513  # 2^9 + 1
height = 513  # 2^9 + 1

# Scale factor for the noise. Lower values mean the terrain features will be larger.
scale = 100.0
base = np.random.randint(0, 1000)   
print(f"Base (Seed): {base}")
octaves = 4
persistence = 0.3
lacunarity = 2.0

# Folder to save the heightmap
folder_name = "heightmaps"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create an empty image
heightmap = np.zeros((width, height))

# Fill in the heightmap with Perlin noise
for x in range(width):
    for y in range(height):
        # Generate Perlin noise value between -1 and 1
        value = pnoise2(x / scale, y / scale, 
                        octaves=octaves, 
                        persistence=persistence, 
                        lacunarity=lacunarity, 
                        repeatx=1024, 
                        repeaty=1024, 
                        base=base)
        # Normalize to 0 to 255
        color = int((value + 1) * 128)
        heightmap[x, y] = color

# Save the heightmap
heightmap_path = os.path.join(folder_name, 'heightmap.png')
img = Image.fromarray(heightmap.astype(np.uint8))
img.save(heightmap_path)

print(f"Heightmap saved at: {heightmap_path}")
