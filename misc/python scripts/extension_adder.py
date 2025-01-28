import os

# Path to the folder
folder_path = r"C:\Users\Tahseen Fatima\Desktop\pics"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    # Check if it's a file and doesn't already have an extension
    if os.path.isfile(file_path) and not filename.endswith(".jpg"):
        # Rename the file by adding the .jpg extension
        new_filename = f"{filename}.jpg"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)

print("All files have been renamed with .jpg extension.")
