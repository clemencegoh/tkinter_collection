import tkinter as tk


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


def text_field_component(parent: tk.Frame, label: str, isPassword: bool):
    field_wrapper = tk.Frame(master=parent)
    field_wrapper.pack()

    field_label = tk.Label(master=field_wrapper, text=label)
    field_entry = tk.Entry(master=field_wrapper)

    if isPassword:
        field_entry = tk.Entry(master=field_wrapper, show="*")

    field_label.pack(fill=tk.X, side=tk.LEFT, expand=True)
    field_entry.pack(fill=tk.X, side=tk.LEFT, expand=True)


def basic_form(master: tk.Frame):
    # build overall wrapper
    overall_wrapper = tk.Frame(master=master, height=300, width=50)
    overall_wrapper.pack()

    text_field_component(overall_wrapper, "username: ", False)
    text_field_component(overall_wrapper, "password: ", True)
    submit_button = tk.Button(master=overall_wrapper, text="Submit")
    submit_button.pack()


if __name__ == "__main__":
    # set up tkinter
    window = tk.Tk()
    window.title("Tkinter components")
    window.geometry("1200x600")  # todo: remove this
    # controller = ScreenController(root)
    # gui()
    basic_form(window)

    window.mainloop()
