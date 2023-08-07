import matplotlib.pyplot as plt

x=['(0,1)','(0,2)','(0,3)','(0,5)','(0,6)','(0,7)','(0,8)','(0,9)']
y=[48, 48, 48, 48, 48, 48, 48, 48]

plt.plot(x,y)

plt.xlabel('Goal Nodes')
plt.ylabel('Maximum Fringe Size')

plt.title('DFS')

plt.show()