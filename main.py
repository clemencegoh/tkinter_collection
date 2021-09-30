import tkinter as tk
from tkinter.constants import COMMAND


def test_frame(frame: tk.Tk):
    someLabel = tk.Label(frame, text="Hello world label")


class ScreenController:
    def __init__(self, root: tk.Tk):
        self.root = root
        # self.activity_frame = tk.Frame(root, bd=1)
        # self.activity_frame.pack(
        #     side=tk.BOTTOM,
        #     fill=tk.BOTH,
        #     expand=1,
        # )
        self.main_screen()

    def rebuild_activity(self):
        # if self.activity_frame:
        #     self.activity_frame.destroy()
        # self.activity_frame = tk.Frame(self.root, bd=1)
        # self.activity_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        pass

    def main_screen(self):
        # self.rebuild_activity()
        test_frame(self.root)


def gui(window: tk.Tk):
    greeting = tk.Label(
        text="hello world",
        foreground="white",
        background="black",
        height=10,
        width=10,
    )

    def get_input():
        userInput = formEntry.get()
        print(userInput)

    formLabel = tk.Label(
        text="name",
    )
    formEntry = tk.Entry()
    formEntry.insert(0, "placeholder text")

    button = tk.Button(
        text="Click me!",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=get_input,
    )

    formLabel.pack()
    formEntry.pack()
    button.pack()


if __name__ == "__main__":
    # set up tkinter
    window = tk.Tk()
    window.title("Tkinter components")
    window.geometry("1200x600")  # todo: remove this
    # controller = ScreenController(root)
    gui(window=window)

    window.mainloop()
