import matplotlib.pyplot as plt
plt.title('graph')
plt.plot([1,2,3,4],[12,43,25,15], 'r.', color = 'skyblue', ls = '--', label = 'blue')
plt.plot([1,2,3,4], 'r.--')

plt.legend()
plt.show()