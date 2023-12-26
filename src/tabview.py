import customtkinter


class TabView(customtkinter.CTkTabview):
    """
    Tabview which manages the interaction between the video and audio downloader.
    """

    def __init__(self, master):
        """
        Set up the UI components.
        """

        super().__init__(master)

        self.add("Video")
        self.add("Audio")

        #################
        ##### VIDEO #####
        #################

        # line 1

        self.url_status_label = customtkinter.CTkLabel(self.tab("Video"), text="Enter the URL of the YouTube video:")
        self.url_status_label.grid(row=0, column=0, padx=15, pady=10)

        self.url_entry = customtkinter.CTkEntry(self.tab("Video"), width=500)
        self.url_entry.grid(row=0, column=1, padx=15, pady=10)

        self.download_button = customtkinter.CTkButton(self.tab("Video"), text="Download", width=150)
        self.download_button.grid(row=0, column=2, padx=15, pady=10)
        self.download_button.configure(command=master.download_video)

        # line 2

        self.path_label1 = customtkinter.CTkLabel(self.tab("Video"), text="Downloading Path:")
        self.path_label1.grid(row=1, column=0, padx=15, pady=10)

        self.path_label2 = customtkinter.CTkLabel(self.tab("Video"), text=master.download_path)
        self.path_label2.grid(row=1, column=1, padx=15, pady=10)

        self.change_path_button = customtkinter.CTkButton(self.tab("Video"), text="Change path", width=150)
        self.change_path_button.grid(row=1, column=2, padx=15, pady=10)
        self.change_path_button.configure(command=master.change_path)

        # line 3

        self.progress_bar = customtkinter.CTkProgressBar(self.tab("Video"), mode="determinate")
        self.progress_bar.grid(row=2, column=0, padx=15, pady=10, columnspan=3, sticky="ew")
        self.progress_bar.set(0)

        # line 4

        self.status_label = customtkinter.CTkLabel(self.tab("Video"), text="Status")
        self.status_label.grid(row=3, column=2, padx=15, pady=10)

        #################
        ##### AUDIO #####
        #################

        # line 1

        self.url_status_label = customtkinter.CTkLabel(self.tab("Audio"), text="Enter the URL of the YouTube video:")
        self.url_status_label.grid(row=0, column=0, padx=15, pady=10)

        self.url_entry = customtkinter.CTkEntry(self.tab("Audio"), width=500)
        self.url_entry.grid(row=0, column=1, padx=15, pady=10)

        self.download_button = customtkinter.CTkButton(self.tab("Audio"), text="Download", width=150)
        self.download_button.grid(row=0, column=2, padx=15, pady=10)
        self.download_button.configure(command=master.download_video)

        # line 2

        self.path_label1 = customtkinter.CTkLabel(self.tab("Audio"), text="Downloading Path:")
        self.path_label1.grid(row=1, column=0, padx=15, pady=10)

        self.path_label2 = customtkinter.CTkLabel(self.tab("Audio"), text=master.download_path)
        self.path_label2.grid(row=1, column=1, padx=15, pady=10)

        self.change_path_button = customtkinter.CTkButton(self.tab("Audio"), text="Change path", width=150)
        self.change_path_button.grid(row=1, column=2, padx=15, pady=10)
        self.change_path_button.configure(command=master.change_path)

        # line 3

        self.progress_bar = customtkinter.CTkProgressBar(self.tab("Audio"), mode="determinate")
        self.progress_bar.grid(row=2, column=0, padx=15, pady=10, columnspan=3, sticky="ew")
        self.progress_bar.set(0)

        # line 4

        self.status_label = customtkinter.CTkLabel(self.tab("Audio"), text="Status")
        self.status_label.grid(row=3, column=2, padx=15, pady=10)

