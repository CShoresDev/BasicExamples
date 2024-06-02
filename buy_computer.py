# stores customer's choice.
choice = ""

# a list to append computer choices to.
computer_parts = []

# a list of available computer parts in the store.
available_parts = ["Mouse Pad",
                   "Keyboard",
                   "RAM",
                   "Mouse",
                   "Additional Software",
                   "HDMI Cable"]

# gets user input from options menu to determine what to do next.
while not choice == "0":

    choice = input("****************************************\n"
                   "What computer parts do you need?\n\t"
                   "-> Select \"1\" for \"Mouse Pad\"\n\t"
                   "-> Select \"2\" for \"Keyboard\"\n\t"
                   "-> Select \"3\" for \"RAM\"\n\t"
                   "-> Select \"4\" for \"Mouse\"\n\t"
                   "-> Select \"5\" for \"Additional Software\"\n\t"
                   "-> Select \"6\" for \"HDMI Cable\"\n\t"
                   "-> Select \"0\" to quit\n\t"
                   "************************************\nSelection:")

    if choice in "":
        pass
    elif choice in "1,2,3,4,5,6":
        print(f"Adding selection #{choice}...")
        computer_parts.append(available_parts[int(choice) - 1])
        print(f'Selection #{choice} was added successfully!')
else:
    # outputs the current elements in the list based on user selection from menu.
    print("Your Current Shopping List: {}".format(computer_parts))
