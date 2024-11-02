import os
import shutil

def move_to_destination(source_path, destination_path):
    def copy_file_to_destination(current_source_path, current_dest_path):
        for item in os.listdir(current_source_path):
            source_item_path = os.path.join(current_source_path, item)
            dest_file_path = os.path.join(current_dest_path, item)
            if os.path.isdir(source_item_path):
                os.mkdir(os.path.join(destination_path, item))
                copy_file_to_destination(source_item_path, dest_file_path)
            if os.path.isfile(source_item_path):
                print(f'file {item}')
                (shutil.copy(source_item_path, dest_file_path))


    mypath = destination_path
    for root, dirs, files in os.walk(mypath, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
    for dir in dirs:
        os.rmdir(os.path.join(root, dir))
    copy_file_to_destination(source_path, destination_path)