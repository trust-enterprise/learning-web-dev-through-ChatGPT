import os

# Directory path
directory = r"F:\memories\mine\WhatsApp Video"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .mp4 file
    if filename.endswith(".mp4"):
        # Create new filename by removing first 20 characters
        new_name = filename[20:]
        # Full paths for renaming
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")

print("Renaming complete!")
