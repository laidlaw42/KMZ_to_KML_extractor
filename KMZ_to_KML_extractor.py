import os
import zipfile
import shutil

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
backup_dir = os.path.join(script_dir, "KMZ_backups")

# Create the backup directory if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Loop through all KMZ files in the script directory
for kmz_file in os.listdir(script_dir):
    if kmz_file.endswith(".kmz"):
        kmz_path = os.path.join(script_dir, kmz_file)
        base_name = os.path.splitext(kmz_file)[0]  # Remove .kmz for base name
        extracted_dir = os.path.join(script_dir, base_name)  # Extracted folder
        new_extracted_dir = extracted_dir + "_images"  # Corrected renamed folder

        # Get the original timestamps from the KMZ file
        kmz_modified_time = os.path.getmtime(kmz_path)
        kmz_created_time = os.path.getctime(kmz_path)  # Creation time (Windows may not preserve)

        # Unzip the KMZ file
        with zipfile.ZipFile(kmz_path, "r") as zip_ref:
            zip_ref.extractall(extracted_dir)

        # Path of the extracted KML file
        kml_path = os.path.join(extracted_dir, "doc.kml")
        
        # New name for the KML file (same as KMZ but with .kml)
        new_kml_name = base_name + ".kml"
        new_kml_path = os.path.join(script_dir, new_kml_name)

        # Rename and move the KML file to the script's directory
        if os.path.exists(kml_path):
            shutil.move(kml_path, new_kml_path)
            print(f"Renamed and moved: {new_kml_name}")

            # Set the extracted KML's timestamps to match the original KMZ
            os.utime(new_kml_path, (kmz_modified_time, kmz_modified_time))  # Set modified & access time
            try:
                os.system(f'touch -t {kmz_created_time} "{new_kml_path}"')  # For Unix-based systems
            except:
                pass  # Ignore if not supported
            print(f"Preserved timestamps for: {new_kml_name}")

        # Handle images directory
        images_dir = os.path.join(extracted_dir, "images")
        if os.path.exists(images_dir) and os.path.isdir(images_dir):
            for img_file in os.listdir(images_dir):
                img_path = os.path.join(images_dir, img_file)
                if os.path.isfile(img_path):
                    shutil.move(img_path, extracted_dir)  # Move images to parent directory
            shutil.rmtree(images_dir)  # Remove empty "images" folder

        # Ensure the extracted folder is renamed properly
        if os.path.exists(extracted_dir):
            shutil.move(extracted_dir, new_extracted_dir)  # Correctly renames the folder
            print(f"Renamed folder: {new_extracted_dir}")

        # Move the renamed _images folder and KMZ file to the backup directory
        shutil.move(new_extracted_dir, backup_dir)
        shutil.move(kmz_path, backup_dir)
        print(f"Moved {new_extracted_dir} and {kmz_file} to {backup_dir}")

print("Processing complete.")
