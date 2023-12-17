import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # line 1

        self.label1 = customtkinter.CTkLabel(self, text="Enter the URL of the YouTube video:")
        self.label1.grid(row=0, column=0)

        self.entry1 = customtkinter.CTkEntry(self)
        self.entry1.grid(row=0, column=1)

        self.button1 = customtkinter.CTkButton(self, text="Download")
        self.button1.grid(row=0, column=2)

        # line 2

        self.label2 = customtkinter.CTkLabel(self, text="Downloading Path:")
        self.label2.grid(row=1, column=0)

        self.label3 = customtkinter.CTkLabel(self, text="PATH")
        self.label3.grid(row=1, column=1)

        self.button2 = customtkinter.CTkButton(self, text="Change path")
        self.button2.grid(row=1, column=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()
