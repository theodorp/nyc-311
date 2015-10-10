import pandas as pd
from ggplot import *
import matplotlib.pyplot as plt

from bokeh import mpl
from bokeh.plotting import output_file, show

df = pd.read_csv('parties_2014.csv', parse_dates=['Created Date'])

df1 = df.loc[0:12000]
df1 = df1.dropna(subset = ['Longitude', 'Latitude'])
df1 = df1[df1['Borough']=='MANHATTAN']

g = ggplot(aes('Latitude', 'Longitude'), data=df1) + geom_point()
g.draw()

plt.title("ggplot to bokeh")

output_file('test.html')
show(mpl.to_bokeh())