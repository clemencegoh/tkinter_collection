import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    label = tk.Label(text="hello world")
    entry = tk.Entry()
    label.pack()
    entry.pack()

    window.mainloop()
