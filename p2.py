import matplotlib.pyplot as plt
medals = ['Gold', 'Silver', 'Bronze', 'Total']
aus = [32, 59, 59, 150]
sa = [21, 14, 19, 54]
plt.bar(medals, aus, label = 'By Australia')
plt.bar(medals, sa, label = 'By South Africa')
plt.xlabel('Medals')
plt.ylabel('Amount')
plt.legend()
plt.title('Medals won by Australia and South Africa in a cricket match')
plt.show()