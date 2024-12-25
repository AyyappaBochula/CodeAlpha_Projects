import os
import shutil

def organize_files(directory):
    file_categories = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".sh"],
        "Others": []
    }

    for category in file_categories.keys():
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)


    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)

        moved = False
        for category, extensions in file_categories.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, category, filename))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))
    
    print(f"Files in {directory} have been organized!")

if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ")
    if os.path.exists(folder_to_organize):
        organize_files(folder_to_organize)
    else:
        print("The specified folder does not exist.")
