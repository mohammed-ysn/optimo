import os
import shutil


def copy_cc_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        # error
        print("Error: destination directory does not exist")
        return

    for file in os.listdir(source_dir):
        if file.endswith(".cc"):
            new_filename = "optimo-" + file
            shutil.copy(
                os.path.join(source_dir, file), os.path.join(dest_dir, new_filename)
            )
            print(f"Copied file: {file} -> {new_filename}")


if __name__ == "__main__":
    # Copy all .cc files from ns3_scripts directory to ns-3.40/scratch directory
    source_dir = "ns3_scripts"
    dest_dir = "./ns-allinone-3.40/ns-3.40/scratch"
    copy_cc_files(source_dir, dest_dir)
