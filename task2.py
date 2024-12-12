import os
import shutle
folder_path = '/path/to/your/folder'
file_extensions = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.ogg']
}
for filename in os.listdir(folder_path):
    file_extension = os.path.splitext(filename)[1].lower()
    for folder, extensions in file_extensions.items():
        if file_extension in extensions:
            shutle.move(os.path.join(folder_path, filename), os.path.join(folder_path, folder, filename))
            print(f"Moved {filename} to {folder} folder")
            break