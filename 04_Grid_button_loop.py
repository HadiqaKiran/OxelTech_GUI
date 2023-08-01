import tkinter as tk
from tkinter import ttk


#window
window = tk.Tk()
window.title('Test')
window.geometry('800x600')

#frames
frame_top = tk.Frame(window, width = 100, height=50,background="bisque")
frame_left = tk.Frame(window, width = 50, height=200,background="bisque")
canvas_middle = tk.Canvas(window, width = 100, height=100, borderwidth= 10,relief=tk.GROOVE)
frame_right= tk.Frame(window, width = 50, height=200,background="bisque")
frame_bottom = tk.Frame(window, width = 100, height=50,background="bisque")

#add image in the canvas
image_logo_stm = tk.PhotoImage(file="st_logo.png")
canvas_middle.create_image(260,180, image=image_logo_stm )
canvas_middle.create_text(260,360, text= "STM32F130", font=("courier", 30, "bold"))


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

#Options to be displayed for each pin
list_pin_config_options = ['GPIO_INPUT_DIGITAL', 'GPIO_OUTPUT_DIGITAL', 'GPIO_INPUT_ANALOG', 'GPIO_OUTPUT_ANALOG']

# left side pin configuration
list_left_button_text = ['VDD', 'PC13', 'PC14-OSC32-IN', 'PC15-OSC32_OUT', 'PF0-OSC_IN', 'PF1-OSC_OUT','NRST','PC0','PC1','PC2','PC3','VSSA','VDDA','PA0','PA1','PA2']

left_pin_count = 16
list_left_pin_count = list(range(left_pin_count))
frame_left.columnconfigure(0,weight=1)
frame_left.rowconfigure(list_left_pin_count,weight=1)

btn_cntr = 0

for i in range(left_pin_count):
    temp_button = tk.Menubutton(frame_left, text=list_left_button_text[i],  width=3, height= 1,anchor='w',bd = 1)
    temp_menu =  tk.Menu ( temp_button, tearoff = 0 )
    temp_button["menu"] =  temp_menu
    for item in list_pin_config_options:
        temp_menu.add_radiobutton ( label = item, value=btn_cntr)
        btn_cntr+=1
    temp_button.grid(row=i,column=0,sticky='nsew')


# right side pin configuration
list_right_button_text = ['PF7', 'PF6','PA13', 'PA12', 'PA11', 'PA10','PA9','PA8','PC9','PC8','PC7','PC6','PB15','PB14','PB13','PB12']

right_pin_count = 16
list_right_pin_count = list(range(right_pin_count))
frame_right.columnconfigure(0,weight=1)
frame_right.rowconfigure(list_right_pin_count,weight=1)

for i in range(right_pin_count):
    temp_button = tk.Menubutton(frame_right, text=list_right_button_text[i], width=3, height= 1,anchor='w',bd = 1)
    temp_menu =  tk.Menu ( temp_button, tearoff = 0 )
    temp_button["menu"] =  temp_menu
    for item in list_pin_config_options:
        temp_menu.add_radiobutton ( label = item, value=btn_cntr)
        btn_cntr +=1
    temp_button.grid(row=i,column=0,sticky='nsew')


# top side pin configuration
list_top_button_text = ['VDD','VSS','PB9','PB8','BOOT0','PB7','PB6','PB5','PB4','PB3','PD2','PC12','PC11','PC10','PA15','PA14']

top_pin_count = 16
list_top_pin_count = list(range(top_pin_count))
frame_top.columnconfigure(list_top_pin_count,weight=1)
frame_top.rowconfigure(0,weight=1)

for i in range(top_pin_count):
    temp_button = tk.Menubutton(frame_top, text=list_top_button_text[i],  width=3, height= 1,anchor='w',bd = 1)
    temp_menu =  tk.Menu ( temp_button, tearoff = 0 )
    temp_button["menu"] =  temp_menu
    for item in list_pin_config_options:
        temp_menu.add_radiobutton ( label = item,value=btn_cntr)
        btn_cntr+=1
    temp_button.grid(row=0,column=i,sticky='nsew')


# bottom side pin configuration
list_bottom_button_text = ['PA3', 'PF4', 'PF5', 'PA4','PA5','PA6','PA7','PC4','PC5','PB0','PB1','PB2','PB10','PB11','VSS','VDD']

bottom_pin_count = 16
list_bottom_pin_count = list(range(bottom_pin_count))
frame_bottom.columnconfigure(list_bottom_pin_count,weight=1)
frame_bottom.rowconfigure(0,weight=1)

for i in range(bottom_pin_count):
    temp_button = tk.Menubutton(frame_bottom, text=list_bottom_button_text[i],  width=3, height= 1,anchor='w',bd = 1)
    temp_menu =  tk.Menu ( temp_button, tearoff = 0 )
    temp_button["menu"] =  temp_menu
    for item in list_pin_config_options:
        temp_menu.add_radiobutton ( label = item,value=btn_cntr)
        btn_cntr+=1
    temp_button.grid(row=0,column=i,sticky='nsew')

# #main loop
window.mainloop()