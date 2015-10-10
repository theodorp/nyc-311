from __future__ import print_function

import pandas as pd

from bokeh.browserlib import view
from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models.glyphs import Circle
from bokeh.io import vform
from bokeh.models import (
    GMapPlot, Range1d, ColumnDataSource,
    PanTool, WheelZoomTool, BoxSelectTool,
    BoxSelectionOverlay, GMapOptions, HoverTool, Slider)
from bokeh.resources import INLINE

x_range = Range1d()
y_range = Range1d()

# JSON style string taken from: https://snazzymaps.com/style/1/pale-dawn
map_options = GMapOptions(lat=40.7213, lng=-73.9968, map_type="roadmap", zoom=12, styles="""
[{"featureType":"administrative","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"landscape","elementType":"all","stylers":[{"visibility":"simplified"},{"hue":"#0066ff"},{"saturation":74},{"lightness":100}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"off"},{"weight":0.6},{"saturation":-85},{"lightness":61}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"visibility":"on"}]},{"featureType":"road.arterial","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road.local","elementType":"all","stylers":[{"visibility":"on"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"water","elementType":"all","stylers":[{"visibility":"simplified"},{"color":"#5f94ff"},{"lightness":26},{"gamma":5.86}]}]
""")

plot = GMapPlot(
    x_range=x_range, y_range=y_range,
    map_options=map_options,
    title="Manhattan"
)

df = pd.read_csv('parties_2014.csv', nrows=10000, usecols=['Descriptor','Borough','Latitude', 'Longitude'])
df = df[(df['Borough']=='MANHATTAN')]
df = df.dropna()

source = ColumnDataSource(
    data=dict(
        lat=df['Latitude'],
        lon=df['Longitude'],
    )
)

circle = Circle(x="lon", y="lat", size=5, fill_alpha=0.5, fill_color="magenta", line_alpha=0.3, line_color="black")
plot.add_glyph(source, circle)

slider = Slider(start=0, end=6, value=1, step=1, title="Weekdays")

pan = PanTool()
wheel_zoom = WheelZoomTool()
box_select = BoxSelectTool()

plot.add_tools(pan, wheel_zoom, box_select)
overlay = BoxSelectionOverlay(tool=box_select)
plot.add_layout(overlay)

# layout = vform(slider, plot)

doc = Document()
# doc.add(slider)
doc.add(plot, slider)

if __name__ == "__main__":
    filename = "maps.html"
    with open(filename, "w") as f:
        f.write(file_html(doc, INLINE, "Google Maps Example"))
    print("Wrote %s" % filename)
    view(filename)