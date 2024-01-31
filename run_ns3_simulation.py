import subprocess
import sys

import copy_scripts


def main():
    if "--copy-scripts" in sys.argv:
        copy_scripts.copy_cc_files("my_scripts", "./ns-allinone-3.40/ns-3.40/scratch")
        sys.argv.remove("--copy-scripts")

    filename = sys.argv[1] if len(sys.argv) > 1 else "customfirst"
    ns3_command = f"./ns-allinone-3.40/ns-3.40/ns3 run scratch/{filename}"

    print(f"Running ns3 command: {ns3_command}")
    subprocess.run(ns3_command, shell=True)


if __name__ == "__main__":
    main()
