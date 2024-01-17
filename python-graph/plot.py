import matplotlib.pyplot as plt
import math

r = 5.0
exact_pi = math.pi
approximation_pi = 3.14

s1 = exact_pi * r * r
s2 = approximation_pi * r * r

absolute_err = abs(s1 - s2)
relative_err = absolute_err / s1
percentage_err = relative_err * 100

print("Exercise 9", absolute_err, percentage_err)

circle1 = plt.Circle((0, 0), r, color='r', alpha=0.2, label='Exact Area')
circle2 = plt.Circle((0, 0), r, color='black', alpha=0.2, label='Approximate Area')

fig, ax = plt.subplots()  
ax.add_artist(circle1)
ax.add_artist(circle2)

ax.set_aspect('equal')  
ax.legend()

# zoome out a bit
plt.xlim(-6, 6)
plt.ylim(-6, 6)



plt.show()
