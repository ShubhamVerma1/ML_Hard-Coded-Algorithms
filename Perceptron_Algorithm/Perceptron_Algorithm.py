import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Training set
# Training is done on three features x, y, z
x_train = [1]*100
y_train = [1]*100
z_train = [1]*100
# Output for each set of x, y, z
output_train = [1]*100

# Threshold
theta = 0

# Learning Rate
m = 0.1

# Making of Training set

# For output class 1
for i in range(50):
    x_train[i] = random.randint(5, 11)
    y_train[i] = (random.randint(4, 9))
    z_train[i] = (random.randint(2, 10))
    output_train[i] = 1

# For output class 0
for i in range(50, 100):
    x_train[i] = random.randint(-1, 4)
    y_train[i] = (random.randint(-4, 3))
    z_train[i] = (random.randint(-3, 6))
    output_train[i] = 0


# Assigning Random values to weights

weights = [1]*4
weights[0] = random.uniform(0, 1)  # for x
weights[1] = random.uniform(0, 1)  # for y
weights[2] = random.uniform(0, 1)  # for z
weights[3] = random.uniform(0, 1)  # for the bias


# Method for calculating Current output for current wieghts

def calculate_output(theta, weight, x, y, z):
    if (weight[0] * x + weight[1] * y + weight[2] * z + weight[3]) >= theta:
        return 1
    else:
        return 0


iteration = 0

while True:

    global_error = 0

    for j in range(100):

        current_ouput = calculate_output(theta, weights, x_train[j], y_train[j], z_train[j])

        #localerror = actual output - current_output
        localerror = output_train[j] - current_ouput

        weights[0] += localerror * m * x_train[j] * 1.0000000000000000
        weights[1] += localerror * m * y_train[j] * 1.0000000000000000
        weights[2] += localerror * m * z_train[j] * 1.0000000000000000
        weights[3] += localerror * m * 1.0000000000000000
        # Sum of squared errors
        global_error += localerror * localerror
    iteration += 1

    if global_error == 0 or iteration == 1000:
        break

print("No of iterations = ",iteration)
print()
print("Boundry Plane equation is ->  "+ str(weights[0])+"* x + "+ str(weights[1])+"* y + "+ str(weights[2])+"* z + "+ str(weights[3])+" = 0 ")



# Plotting on graph part -

#First we create the plane

#Take x and y
xx, yy = np.meshgrid(range(10), range(10))

# Equation of plane is -  a*x+b*y+c*z+d = 0
# where a, b, c, d are weights[0, 1, 2, 3]
# So z = (-1/c)*(a*x+ b*y+ d)

z = (-weights[0] * xx - weights[1] * yy - weights[3]) * 1. /weights[2]

plt3d = plt.figure().gca(projection='3d')

# Plot the plane
plt3d.plot_surface(xx, yy, z, alpha=0.2)

ax = plt.gca()
ax.hold(True)

# Plot the points with output 1, color red
ax.scatter(x_train[:50], y_train[:50], z_train[:50], c='r', marker='o')

# Plot the points with output 0, color blue
ax.scatter(x_train[50:], y_train[50:], z_train[50:], c='b', marker='o')

ax.set_xlabel('X Feature')
ax.set_ylabel('Y Feature')
ax.set_zlabel('Z Feature')

plt.show()
