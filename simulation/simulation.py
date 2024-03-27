import shutil
import subprocess
import os


SIMULATION_OUTPUT_DIR = "simulation_output"


class NS3Simulation:
    def __init__(
        self,
        filename,
        duration,
        copy_scripts=False,
        tcp_variant="TcpWestwoodPlus",
    ):
        self.filename = filename
        if not os.path.isfile(f"./ns-allinone-3.40/ns-3.40/scratch/{filename}.cc"):
            print(
                f"Warning: file ./ns-allinone-3.40/ns-3.40/scratch/{filename}.cc not found"
            )
            print("Hint: You may want to set the copy_scripts parameter to True")

        self.copy_scripts = copy_scripts
        self.tcp_variant = tcp_variant
        self.duration = duration

    def set_tcp_variant(self, tcp_variant):
        # Transport protocol to use: TcpNewReno, TcpLinuxReno,
        # TcpHybla, TcpHighSpeed, TcpHtcp, TcpVegas, TcpScalable, TcpVeno,
        # TcpBic, TcpYeah, TcpIllinois, TcpWestwoodPlus, TcpLedbat,
        # TcpLp, TcpDctcp, TcpCubic, TcpBbr
        self.tcp_variant = tcp_variant

    def set_duration(self, duration):
        self.duration = duration

    def run(self):
        # Copy the .cc files to the ns3 scratch directory
        if self.copy_scripts:
            source_dir = os.path.join(os.path.dirname(__file__), "../ns3_scripts")
            dest_dir = os.path.join(
                os.path.dirname(__file__), "../ns-allinone-3.40/ns-3.40/scratch"
            )

            if not os.path.exists(dest_dir):
                print("Error: destination directory does not exist")
                print("Hint: Run the setup.sh script to set up the ns3 environment")
                return

            for file in os.listdir(source_dir):
                if file.endswith(".cc"):
                    new_filename = "optimo-" + file
                    shutil.copy(
                        os.path.join(source_dir, file),
                        os.path.join(dest_dir, new_filename),
                    )
                    print(f"Copied file: {file} -> {new_filename}")

        # Create the output directory if it does not exist
        if not os.path.exists(SIMULATION_OUTPUT_DIR):
            os.makedirs(SIMULATION_OUTPUT_DIR)

        ns3_command = (
            f'./ns-allinone-3.40/ns-3.40/ns3 run "scratch/optimo-{self.filename} '
            f"--transport_prot={self.tcp_variant} "
            f"--duration={self.duration} "
            f"--tracing=true "
            f"--pcap_tracing=true "
            '" '
            f"--cwd={SIMULATION_OUTPUT_DIR}"
        )
        print(f"Running ns3 command: {ns3_command}")
        subprocess.run(ns3_command, shell=True)
        print("Simulation completed!")
