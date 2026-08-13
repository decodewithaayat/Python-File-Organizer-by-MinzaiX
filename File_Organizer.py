import os
import shutil


# ==================================================
#              PYTHON FILE ORGANIZER
#              Developed by MinzaiX
#              GitHub: decodewithaayat
# ==================================================

print("""
==================================================
             PYTHON FILE ORGANIZER
             Developed by MinzaiX
             GitHub: decodewithaayat
==================================================
""")


FILE_CATEGORIES = {
    # Documents
    "pdf": "PDFs",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Text Files",
    "rtf": "Documents",
    "odt": "Documents",

    # Images
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "svg": "Images",
    "webp": "Images",

    # Videos
    "mp4": "Videos",
    "mkv": "Videos",
    "avi": "Videos",
    "mov": "Videos",
    "flv": "Videos",
    "wmv": "Videos",

    # Music
    "mp3": "Music",
    "wav": "Music",
    "aac": "Music",
    "flac": "Music",
    "ogg": "Music",

    # Archives
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "tar": "Archives",
    "gz": "Archives",

    # Programming
    "py": "Python",
    "c": "C",
    "cpp": "C++",
    "java": "Java",
    "js": "JavaScript",
    "html": "HTML",
    "css": "CSS",

    # Data
    "csv": "Data",
    "xlsx": "Data",
    "xls": "Data",
    "json": "Data",
    "xml": "Data",

    # Executables
    "exe": "Executables",
    "msi": "Executables",

    # Disk Images
    "iso": "Disk Images",
}


def get_file_size(file_path):
    """Return file size in KB."""
    size = os.path.getsize(file_path)
    return size / 1024


def get_unique_path(destination):
    """
    If a file already exists, create a new filename.

    Example:
    photo.jpg
    photo_1.jpg
    photo_2.jpg
    """

    if not os.path.exists(destination):
        return destination

    directory = os.path.dirname(destination)
    filename = os.path.basename(destination)

    name, extension = os.path.splitext(filename)

    counter = 1

    while True:
        new_filename = f"{name}_{counter}{extension}"
        new_destination = os.path.join(directory, new_filename)

        if not os.path.exists(new_destination):
            return new_destination

        counter += 1


def organize_files(directory):
    """Organize files inside the selected directory."""

    if not os.path.exists(directory):
        print("\n❌ Directory does not exist.")
        return

    if not os.path.isdir(directory):
        print("\n❌ The given path is not a directory.")
        return

    moved_files = 0
    skipped_files = 0
    total_size = 0

    # Existing folders created by the organizer
    organizer_folders = set(FILE_CATEGORIES.values())
    organizer_folders.add("Others")

    for filename in os.listdir(directory):

        file_path = os.path.join(directory, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        # Get file extension
        extension = os.path.splitext(filename)[1].lower().replace(".", "")

        # Determine category
        category = FILE_CATEGORIES.get(extension, "Others")

        # Create destination folder
        destination_folder = os.path.join(directory, category)

        try:
            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(
                destination_folder,
                filename
            )

            # Handle duplicate filenames
            destination = get_unique_path(destination)

            # Get file size before moving
            file_size = get_file_size(file_path)

            # Move file
            shutil.move(file_path, destination)

            moved_files += 1
            total_size += file_size

            print(
                f"✓ {filename:<30} → {category}"
            )

        except PermissionError:
            skipped_files += 1
            print(f"⚠ Permission denied: {filename}")

        except Exception as error:
            skipped_files += 1
            print(f"⚠ Error with {filename}: {error}")

    # Summary
    print("\n" + "=" * 50)
    print("                    SUMMARY")
    print("=" * 50)

    print(f"Files moved   : {moved_files}")
    print(f"Files skipped : {skipped_files}")
    print(f"Total size    : {total_size / 1024:.2f} MB")

    print("\n✅ Organization completed!")
    print("Developed by MinzaiX")
    print("GitHub: decodewithaayat")


def main():
    """Main program."""

    print("\nPython File Organizer")
    print("-" * 30)

    directory = input(
        "Enter folder path to organize: "
    ).strip()

    # Remove quotes if user pastes a quoted path
    directory = directory.strip('"')

    organize_files(directory)


if __name__ == "__main__":
    main()