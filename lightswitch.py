import tkinter as tk
window = tk.Tk()

button = tk.Button(text='licht knop', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
knopje = 0
def klik(event):
    global knopje
    if knopje == 0:
        print('het licht staat aan.')
        button['text'] = 'licht knop staat aan'
        window.configure(bg='yellow')
        knopje = 1
    else:
        print('het licht staat uit.')
        button['text'] = 'licht knop staat uit'
        window.configure(bg='black')
        knopje = 0

button.bind("<Button>", klik)

# schijf hier tussen je code

window.mainloop()