#hi
import tkinter
import tkintermapview
import random

rootTk = tkinter.Tk()
rootTk.geometry(f"{800}x{600}")
rootTk.title("Map view")

map_widget = tkintermapview.TkinterMapView(rootTk, width=800, height = 600, corner_radius=8)
map_widget.pack(fill = "both", expand = True)

#google normal title server
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)


def testClick(marker):
    print("marker clicked:", marker.text)
    marker.set_text("hello")

def testClick2(marker):
    randomList = [1, 2, 3, 4, 5]
    marker.set_text(random.choice(randomList))

marker = map_widget.set_marker(51.5074, 0.1278, command = testClick2, text = "London", marker_color_circle="black") 
# marker1 = map_widget.set_address("colosseo, rome, italy", marker=True, command = testClick)
# marker2 = map_widget.set_address("Delhi, India", marker=True, command = testClick2)
'''
DONT NEED TO USE SET ADDRESS IF USING LATITUDE LONGITUDE
'''

rootTk.mainloop()
