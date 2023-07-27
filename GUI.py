import tkinter as tk


#create window object
myWindow = tk.Tk()
myWindow.geometry("600x400")

#create label
company = tk.Label(text="OxelTech", font=("Arial", 25), fg='#f00')
company.pack()



#create entry
entry = tk.Entry()
entry.pack()


#function called when button is pressed
def submit(): 
    name=entry.get()     
    print("The name is : " + name)
    entry.delete(0,"end")   

# create button
sub_btn = tk.Button(text = 'Submit',bg="blue" ,command = submit)
sub_btn.pack()

#to display window. It enables the window to listen continuously
myWindow.mainloop()