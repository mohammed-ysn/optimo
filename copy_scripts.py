import os
import shutil


def copy_cc_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        # error
        print("Error: destination directory does not exist")
        return

    for file in os.listdir(source_dir):
        if file.endswith(".cc"):
            shutil.copy(os.path.join(source_dir, file), dest_dir)
            print("Copied file: " + file)


if __name__ == "__main__":
    # Copy all .cc files from my_scripts directory to ns-3.40/scratch directory
    source_dir = "my_scripts"
    dest_dir = "./ns-allinone-3.40/ns-3.40/scratch"
    copy_cc_files(source_dir, dest_dir)