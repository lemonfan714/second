import matplotlib.pyplot as plt

type_eq = 'linar'
x = [i for i in range(-10, 10)]
k = 0.25
y = []
for i in x:
    y.append(i * k)

fig = plt.figure(figsize = (8.0, 8.0))
ax = fig.add_subplot()

ax.plot(x, y, color='black', marker='o')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.show()