import tkinter as tk
from tkinter import ttk


#window
window = tk.Tk()
window.title('OxelTech')
window.geometry('800x600')





#frame middle
frame_top = tk.Frame(window, width = 100, height=50,background="bisque")
frame_left = tk.Frame(window, width = 50, height=200,background="bisque")
canvas_middle = tk.Canvas(window, width = 100, height=100, borderwidth= 10,relief=tk.GROOVE)
frame_right= tk.Frame(window, width = 50, height=200,background="bisque")
frame_bottom = tk.Frame(window, width = 100, height=50,background="bisque")

#add image in the canvas
image_logo_stm = tk.PhotoImage(file="log_stm_resized1.png")
canvas_middle.create_image(122,120, image=image_logo_stm )
canvas_middle.create_text(120,210, text= "STM32F4", font=("courier", 12, "bold"))







#define a grid
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)


#place widgets
frame_top.grid(row=0,column=1,sticky='sew')
frame_left.grid(row=1,column=0,sticky='nse')
canvas_middle.grid(row=1,column=1,sticky='nswe')
frame_right.grid(row=1,column=2,sticky='nsw')
frame_bottom.grid(row=2,column=1,sticky='new')


# left side pin configuration
list_left_button_text = ['VDD', 'PC13', 'PC14-OSC32-IN', 'PC13', 'VDD', 'VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD']

left_pin_count = 16
list_left_pin_count = list(range(left_pin_count))
frame_left.columnconfigure(0,weight=1)
frame_left.rowconfigure(list_left_pin_count,weight=1)

for i in range(left_pin_count):
    temp_button = tk.Button(frame_left, text=list_left_button_text[i],  width=3, height= 1,anchor='w',bd = 1)
    temp_button.grid(row=i,column=0,sticky='nsew')


# right side pin configuration
list_right_button_text = ['PF7', 'PF6', 'PC14-OSC32-IN', 'PC13', 'VDD', 'VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD']

right_pin_count = 16
list_right_pin_count = list(range(right_pin_count))
frame_right.columnconfigure(0,weight=1)
frame_right.rowconfigure(list_right_pin_count,weight=1)

for i in range(right_pin_count):
    temp_button = tk.Button(frame_right, text=list_right_button_text[i],  width=3, height= 1,anchor='w',bd = 1)
    temp_button.grid(row=i,column=0,sticky='nsew')


# top side pin configuration
list_top_button_text = ['PF7', 'PF6', 'PC14-OSC32-IN', 'PC13', 'VDD', 'VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD']

top_pin_count = 16
list_top_pin_count = list(range(top_pin_count))
frame_top.columnconfigure(list_top_pin_count,weight=1)
frame_top.rowconfigure(0,weight=1)

for i in range(top_pin_count):
    temp_button = tk.Button(frame_top, text=list_top_button_text[i],  width=2, height= 1,anchor='w',bd = 1)
    temp_button.grid(row=0,column=i,sticky='nsew')


# bottom side pin configuration
list_bottom_button_text = ['PF7', 'PF6', 'PC14-OSC32-IN', 'PC13', 'VDD', 'VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD','VDD']

bottom_pin_count = 16
list_bottom_pin_count = list(range(bottom_pin_count))
frame_bottom.columnconfigure(list_bottom_pin_count,weight=1)
frame_bottom.rowconfigure(0,weight=1)

for i in range(bottom_pin_count):
    temp_button = tk.Button(frame_bottom, text=list_bottom_button_text[i],  width=2, height= 1,anchor='w',bd = 1)
    temp_button.grid(row=0,column=i,sticky='nsew')

# #main loop
window.mainloop()