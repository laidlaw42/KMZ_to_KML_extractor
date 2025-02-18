# KMZ Extraction & Backup Script

This Python script automates the extraction of `.kmz` files, renames the extracted `.kml`, organizes extracted images, and backs up the original files.  

## 📌 Features
- Extracts `.kmz` files in the script's directory.
- Moves the extracted `doc.kml` to the script's directory, renaming it based on the `.kmz` filename.
- Moves images from the extracted `images` folder into the main extracted directory.
- Renames the extracted folder by appending `_images` to the name.
- Moves the renamed `_images` directories and original `.kmz` files into a `KMZ_backups` folder.
- Preserves the **modified date and creation date** of the extracted `.kml` to match the original `.kmz`.

---

## 🛠️ How It Works

1. The script scans for all `.kmz` files in its directory.
2. Each `.kmz` is extracted into a folder named after the file (e.g., `25000_Survey_20250218.kmz` → `25000_Survey_20250218`).
3. The extracted `doc.kml` is renamed to match the `.kmz` filename and moved to the script’s directory.
4. All images from the `images` subdirectory are moved to the extracted folder.
5. The extracted folder is renamed by appending `_images` (e.g., `25000_Survey_20250218_images`).
6. The `_images` folder and the original `.kmz` file are moved to a `KMZ_backups` directory.
7. The extracted `.kml` file's timestamps are updated to match the original `.kmz`.

---

## 📂 Folder Structure

### **Before Running the Script**
```
📂 Project Folder
 ├── 25000_Survey_20250218.kmz
 ├── Another_File.kmz
 ├── KMZ_Extractor.py
```

### **After Running the Script**
```
📂 Project Folder
 ├── 25000_Survey_20250218.kml
 ├── Another_File.kml
 ├── 📂 KMZ_backups
 │   ├── 25000_Survey_20250218.kmz
 │   ├── Another_File.kmz
 │   ├── 📂 25000_Survey_20250218_images
 │   │   ├── overlay.jpg
 │   │   ├── icon.png
 │   ├── 📂 Another_File_images
 │       ├── image1.png
 │       ├── image2.png
```

---

## 🚀 Usage Instructions

### **1️⃣ Install Python (If Not Installed)**
Ensure you have Python **3.x** installed. You can check by running:
```sh
python --version
```

### **2️⃣ Place the Script in the Desired Folder**
Copy `KMZ_Extractor.py` into the folder containing `.kmz` files.

### **3️⃣ Run the Script**
Execute the script using:
```sh
python KMZ_Extractor.py
```

### **4️⃣ Check the Output**
- Extracted `.kml` files will be in the script’s directory.
- The `KMZ_backups` folder will contain all `_images` directories and `.kmz` backups.

---

## ⚙️ Requirements

- **Python 3.x**
- **Modules used**:  
  - `os` (built-in)
  - `shutil` (built-in)
  - `zipfile` (built-in)

No external dependencies are required.

---

## 📝 Notes

- Windows does not fully support changing the **creation date**, but the modified date will always match the original `.kmz`.
- If a `.kmz` file does not contain images, the script will skip the image-handling steps.
- Existing files with the same names **will be overwritten**, so ensure backups are made if needed.

---

## 📌 License
MIT license because I don't know the difference and can't be bothered reading.

---

## 📧 Contact
For any issues or suggestions, feel free to reach out.

---
