import numpy as np

data = np.array([20, 23, -100, -5, 30, 70, -18, 99, 81, 16, 45, 90, -39, -82, 75, 0, 16, 91, 48, 0, 70])

result1 = np.where(data < 0)

result2 = np.where((data >= -10) & (data <= -1))

result3 = np.where((data >= 1) & (data <= 50) | (data < 0))

print(data[result1])
print(data[result2])
print(data[result3])
