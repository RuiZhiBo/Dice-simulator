from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []

for roll_num in range(1000):
	result = die.roll()
	results.append(result)

#分析结果
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果频率'}

my_layout = Layout(title='投掷D6 1000次模拟器', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')
