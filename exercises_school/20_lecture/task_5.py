import numpy as np

data = np.array([0.1743, 0.2732, 0.3521, 0.4924])
filter = np.array([True, False, True, False])
nova_data = data[filter]
print("Nová data:", nova_data)
print("Stará data:", data)
data *= 1000
data -= 1
nove_data = np.array([10, 20, 30, 40])
data += nove_data
pripraveny_filtr = data < 0.25
print("Nová data:", nova_data)
print("Stará data:", data)
print("Filtr:", pripraveny_filtr)
