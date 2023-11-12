from downloader import Downloader


while True:
    choice = input(
        "Welcome to YouTube Downloader!\n"
        "- Enter 1 for Command Line Interface\n"
        "- Enter 2 for Graphical User Interface\n"
        "- Enter 'exit' to Exit\n"
        "Enter your input: "
    )

    if choice == "1":
        Downloader.cli()

    elif choice == "2":
        Downloader.gui()

    elif choice.lower() == "exit":
        print("\nThank you for using Youtube Downloader. See you soon!")
        exit()

    else:
        print(f"'{choice}' is not part of the options. Try again...\n")
