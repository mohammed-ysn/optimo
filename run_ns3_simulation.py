import sys
import subprocess


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "customfirst"
    ns3_command = f"./ns-allinone-3.40/ns-3.40/ns3 run scratch/{filename}"

    print(f"Running ns3 command: {ns3_command}")
    subprocess.run(ns3_command, shell=True)


if __name__ == "__main__":
    main()
