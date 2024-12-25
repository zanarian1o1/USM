## USM
# Unturned Server Manager
=======================

Overview
--------
The Unturned Server Manager is a graphical user interface (GUI) application designed to help users manage and edit their Unturned game server settings easily. This program allows you to select your server folder, view specific configuration files, edit their contents, and save changes seamlessly.

Features
--------
- Select the Unturned server folder using a file dialog.
- View and edit specific configuration files such as:
  - Commands.dat
  - Banlist.dat
  - Config.json
  - WorkshopDownloadConfig.json
  - Whitelist.dat
  - Blacklist.dat
  - Adminlist.dat
- Save changes made to the configuration files.
- Help section providing detailed instructions on server setup and configuration.

Requirements
------------
- Python 3.x
- Tkinter (usually included with Python installations)
- Basic knowledge of Unturned server configuration files.

Installation
------------
1. Ensure you have Python 3.x installed on your system.
2. Download the script file (e.g., `unturned_server_manager.py`).
3. Run the script using Python: python unturned_server_manager.py


Usage
-----
1. Launch the application.
2. Click the "Select Server Folder" button to choose the folder where your Unturned server is installed. The default path is typically: [C:\Program Files (x86)\Steam\steamapps\common\U3DS\Servers\Default]
3. Once the folder is selected, the application will display a list of specific configuration files found in that folder.
4. Select a file from the list to view and edit its contents in the text area.
5. After making changes, click the "Save Changes" button to save your modifications.
6. For assistance, click the "Help" button to view detailed instructions on configuring your server.

Help Section
------------
There is a help section which provides guidance on:
- Main server setup and configuration.
- Configuring loadouts for players.
- Adding workshop content to your server.
- Using server commands in-game.

Troubleshooting
---------------
- If you encounter issues with file access, ensure that the selected folder contains the necessary configuration files.
- Check for any permission issues that may prevent the application from reading or writing files.

Contact
-------
For any questions or feedback, please reach out to the developer.

Enjoy managing your Unturned server!
