"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
import os.path
import matplotlib.cm as cmx
import matplotlib.colors as colors



def get_cmap(N):
    '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct 
    RGB color.'''
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv') 
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return np.arange(N)


file = open(os.path.normpath("C:/Data/nba.csv"))
print("starting")

count = 0
data = []
for line in file:
	data.append(line.split(","))
file.close()
print("done reading data")

N = len(data) 
x = []#np.random.rand(N)
y = []#np.random.rand(N)
color = get_cmap(6*N)#np.random.rand(2*N)
col = []


tcMap = {}
pcMap = {}
pMap = {}

count = 0
pCount = 0
print(data[1])
print(len(data))
names = []
area = []
for i in range(0,N):
	print(i)
	'''if tcMap.get(data[i][2]) == None:
		tcMap[data[i][2]] = colors[count]
		count+=1'''
	if pcMap.get(data[i][1]) == None:
		pcMap[data[i][1]] = color[count]
		count+=5
		count = count % N

	print(data[i][0])
	x.append(data[i][0][:data[i][0].index("-")])
	col.append(pcMap.get(data[i][1])) #colors
	y.append( float(data[i][2]) ) #Gets win percentages
	area.append( float(data[i][3]) ) #Gets the games won in an array to make as sizes for mvps
	names.append(data[i][1])



area =   (np.array(area))**2 # 0 to 15 point radiuses
print(x)

fig, ax = plt.subplots()

plt.scatter(x, y, s=area, c=col, alpha=0.5)

for i, txt in enumerate(names):
    ax.annotate(txt, (x[i],y[i]))

plt.show()

