import tkinter as tk
import json


#create window object
myWindow = tk.Tk()
myWindow.geometry("600x400")

#create label
company = tk.Label(text="OxelTech", font=("Arial", 25), fg='#f00')
company.pack()



#create entry1
entry = tk.Entry()
entry.pack()


#Read file 
with open ('gui.json', 'r') as fileRead:
    data= json.load(fileRead) 

#function called when button is pressed
def submit(): 
    name=entry.get()     
    print("The name is : " + name)
    entry.delete(0,"end")
    data["P6"] = name
    #Write in file 
    with open ('gui.json', 'w') as fileWrite:
        json.dump(data, fileWrite)  










# create button
sub_btn = tk.Button(text = 'Submit',bg="blue" ,command = submit)
sub_btn.pack()









#to display window. It enables the window to listen continuously
myWindow.mainloop()