import os
import zipfile
import shutil
from datetime import datetime

# Function to preserve the original modified and creation dates of the KML
def preserve_file_dates(src, dest):
    # Get the original file's timestamps
    stat = os.stat(src)
    mod_time = stat.st_mtime
    create_time = stat.st_ctime
    
    # Set the timestamps for the new file
    os.utime(dest, (mod_time, mod_time))  # Modify only the access and modified times
    os.utime(dest, (create_time, mod_time))  # Windows doesn't allow creation time change

# Walk through all directories and subdirectories
def process_kmz_files(root_folder):
    # Traverse the folder tree
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.kmz'):
                kmz_path = os.path.join(root, file)
                print(f"Processing {kmz_path}")

                # Extract the name without extension for renaming purposes
                base_name = os.path.splitext(file)[0]
                extracted_folder = os.path.join(root, base_name)

                # Step 1: Create the extraction folder
                if not os.path.exists(extracted_folder):
                    os.makedirs(extracted_folder)

                # Step 2: Extract the KMZ file
                with zipfile.ZipFile(kmz_path, 'r') as kmz:
                    kmz.extractall(extracted_folder)

                # Step 3: Rename and move the doc.kml to the parent folder
                doc_kml_path = os.path.join(extracted_folder, 'doc.kml')
                new_kml_name = os.path.join(root, base_name + '.kml')

                if os.path.exists(doc_kml_path):
                    os.rename(doc_kml_path, new_kml_name)

                    # Step 4: Preserve the timestamps of the KML file
                    preserve_file_dates(kmz_path, new_kml_name)

                # Step 5: Move the images folder contents to the parent folder
                images_folder = os.path.join(extracted_folder, 'images')
                if os.path.isdir(images_folder):
                    images_target_folder = os.path.join(root, base_name + '_images')
                    
                    if not os.path.exists(images_target_folder):
                        os.makedirs(images_target_folder)

                    # Move all images from the 'images' folder
                    for image_file in os.listdir(images_folder):
                        src_image_path = os.path.join(images_folder, image_file)
                        dst_image_path = os.path.join(images_target_folder, image_file)
                        if os.path.isfile(src_image_path):
                            shutil.move(src_image_path, dst_image_path)

                # Step 6: Rename the extracted folder and move it to a KMZ_backups folder
                kmz_backups_folder = os.path.join(root, 'KMZ_backups')
                if not os.path.exists(kmz_backups_folder):
                    os.makedirs(kmz_backups_folder)

                # Rename the folder to include _images and move it to KMZ_backups
                images_target_folder = os.path.join(root, base_name + '_images')
                if os.path.isdir(images_target_folder):
                    shutil.move(images_target_folder, os.path.join(kmz_backups_folder, base_name + '_images'))

                # Move the original KMZ file to the backups folder
                shutil.move(kmz_path, kmz_backups_folder)

                # Clean up the extracted folder
                shutil.rmtree(extracted_folder)

if __name__ == '__main__':
    # Get the current directory where the script is located
    script_directory = os.path.dirname(os.path.realpath(__file__))
    process_kmz_files(script_directory)
