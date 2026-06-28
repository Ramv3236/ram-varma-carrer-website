"""
3D Image Surface Visualization
Rotate your profile image as a 3D surface
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# 1. Load the image and convert to grayscale
try:
    img = Image.open('my_image.png').convert('L') 
    print("✓ Image loaded successfully")
except FileNotFoundError:
    print("⚠ Image not found. Creating a synthetic 3D surface...")
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(- (X**2 + Y**2)) * 255
    img = Image.fromarray(Z.astype(np.uint8))

# 2. Downsample for smooth rendering
img.thumbnail((150, 150))  
img_array = np.array(img)

# 3. Create 3D coordinates from image
height, width = img_array.shape
x = np.arange(0, width)
y = np.arange(0, height)
X, Y = np.meshgrid(x, y)

# 4. Use pixel intensity as height (Z coordinate)
Z = img_array 

# 5. Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.axis('off')

# Plot the 3D surface
surface = [ax.plot_surface(X, -Y, Z, cmap='plasma', edgecolor='none', rstride=1, cstride=1, alpha=0.9)]

# Initial camera angle
ax.view_init(elev=35, azim=0)

# Set labels
ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Intensity')

# 6. Animation function - rotate 360 degrees
def update(frame):
    ax.view_init(elev=35, azim=frame)
    return surface

# 7. Create animation (360° rotation)
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=False, repeat=True)

plt.title('3D Profile Image Visualization - 360° Rotation', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()
