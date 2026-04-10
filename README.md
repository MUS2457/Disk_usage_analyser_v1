# File Management Tool

A simple, interactive command-line tool that helps you explore and analyze files inside any folder.  
It provides searching, counting, duplicate detection, and modification-date analysis through a clean menu interface.

---

## Features

### Search File by Name
Find files by entering their name (without extension). Searches all subfolders.

### Search File by Extension
Find all files with a specific extension (e.g., `.png`, `.txt`, `.mp4`).

### Search File Size
Enter an exact filename and get its size in bytes, including duplicates with the same name.

### Count All Files
Shows the total number of files inside the folder (including subfolders).

### Count Files by Extension Type
Counts files grouped by category (documents, images, audio, video, archives, code, etc.).

### Show Duplicate Files
Detects duplicate files based on size.

### Last Modification by Day
Shows how many days ago each file was last modified.

### Show All File Sizes
Lists every file grouped by its size in bytes.

### Count Files by Size
Shows how many files share the same size.

### Exit
Closes the program.

---

## How It Works

1. The program asks you for a folder path.  
2. It verifies the folder exists.  
3. You choose an option from the menu.  
4. The tool performs the requested analysis and prints the results.

All operations automatically scan subfolders.


## Running the Program

```bash
python main.py
