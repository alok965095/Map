from tkinter import *
import tkintermapview 
from tkintermapview import TkinterMapView
def srch():
    search = var.get()
    gm.set_address(search,marker=True)
root = Tk() 
var = StringVar()
search = "India"
gm = TkinterMapView(root,width=750,height=400)
gm.pack(fill = "both",expand=True)
gm.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",\
                   max_zoom=22)
gm.set_address(search,marker=False)
gm.set_zoom(12)
root.geometry("600x600")
root.title("Map")
root.resizable(0,0)
ent = Entry(root,textvariable=var,font = "verdana 17").place(x = 140,y = 20)
btn = Button(root,text = "Search",font = "verdana 12",command = srch).place(x = 400,y = 20)
root.mainloop()

