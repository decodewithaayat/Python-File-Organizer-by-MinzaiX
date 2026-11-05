<h1 align="center">📁 Python File Organizer</h1>

<p align="center">
  A simple command-line tool that automatically sorts messy folders into clean, categorized folders.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Dependencies-None-brightgreen?style=for-the-badge" alt="No dependencies">
</p>

---

## 📌 About

Downloads folders usually get cluttered with PDFs, images, videos, and installers all mixed together.
This script scans a folder and moves every file into a category folder based on its file extension.

## ✨ Features

- Sorts files into categories: **PDFs, Documents, Images, Videos, Music, Archives, Python, C, C++, Java, JavaScript, HTML, CSS, Data, Executables, Disk Images**
- Unknown file types go into an **Others** folder
- **Duplicate-safe**: if a file with the same name exists, it is renamed (`photo.jpg` → `photo_1.jpg`) instead of being overwritten
- Shows a live log of every moved file
- Prints a **summary** at the end (files moved, files skipped, total size)
- Handles permission errors and invalid paths without crashing
- Works with paths pasted with quotes (`"C:\Users\Me\Downloads"`)

## 🛠️ Tech Used

- Python 3.6+
- Built-in modules only: `os`, `shutil` (no installation needed)

## 🚀 How to Run

1. Install [Python](https://www.python.org/downloads/) (3.6 or higher)
2. Clone this repository:
   ```bash
   git clone https://github.com/decodewithaayat/Python-File-Organizer-by-MinzaiX.git
   cd Python-File-Organizer-by-MinzaiX
   ```
3. Run the script (replace `main.py` with your file name):
   ```bash
   python main.py
   ```
4. Enter the folder path when asked, for example:
   ```
   Enter folder path to organize: C:\Users\Aayat\Downloads
   ```

## 🖥️ Example Output

```
✓ resume.pdf                     → PDFs
✓ photo.jpg                      → Images
✓ song.mp3                       → Music
✓ setup.exe                      → Executables

==================================================
                    SUMMARY
==================================================
Files moved   : 4
Files skipped : 0
Total size    : 12.35 MB

✅ Organization completed!
```

## 📂 Folder Structure After Running

```
Downloads/
├── PDFs/
├── Images/
├── Music/
├── Executables/
└── Others/
```

## ⚠️ Note

- This tool **moves** files (it does not copy). Test it on a small sample folder first.
- Only files directly inside the selected folder are organized. Existing sub-folders are not touched.

## 🔮 Future Improvements

- [ ] Undo option
- [ ] Preview mode (show what will move, without moving)
- [ ] Organize files by date
- [ ] GUI version

## 👨‍💻 Author

**Shaikh Aayat Ullah** (MinzaiX)
[GitHub](https://github.com/decodewithaayat) • [LinkedIn](https://www.linkedin.com/in/shaikh-aayat-a34797392)
