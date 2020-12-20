import matplotlib.pyplot as plt
import numpy as np

A = np.loadtxt("day20.npy", dtype=int)
nx, ny = A.shape

monster_coords = [(1, 21), (1, 48), (10, 63), (11, 12), (16, 65), (18, 2), (22, 46), (22, 70), (25, 16), (29, 44), (35, 67), (38, 20), (39, 73), (40, 49), (46, 7), (47, 36), (47, 62), (52, 50), (59, 50), (61, 2), (61, 27), (63, 72), (68, 7), (70, 39), (74, 1), (75, 67), (80, 1), (80, 23), (82, 63), (86, 42), (91, 8), (91, 40), (91, 71)]

monster_str = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "]
monster_pix = []
for i in range(3):
  for j in range(20):
    if monster_str[i][j] == "#":
      monster_pix.append((i,j))

water1_col = (38, 111, 199)
water2_col = (102, 163, 237)
monster_col = (65, 240, 85)

# Draw ocean
image = []
for i in range(nx):
  row = []
  image.append(row)
  for j in range(nx):
    if A[i,j] == 1:
      row.append(water1_col)
    else:
      row.append(water2_col)
image = np.array(image)

# Put monsters
for i0, j0 in monster_coords:
  for i, j in monster_pix:
    image[i0+i, j0+j, :] = monster_col

plt.figure(figsize=(10,10))
plt.imshow(image)
plt.axis('off')
plt.tight_layout()

plt.show()
