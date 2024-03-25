import numpy as np
marks = [1, 2, 3, 4, 5]
p = np.array([0.1, 0.25, 0.25, 0.28, 0.12])
generated_marks = np.random.choice(marks, size=15, p=p)

print("Vygenerované známky:", generated_marks)
