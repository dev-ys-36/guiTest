import tkinter as gui

#window
window = gui.Tk()
window.title("test") 
window.geometry("640x400+100+100") #x + y value
window.resizable(True, True) #size value

#function
def test1():
    print('test1')

def test2():
    print('test2') 

#label
label = gui.Label(window, text='test')
label.pack()

#button
b1 = gui.Button(window, text='test1', command=test1)
b2 = gui.Button(window, text='test2', command=test2)
b1.pack(side=gui.LEFT, padx=10)
b2.pack(side=gui.LEFT, padx=10)

#entry
"""gui.Label(window, text='test1').grid(row=0)
gui.Label(window, text='test2').grid(row=1)

e1 = gui.Entry(window)
e2 = gui.Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)"""

window.mainloop()