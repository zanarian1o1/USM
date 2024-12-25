import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading

class UnturnedServerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Unturned Server Manager")
        self.server_folder = ""

        # Create UI elements
        self.create_widgets()

    def select_folder(self):
        self.server_folder = filedialog.askdirectory(title="Select Unturned Server Folder")
        if self.server_folder:
            self.load_files()  # Ensure this method is defined

    def create_widgets(self):
        # Button to select server folder
        self.select_folder_button = tk.Button(self.root, text="Select Server Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=10)

        # Listbox to display files
        self.file_listbox = tk.Listbox(self.root)
        self.file_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.file_listbox.bind('<<ListboxSelect>>', self.load_file_content)

        # Text area to edit file content
        self.file_content = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.file_content.pack(pady=10, fill=tk.BOTH, expand=True)  # Allow text area to expand

        # Save button
        self.save_button = tk.Button(self.root, text="Save Changes", command=self.save_file)
        self.save_button.pack(pady=10)

        # Help button
        self.help_button = tk.Button(self.root, text="Help", command=self.help)
        self.help_button.pack(pady=10)

    def load_files(self):
        self.file_listbox.delete(0, tk.END)
        specific_files = ['Commands.dat', 'Banlist.dat', 'Config.json', 'WorkshopDownloadConfig.json', 'Whitelist.dat', 'Blacklist.dat', 'Adminlist.dat']  # Add more as needed
        found_files = set()  # Ensure this is a set to keep track of unique files
        
        # Walk through the directory tree
        for root, dirs, files in os.walk(self.server_folder):
            # Exclude "Maps" and "Workshop" directories
            dirs[:] = [d for d in dirs if d.lower() not in ['maps', 'workshop']]

            for file in files:
                if file in specific_files:
                    full_path = os.path.join(root, file)
                    found_files.add(os.path.normpath(full_path))  # Normalize the path and add to the set

        # Populate the listbox with found files
        for file in found_files:
            self.file_listbox.insert(tk.END, os.path.basename(file))  # Insert only the file name

        # Debugging output
        if not found_files:
            print("No specified files found in the selected folder.")
        else:
            print(f"Found files: {found_files}")

    def load_file_content(self, event):
        # Check if there is a selection
        if not self.file_listbox.curselection():
            return  # Exit the method if no item is selected

        selected_file = self.file_listbox.get(self.file_listbox.curselection())
        threading.Thread(target=self.read_file, args=(selected_file,)).start()  # Start a new thread for reading the file

    def read_file(self, selected_file):
        file_path = None

        # Construct the full path using the found files list
        for root, dirs, files in os.walk(self.server_folder):
            for file in files:
                if file == selected_file:
                    file_path = os.path.join(root, file)
                    file_path = os.path.normpath(file_path)  # Normalize the path
                    break  # Exit the loop once the file is found

        # Check if the file_path was found
        if file_path and os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Use the main thread to update the GUI
                    self.root.after(0, lambda: self.update_text_area(content))
            except Exception as e:
                print(f"An error occurred: {e}")  # Print the error message for debugging
                self.root.after(0, lambda: messagebox.showerror("Error", f"An unexpected error occurred: {e}"))
        else:
            print(f"File not found: {selected_file}")  # Debugging output
            self.root.after(0, lambda: messagebox.showerror("Error", f"The file {selected_file} could not be found."))

    def help(self):
        help_text = (
            "this does not go over how to forward your server onto the internet, that is a whole different topic.\n"
            "thats a bit to complicated for me to add to this program, maybe at a later date.\n"
            "this program is designed to just help edit your servers settings, and to make it easier to find the files you need to edit.\n"
            "So for the time being, if you follow this tutorial, it will just be a lan server.\n"

            "fist off, you need to install and run Unturned server manager once, if you havent already.\n"
            "then use the select folder button to select the folder where your server is installed.\n"
            "typically (r'C:\\Program Files (x86)\\Steam\\steamapps\\common\\U3DS\\Servers\\Default').\n"
            "then you can select the file you want to edit from the list:\n\n"

            "1. Main Setup\n"
            "Folder: [Commands.dat]\n"
            "Instructions:\n"
            "Open [Commands.dat] to configure your server settings.\n"
            "Modify the following parameters:\n"
            "name : [your server name] - Set the name of your server.\n"
            "password: [optional] - Set if you want a private server.\n"
            "bind: [bind address] - Use the bind address provided by your game server host.\n"
            "port: [port number] - Specify the port for your server.\n"
            "cycle: [day/night cycle] - Set the day/night cycle (e.g., circle 90 for 90 seconds).\n"
            "mode: [game mode] - Choose the game mode (easy, normal, or hard).\n"
            "PVP or PVE: [choice] - Select between player vs player or player vs environment.\n"
            "perspective: [view type] - Choose first, third, or both.\n"
            "map: [map name] - Select from standard maps (PEI, Washington, Yukon, Russia, Germany) or add modded/curated maps.\n"
            "cheats: [True/False] - Allow admins to give items.\n"
            "owner: [Name or SteamID64] - Enter your SteamID64.\n"
            "maxplayers: [1-24] - Set the maximum number of players.\n"
            "welcome: [welcome message] - Customize the welcome message.\n"
            "Loadout: [skillsetID/ItemID/... ] - Define loadouts using the format [skillsetID]/[ItemID]/... .\n"
            "Queue_Size: [size] - Set the size of the server queue.\n"
            "Votify: [voting settings] - Configure voting settings.\n"
            "Chatrate: [time in seconds] - Set a minimum time between chat messages.\n"
            "Whitelisted: [True/False] - Enable whitelisting for your server.\n\n"

            "2. Configuring Loadouts\n"
            "Folder: [Commands.dat]\n"
            "Instructions:\n"
            "Use the command /Loadout [skillsetID]/[ItemID]/... to set up loadouts.\n"
            "Example: /Loadout 255/253/15/15 gives players specific items upon spawning.\n"
            "You can also add loadouts to the commands folder for automatic loading at server start.\n\n"

            "3. Adding Workshop Content\n"
            "Folder: [Steam > steamapps > common > Unturned > Servers > Servername > Workshop > content]\n"
            "Instructions:\n"
            "Find a workshop mod you want to add.\n"
            "Subscribe to the mod on Steam.\n"
            "Move the mod folder from [Steam > Steamapps > Workshop > Content > 304930] to the specified workshop content folder.\n"
            "But even better, edit [WorkshopDownloadConfig.json] in the server folder to include the mod ID.\n\n"

            "4. Server Commands\n"
            "Folder: [N/A (Commands are executed in-game)]\n"
            "Instructions:\n"
            "Use the following commands as needed:\n"
            "/admin [Name or SteamID64] - Grant admin privileges.\n"
            "/unadmin [Name or SteamID64] - Remove admin privileges.\n"
            "/day or /night - Change the time of day.\n"
            "/weather [storm/blizzard] - Change weather conditions.\n"
            "/broadcast [message] - Send a message to all players.\n"
            "/give [ID or \"item name\"] - Give an item to a player.\n"
            "/kick [player] - Kick a player from the server.\n"
            "/ban [player] - Ban a player from the server.\n"
            "/save - Save the server state.\n\n"

            "Now just run from steam or file explorer and enjoy your server!\n\n"
        )

        # Create a new window for help
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("600x400")  # Set a fixed size for the window
        help_window.configure(bg="#f0f0f0")  # Set a background color

        # Create a frame to hold the text and scrollbar
        frame = tk.Frame(help_window, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Add padding

        # Create a Text widget with a specific font
        text = tk.Text(frame, wrap=tk.WORD, font=("Arial", 10), bg="#ffffff", fg="#000000")
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Insert the help text into the text widget
        text.insert(tk.END, help_text)

        # Make the text widget read-only
        text.config(state=tk.DISABLED)

        # Add a scrollbar
        scrollbar = tk.Scrollbar(frame, command=text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.config(yscrollcommand=scrollbar.set)

    def save_file(self):
        # Check if there is a selection
        if not self.file_listbox.curselection():
            messagebox.showwarning("Warning", "No file selected to save.")
            return  # Exit the method if no item is selected

        selected_file = self.file_listbox.get(self.file_listbox.curselection())
        threading.Thread(target=self.write_file, args=(selected_file,)).start()  # Start a new thread for saving the file

    def write_file(self, selected_file):
        file_path = None

        # Construct the full path using the found files list
        for root, dirs, files in os.walk(self.server_folder):
            for file in files:
                if file == selected_file:
                    file_path = os.path.join(root, file)
                    file_path = os.path.normpath(file_path)  # Normalize the path
                    break  # Exit the loop once the file is found

        # Check if the file_path was found
        if file_path and os.path.isfile(file_path):
            try:
                content = self.file_content.get(1.0, tk.END)  # Get content from the text area
                with open(file_path, 'w') as f:
                    f.write(content)  # Write the content back to the file
                self.root.after(0, lambda: messagebox.showinfo("Success", f"Changes saved to {selected_file}"))
            except Exception as e:
                print(f"An error occurred: {e}")  # Print the error message for debugging
                self.root.after(0, lambda: messagebox.showerror("Error", f"An unexpected error occurred: {e}"))
        else:
            print(f"File not found: {file_path}")  # Debugging output
            self.root.after(0, lambda: messagebox.showerror("Error", f"The file {selected_file} could not be found."))    

    def update_text_area(self, content):
        self.file_content.delete(1.0, tk.END)
        self.file_content.insert(tk.END, content)

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = UnturnedServerManager(root)
    root.mainloop()
