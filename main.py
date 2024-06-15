#hi
import tkinter
import tkintermapview
import random
from urllib.request import urlopen
import json

rootTk = tkinter.Tk()
rootTk.geometry(f"{800}x{600}")
rootTk.title("Map view")

map_widget = tkintermapview.TkinterMapView(rootTk, width=800, height = 600, corner_radius=8)
map_widget.pack(fill = "both", expand = True)

#google normal title server
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)



def getGPSLoc():
  url = "http://ipinfo.io/json"
  response = urlopen(url)
  data = json.load(response)
  loc = data["loc"]

  Playerlat, Playerlon = map(float, loc.split(","))

  print(Playerlat, Playerlon)
  return Playerlat, Playerlon

def testClick(marker):
    print("marker clicked:", marker.text)
    marker.set_text("hello")

def testClick2(marker):
    randomList = [1, 2, 3, 4, 5]
    marker.set_text(random.choice(randomList))

def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")


lat, lon = getGPSLoc()
#sets the position in the starting
map_widget.set_position(lat, lon)
marker = map_widget.set_marker(51.5074, 0.1278, command = testClick2, text = "London", marker_color_circle="black") 
map_widget.add_right_click_menu_command(label="Add Marker", command=add_marker_event, pass_coords=True)

rootTk.mainloop()
